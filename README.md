> This is a fork of the original [`mcneel/pythonstubs`](https://github.com/mcneel/pythonstubs) repository. Modifications are focused on improving type hint support.

# Typed McNeel Python Stubs

Typed Python stubs for .NET assemblies that ship with Rhino. Specifically:

- [`rhino-stubs-typed`](https://pypi.org/project/rhino-stubs-typed)
- [`eto-stubs-typed`](https://pypi.org/project/eto-stubs-typed)
- [`grasshopper-stubs-typed`](https://pypi.org/project/grasshopper-stubs-typed)
- [`gh-io-stubs-typed`](https://pypi.org/project/gh-io-stubs-typed)
- [`gh-util-stubs-typed`](https://pypi.org/project/gh-util-stubs-typed)

For more details about the purpose of these packages, see the following posts:

- [Autocomplete while editing Python scripts outside of Rhino](https://discourse.mcneel.com/t/autocomplete-while-editing-python-scripts-outside-of-rhino/79329) on the Rhino forums
- [Autocomplete and Type Hints with Python Scripts for Rhino/Grasshopper](https://stevebaer.wordpress.com/2019/02/25/autocomplete-and-type-hints-with-python-scripts-for-rhino-grasshopper) on Steve Baer's Notes

## Using with [VS Code](https://code.visualstudio.com/)

1. Open your project in VS Code.
2. Open a terminal.
3. Depending on the Python package manager you are using, install the stub packages into your project environment. While using `pip` is possible, we recommend using the [`uv`](https://docs.astral.sh/uv/) package manager.

   ```sh
   pip install rhino-stubs-typed
   ```

4. Now you can import `Rhino` or `Grasshopper` and use the autocomplete feature as well as type prediction.

   ![Stub preview](static/rhino-stub-vscode.gif)
