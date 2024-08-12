using System;
using System.Reflection;
using System.Collections.Generic;
using System.IO;

namespace PyStubblerLib
{
    public static class StubBuilder
    {
        private static List<string> SearchPaths { get; set; } = new List<string>();

        public static string BuildAssemblyStubs(string targetAssemblyPath, string destPath = null, string[] searchPaths = null, BuildConfig cfgs = null)
        {
            // prepare configs
            if (cfgs is null)
                cfgs = new BuildConfig();

            // prepare resolver
            AppDomain.CurrentDomain.AssemblyResolve -= AssemblyResolve;
            AppDomain.CurrentDomain.AssemblyResolve += AssemblyResolve;

            // pick a dll and load
            Assembly assemblyToStub = Assembly.LoadFrom(targetAssemblyPath);
            SearchPaths.Add(targetAssemblyPath);
            if (searchPaths != null)
                SearchPaths.AddRange(searchPaths);

            // extract types
            Type[] typesToStub = assemblyToStub.GetExportedTypes();
            string rootNamespace = typesToStub[0].Namespace.Split('.')[0];

            // prepare output directory
            DirectoryInfo stubsDirectory;
            if (cfgs.DestPathIsRoot && Directory.Exists(destPath))
            {
                stubsDirectory = new DirectoryInfo(destPath);
            }
            else
            {
                var extendedRootNS = cfgs.Prefix + rootNamespace + cfgs.Postfix;
                if (destPath is null || !Directory.Exists(destPath))
                    stubsDirectory = Directory.CreateDirectory(extendedRootNS);
                else
                    stubsDirectory = Directory.CreateDirectory(Path.Combine(destPath, extendedRootNS));
            }

            // build type db
            var stubDictionary = new Dictionary<string, List<Type>>();
            foreach (var stubType in typesToStub)
            {
                if (!stubDictionary.ContainsKey(stubType.Namespace))
                    stubDictionary[stubType.Namespace] = new List<Type>();
                stubDictionary[stubType.Namespace].Add(stubType);
            }

            List<string> namespaces = new List<string>(stubDictionary.Keys);

            // generate stubs for each type
            foreach (var stubList in stubDictionary.Values)
                WriteStubList(stubsDirectory, namespaces.ToArray(), stubList);

            // update the setup.py version with the matching version of the assembly
            var parentDirectory = stubsDirectory.Parent;
            string setup_py = Path.Combine(parentDirectory.FullName, "setup.py");
            if( File.Exists(setup_py))
            {
                string[] contents = File.ReadAllLines(setup_py);
                for( int i=0; i<contents.Length; i++ )
                {
                    string line = contents[i].Trim();
                    if( line.StartsWith("version=") )
                    {
                        line = contents[i].Substring(0, contents[i].IndexOf("="));
                        var version = assemblyToStub.GetName().Version;
                        line = line + $"=\"{version.Major}.{version.Minor}.{version.Build}\",";
                        contents[i] = line;
                    }
                }
                File.WriteAllLines(setup_py, contents);
            }

            // Update the requirements for for Rhino-stubs.
            if (assemblyToStub.GetName().Name.Equals("RhinoCommon", StringComparison.InvariantCulture))
            {
                var contents = new System.Text.StringBuilder();
                contents.AppendLine("--index-url https://pypi.python.org/simple/");
                contents.AppendLine();

                var version = assemblyToStub.GetName().Version;
                contents.AppendLine($"GH_IO-stubs=={version.Major}.{version.Minor}.{version.Build}");
                contents.AppendLine($"GH_Util-stubs=={version.Major}.{version.Minor}.{version.Build}");
                contents.AppendLine($"Grasshopper=={version.Major}.{version.Minor}.{version.Build}");
                string requirementsPath = Path.Combine(parentDirectory.FullName, "requirements.txt");
                File.WriteAllText(requirementsPath, contents.ToString());
            }

            return stubsDirectory.FullName;
        }

        private static Assembly AssemblyResolve(object sender, ResolveEventArgs args)
        {
            string assemblyToResolve = args.Name.Substring(0, args.Name.IndexOf(',')) + ".dll";

            // try to find the dll in given search paths
            foreach (var searchPath in SearchPaths)
            {
                string assemblyPath = Path.Combine(searchPath, assemblyToResolve);
                if (File.Exists(assemblyPath))
                    return Assembly.LoadFrom(assemblyPath);
            }

            // say i don't know
            return null;
        }

        private static string[] GetChildNamespaces(string parentNamespace, string[] allNamespaces)
        {
            List<string> childNamespaces = new List<string>();
            foreach(var ns in allNamespaces)
            {
                if( ns.StartsWith(parentNamespace + "."))
                {
                    string childNamespace = ns.Substring(parentNamespace.Length + 1);
                    if (!childNamespace.Contains("."))
                        childNamespaces.Add(childNamespace);
                }
            }
            childNamespaces.Sort();
            return childNamespaces.ToArray();
        }


        private static void WriteStubList(DirectoryInfo rootDirectory, string[] allNamespaces, List<Type> stubTypes)
        {
            // sort the stub list so we get consistent output over time
            stubTypes.Sort((a, b) => { return a.Name.CompareTo(b.Name); });

            string[] ns = stubTypes[0].Namespace.Split('.');
            string path = rootDirectory.FullName;
            for (int i = 1; i < ns.Length; i++)
                path = Path.Combine(path, ns[i]);

            if (!Directory.Exists(path))
                Directory.CreateDirectory(path);

            path = Path.Combine(path, "__init__.pyi");

            var sb = new System.Text.StringBuilder();

            string[] allChildNamespaces = GetChildNamespaces(stubTypes[0].Namespace, allNamespaces);
            sb.AppendLine("from typing import Tuple, Set, Iterable, List, overload");
            sb.AppendLine("from enum import Enum");
            sb.Append("\n");
            if( allChildNamespaces.Length>0 )
            {                
                for(int i=0; i<allChildNamespaces.Length; i++)
                {
                    sb.AppendLine($"import {allChildNamespaces[i]}");
                }
                sb.Append("\n");
                sb.Append("__all__ = [");
                for(int i=0; i<allChildNamespaces.Length; i++)
                {
                    if (i > 0)
                        sb.Append(", ");
                    sb.Append($"'{allChildNamespaces[i]}'");
                }
                sb.AppendLine("]");
            }

            foreach (var stubType in stubTypes)
            {
                var obsolete = stubType.GetCustomAttribute(typeof(System.ObsoleteAttribute));
                if (obsolete != null)
                    continue;

                sb.AppendLine();
                sb.AppendLine();
                if (stubType.IsGenericType)
                    continue; //skip generics for now
                if (stubType.IsEnum)
                {
                    sb.AppendLine($"class {stubType.Name}(Enum):");
                    var names = Enum.GetNames(stubType);
                    var values = Enum.GetValues(stubType);
                    for (int i = 0; i < names.Length; i++)
                    {
                        string name = names[i];
                        if (name.Equals("None", StringComparison.Ordinal))
                            name = $"{name}_";
                        else if (name.Equals("assert", StringComparison.Ordinal))
                            name = $"{name}_";

                        object val = Convert.ChangeType(values.GetValue(i), Type.GetTypeCode(stubType));
                        sb.AppendLine($"    {name} = {val}");
                    }
                    continue;
                }

                // get the list of constructors and methods
                ConstructorInfo[] constructors = stubType.GetConstructors();
                MethodInfo[] methods = stubType.GetMethods();

                // import parameter types
                HashSet<Tuple<string, string>> paramImports = new HashSet<Tuple<string, string>>();
                foreach (var constructor in constructors)
                {
                    var parameters = constructor.GetParameters();
                    for (int i = 0; i < parameters.Length; i++)
                    {
                        var param = parameters[i];
                        var paramType = param.ParameterType;
                        var relativeNamespace = FindRelativeNamespace(
                            stubType.Namespace, paramType.Namespace
                        );
                        if (relativeNamespace == null)
                            continue;
                        paramImports.Add(
                            Tuple.Create(relativeNamespace, ToPythonType(paramType.Name))
                        );
                    }
                }
                foreach (var method in methods)
                {
                    var parameters = method.GetParameters();
                    for (int i = 0; i < parameters.Length; i++)
                    {
                        var param = parameters[i];
                        var paramType = param.ParameterType;
                        var relativeNamespace = FindRelativeNamespace(
                            stubType.Namespace, paramType.Namespace
                        );
                        if (relativeNamespace == null)
                            continue;
                        paramImports.Add(
                            Tuple.Create(relativeNamespace, ToPythonType(paramType.Name))
                        );
                    }
                }
                foreach (var paramImport in paramImports)
                {
                    var relativeNamespace = paramImport.Item1;
                    var paramType = paramImport.Item2;
                    if (paramType.EndsWith("]"))
                        continue;
                    if (relativeNamespace != "" && relativeNamespace != ".")
                        sb.AppendLine($"from {relativeNamespace} import {paramType}");
                }

                // write class definition
                if (stubType.BaseType != null &&
                  stubType.BaseType.FullName.StartsWith(ns[0]) &&
                  stubType.BaseType.FullName.IndexOf('+') < 0 &&
                  stubType.BaseType.FullName.IndexOf('`') < 0
                ) {
                    var relativeNamespace = FindRelativeNamespace(
                        stubType.Namespace, stubType.BaseType.Namespace
                    );
                    if (relativeNamespace != "" && relativeNamespace != ".")
                        sb.AppendLine($"from {relativeNamespace} import {stubType.BaseType.Name}");
                    sb.AppendLine($"class {stubType.Name}({stubType.BaseType.Name}):");
                }
                else
                    sb.AppendLine($"class {stubType.Name}:");

                string classStartString = sb.ToString();

                // sort for consistent output
                Array.Sort(constructors, MethodCompare);
                foreach (var constructor in constructors)
                {
                    if (constructors.Length > 1)
                        sb.AppendLine("    @overload");
                    sb.Append("    def __init__(self");
                    var parameters = constructor.GetParameters();
                    for (int i = 0; i < parameters.Length; i++)
                    {
                        if (0 == i)
                            sb.Append(", ");
                        sb.Append($"{SafePythonName(parameters[i].Name)}: {ToPythonType(parameters[i].ParameterType)}");
                        if (i < (parameters.Length - 1))
                            sb.Append(", ");
                    }
                    sb.AppendLine("): ...");
                }

                // sort for consistent output
                Array.Sort(methods, MethodCompare);
                Dictionary<string, int> methodNames = new Dictionary<string, int>();
                foreach (var method in methods)
                {
                    if (method.GetCustomAttribute(typeof(System.ObsoleteAttribute)) != null)
                        continue;

                    int count;
                    if (methodNames.TryGetValue(method.Name, out count))
                        count++;
                    else
                        count = 1;
                    methodNames[method.Name] = count;
                }

                var swapFirstTwoParams = false;
                foreach (var method in methods)
                {
                    if (method.GetCustomAttribute(typeof(System.ObsoleteAttribute)) != null)
                        continue;
                        
                    if (method.DeclaringType != stubType)
                        continue;
                    var parameters = method.GetParameters();
                    int outParamCount = 0;
                    int refParamCount = 0;
                    foreach (var p in parameters)
                    {
                        if (p.IsOut)
                            outParamCount++;
                        else if (p.ParameterType.IsByRef)
                            refParamCount++;
                    }
                    int parameterCount = parameters.Length - outParamCount;

                    if (method.IsSpecialName && (method.Name.StartsWith("get_") || method.Name.StartsWith("set_")))
                    {
                        string propName = method.Name.Substring("get_".Length);
                        if (method.Name.StartsWith("get_"))
                            sb.AppendLine("    @property");
                        else
                        {
                            sb.AppendLine($"    @{propName}.setter");
                        }
                        sb.Append($"    def {propName}(");
                    }
                    else if (method.Name.StartsWith("op_")) {
                        if (methodNames[method.Name] > 1)
                            sb.AppendLine("    @overload");
                        var isRight = (
                            parameters.Length > 1
                            && parameters[0].ParameterType != stubType
                            && parameters[1].ParameterType == stubType
                        );
                        if (isRight)
                            swapFirstTwoParams = true;
                        string propName;
                        if (method.Name == "op_Equality")
                            propName = "__eq__";
                        else if (method.Name == "op_Inequality")
                            propName = "__ne__";
                        else if (method.Name == "op_GreaterThan")
                            propName = "__gt__";
                        else if (method.Name == "op_GreaterThanOrEqual")
                            propName = "__ge__";
                        else if (method.Name == "op_LessThan")
                            propName = "__lt__";
                        else if (method.Name == "op_LessThanOrEqual")
                            propName = "__le__";
                        else if (method.Name == "op_Addition")
                            propName = !isRight ? "__add__" : "__radd__";
                        else if (method.Name == "op_Subtraction")
                            propName = !isRight ? "__sub__" : "__rsub__";
                        else if (method.Name == "op_Multiply")
                            propName = !isRight ? "__mul__" : "__rmul__";
                        else if (method.Name == "op_Division")
                            propName = !isRight ? "__truediv__" : "__rtruediv__";
                        else if (method.Name == "op_IntegerDivision")
                            propName = !isRight ? "__floordiv__" : "__rfloordiv__";
                        else if (method.Name == "op_Modulus")
                            propName = !isRight ? "__mod__" : "__rmod__";
                        else if (method.Name == "op_Exponent")
                            propName = !isRight ? "__pow__" : "__rpow__";
                        else if (method.Name == "op_LeftShift")
                            propName = !isRight ? "__lshift__" : "__rlshift__";
                        else if (method.Name == "op_RightShift")
                            propName = !isRight ? "__rshift__" : "__rrshift__";
                        else if (method.Name == "op_BitwiseAnd")
                            propName = !isRight ? "__and__" : "__rand__";
                        else if (method.Name == "op_BitwiseOr")
                            propName = !isRight ? "__or__" : "__ror__";
                        else if (method.Name == "op_ExclusiveOr")
                            propName = !isRight ? "__xor__" : "__rxor__";
                        else if (method.Name == "op_UnaryNegation")
                            propName = "__neg__";
                        else if (method.Name == "op_UnaryPlus")
                            propName = "__pos__";
                        else if (method.Name == "op_OnesComplement")
                            propName = "__invert__";
                        else if (method.Name == "op_Concatenate")
                            propName = "__add__";
                        else if (method.Name == "op_False" || method.Name == "op_True")
                            propName = "__bool__";
                        else 
                            propName = method.Name;
                        sb.Append($"    def {propName}(");
                    }
                    else
                    {
                        if (methodNames[method.Name] > 1)
                            sb.AppendLine("    @overload");
                        sb.Append($"    def {method.Name}(");
                    }

                    bool addComma = false;
                    if (!method.IsStatic)
                    {
                        sb.Append("self");
                        addComma = true;
                    }
                    for (int i = 0; i < parameters.Length; i++)
                    {
                        if (parameters[i].IsOut)
                            continue;

                        var parameter = parameters[i];
                        if (method.IsStatic && swapFirstTwoParams && i == 0 && parameters.Length > 1)
                            parameter = parameters[1];
                        else if (method.IsStatic && swapFirstTwoParams && i == 1)
                            parameter = parameters[0];

                        if (addComma)
                            sb.Append(", ");

                        sb.Append($"{SafePythonName(parameter.Name)}: {ToPythonType(parameter.ParameterType)}");
                        addComma = true;
                    }
                    sb.Append(")");
                    {
                        List<string> types = new List<string>();
                        if (method.ReturnType == typeof(void))
                        {
                            if (outParamCount == 0 && refParamCount == 0)
                                types.Add("None");
                        }
                        else
                            types.Add(ToPythonType(method.ReturnType));

                        foreach (var p in parameters)
                        {
                            if (p.IsOut || (p.ParameterType.IsByRef))
                            {
                                types.Add(ToPythonType(p.ParameterType));
                            }
                        }

                        sb.Append($" -> ");
                        if (outParamCount == 0 && refParamCount == 0)
                            sb.Append(types[0]);
                        else
                        {
                            sb.Append("Tuple[");
                            for (int i = 0; i < types.Count; i++)
                            {
                                if (i > 0)
                                    sb.Append(", ");
                                sb.Append(types[i]);
                            }
                            sb.Append("]");
                        }
                    }
                    sb.AppendLine(": ...");
                }
                // If no strings appended, class is empty. add "pass"
                if (sb.ToString().Length == classStartString.Length)
                {
                    sb.AppendLine($"    pass");
                }

            }
            File.WriteAllText(path, sb.ToString());
        }

        private static string SafePythonName(string s)
        {
            if (s == "from")
                return "from_";
            else if (s == "class")
                return "class_";
            else if (s == "in")
                return "in_";
            else if (s == "or")
                return "or_";
            return s;
        }

        private static string FindRelativeNamespace(string from, string to)
        {
            // Split the paths into components
            var fromParts = from.Split('.');
            var toParts = to.Split('.');

            // Find the common prefix
            int commonLength = 0;
            int minLength = Math.Min(fromParts.Length, toParts.Length);
            for (int i = 0; i < minLength; i++)
            {
                if (fromParts[i] == toParts[i])
                {
                    commonLength++;
                }
                else
                {
                    break;
                }
            }

            if (commonLength == 0)
                return null;

            // Create the relative path
            var relativePathParts = new List<string>();

            // Add "." for each level up from the 'from' path
            for (int i = commonLength; i < fromParts.Length; i++)
            {
                relativePathParts.Add(".");
            }

            // Add the remaining parts of the 'to' path
            for (int i = commonLength; i < toParts.Length; i++)
            {
                relativePathParts.Add("." + toParts[i]);
            }

            // Join the parts into a single string
            return string.Join("", relativePathParts);
        }

        private static string ToPythonType(string s)
        {
            string rc = s;
            if (rc.EndsWith("&"))
                rc = rc.Substring(0, rc.Length - 1);

            if (rc.Length > 2 && rc[rc.Length - 2] == '`')
                rc = rc.Substring(0, rc.Length - 2);

            if (rc.EndsWith("[]"))
            {
                string partial = ToPythonType(rc.Substring(0, rc.Length - 2));
                return $"Set[{partial}]";
            }

            if (rc.EndsWith("*"))
                return rc.Substring(0, rc.Length - 1); // ? not sure what we can do for pointers

            if (rc.Equals("String"))
                return "str";
            if (rc.Equals("Double"))
                return "float";
            if (rc.Equals("Boolean"))
                return "bool";
            if (rc.Equals("Int32"))
                return "int";

            return rc;
        }

        private static string ToPythonType(Type t)
        {
            if (t.IsGenericType && t.Name.StartsWith("IEnumerable"))
            {
                string rc = ToPythonType(t.GenericTypeArguments[0]);
                return $"Iterable[{rc}]";
            }
            // TODO: Figure out the right way to get at IEnumerable<T>
            if (t.FullName != null && t.FullName.StartsWith("System.Collections.Generic.IEnumerable`1[["))
            {
                string enumerableType = t.FullName.Substring("System.Collections.Generic.IEnumerable`1[[".Length);
                enumerableType = enumerableType.Substring(0, enumerableType.IndexOf(','));
                var pieces = enumerableType.Split('.');
                string rc = ToPythonType(pieces[pieces.Length - 1]);
                return $"Iterable[{rc}]";
            }
            if (t.FullName != null && t.FullName.StartsWith("System.Collections.Generic.IList`1[["))
            {
                string enumerableType = t.FullName.Substring("System.Collections.Generic.IList`1[[".Length);
                enumerableType = enumerableType.Substring(0, enumerableType.IndexOf(','));
                var pieces = enumerableType.Split('.');
                string rc = ToPythonType(pieces[pieces.Length - 1]);
                return $"List[{rc}]";
            }
            return ToPythonType(t.Name);
        }

        static int MethodCompare(MethodBase a, MethodBase b)
        {
            string aSignature = a.Name;
            foreach (var parameter in a.GetParameters())
                aSignature += $"_{parameter.GetType().Name}";
            string bSignature = b.Name;
            foreach (var parameter in b.GetParameters())
                bSignature += $"_{parameter.GetType().Name}";
            return aSignature.CompareTo(bSignature);
        }
    }
}
