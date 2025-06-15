from typing import overload, Tuple, Iterable, Iterator, Sequence, MutableSequence
from enum import Enum

import Custom

__all__ = ['Custom']


class BitmapFileTypes(Enum):
    bmp = 1
    jpg = 2
    pcx = 4
    png = 8
    tif = 16
    tga = 32


class GetBoxMode(Enum):
    All = 0
    Corner = 1
    ThreePoint = 2
    Vertical = 3
    Center = 4


class GetResult(Enum):
    NoResult = 0
    Cancel = 1
    Nothing = 2
    Option = 3
    Number = 4
    Color = 5
    Undo = 6
    Miss = 7
    Point = 8
    Point2d = 9
    Line2d = 10
    Rectangle2d = 11
    Object = 12
    String = 13
    CustomMessage = 14
    Timeout = 15
    Circle = 16
    Plane = 17
    Cylinder = 18
    Sphere = 19
    Angle = 20
    Distance = 21
    Direction = 22
    Frame = 23
    ExitRhino = 268435455
    User5 = 4294967291
    User4 = 4294967292
    User3 = 4294967293
    User2 = 4294967294
    User1 = 4294967295


from ..UI import LocalizeStringPair
from ..Geometry import Point3d
from ..Commands import Result
from ..DocObjects import MeshObject
from ..DocObjects import ObjectType
from ..DocObjects import ObjRef
from .Custom import GetObjectGeometryFilter
from ..Geometry import Plane
from ..Display import RhinoView
from ..Geometry import Box
from ..Geometry import MeshingParameters
from ..DocObjects import GripObject
from ..Geometry import NurbsCurve
from ..Geometry import Line
from ..Geometry import Polyline
from ..Geometry import Arc
from ..Geometry import Circle
from ..Geometry import LinearDimension
from .Custom import GetFileNameMode
from ..Display import ViewCaptureSettings
class RhinoGet:
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    @property
    def AllBitmapFileTypes() -> BitmapFileTypes: ...
    @overload
    @staticmethod
    def Get2dRectangle(solidPen: bool) -> Tuple[Result, Rectangle, RhinoView]: ...
    @overload
    @staticmethod
    def GetAngle(commandPrompt: str, basePoint: Point3d, referencePoint: Point3d, defaultAngleRadians: float) -> Tuple[Result, float]: ...
    @overload
    @staticmethod
    def GetArc() -> Tuple[Result, Arc]: ...
    @overload
    @staticmethod
    def GetBool(prompt: str, acceptNothing: bool, offPrompt: str, onPrompt: str, boolValue: bool) -> Tuple[Result, bool]: ...
    @overload
    @staticmethod
    def GetBox() -> Tuple[Result, Box]: ...
    @overload
    @staticmethod
    def GetBox(mode: GetBoxMode, basePoint: Point3d, prompt1: str, prompt2: str, prompt3: str) -> Tuple[Result, Box]: ...
    @overload
    @staticmethod
    def GetBoxWithCounts(xMin: int, xCount: int, yMin: int, yCount: int, zMin: int, zCount: int) -> Tuple[Result, int, int, int, Iterable[Point3d]]: ...
    @overload
    @staticmethod
    def GetCircle() -> Tuple[Result, Circle]: ...
    @overload
    @staticmethod
    def GetColor(prompt: str, acceptNothing: bool, color: Color) -> Tuple[Result, Color]: ...
    @overload
    @staticmethod
    def GetFileName(mode: GetFileNameMode, defaultName: str, title: str, parent: object) -> str: ...
    @overload
    @staticmethod
    def GetFileName(mode: GetFileNameMode, defaultName: str, title: str, parent: object, fileTypes: BitmapFileTypes) -> str: ...
    @overload
    @staticmethod
    def GetFileNameScripted(mode: GetFileNameMode, defaultName: str) -> str: ...
    @overload
    @staticmethod
    def GetGrip(prompt: str) -> Tuple[Result, GripObject]: ...
    @overload
    @staticmethod
    def GetGrips(prompt: str) -> Tuple[Result, Iterable[GripObject]]: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    @staticmethod
    def GetHelix() -> Tuple[Result, NurbsCurve]: ...
    @overload
    @staticmethod
    def GetInteger(prompt: str, acceptNothing: bool, outputNumber: int) -> Tuple[Result, int]: ...
    @overload
    @staticmethod
    def GetInteger(prompt: str, acceptNothing: bool, outputNumber: int, lowerLimit: int, upperLimit: int) -> Tuple[Result, int]: ...
    @overload
    @staticmethod
    def GetLine() -> Tuple[Result, Line]: ...
    @overload
    @staticmethod
    def GetLinearDimension() -> Tuple[Result, LinearDimension]: ...
    @overload
    @staticmethod
    def GetMeshParameters(doc: RhinoDoc, parameters: MeshingParameters, uiStyle: int) -> Tuple[Result, MeshingParameters, int]: ...
    @overload
    @staticmethod
    def GetMultipleObjects(prompt: str, acceptNothing: bool, filter: ObjectType) -> Tuple[Result, Iterable[ObjRef]]: ...
    @overload
    @staticmethod
    def GetMultipleObjects(prompt: str, acceptNothing: bool, filter: GetObjectGeometryFilter) -> Tuple[Result, Iterable[ObjRef]]: ...
    @overload
    @staticmethod
    def GetNumber(prompt: str, acceptNothing: bool, outputNumber: float) -> Tuple[Result, float]: ...
    @overload
    @staticmethod
    def GetNumber(prompt: str, acceptNothing: bool, outputNumber: float, lowerLimit: float, upperLimit: float) -> Tuple[Result, float]: ...
    @overload
    @staticmethod
    def GetOneObject(prompt: str, acceptNothing: bool, filter: ObjectType) -> Tuple[Result, ObjRef]: ...
    @overload
    @staticmethod
    def GetOneObject(prompt: str, acceptNothing: bool, filter: GetObjectGeometryFilter) -> Tuple[Result, ObjRef]: ...
    @overload
    @staticmethod
    def GetPlane() -> Tuple[Result, Plane]: ...
    @overload
    @staticmethod
    def GetPoint(prompt: str, acceptNothing: bool) -> Tuple[Result, Point3d]: ...
    @overload
    @staticmethod
    def GetPointOnMesh(doc: RhinoDoc, meshObjectId: Guid, prompt: str, acceptNothing: bool) -> Tuple[Result, Point3d]: ...
    @overload
    @staticmethod
    def GetPointOnMesh(doc: RhinoDoc, meshObject: MeshObject, prompt: str, acceptNothing: bool) -> Tuple[Result, Point3d]: ...
    @overload
    @staticmethod
    def GetPolygon(numberSides: int, inscribed: bool) -> Tuple[Result, int, bool, Polyline]: ...
    @overload
    @staticmethod
    def GetPolygon(useActiveLayerLinetype: bool, numberSides: int, inscribed: bool) -> Tuple[Result, int, bool, Polyline]: ...
    @overload
    @staticmethod
    def GetPolyline() -> Tuple[Result, Polyline]: ...
    @overload
    @staticmethod
    def GetPrintWindow(settings: ViewCaptureSettings) -> Tuple[Result, ViewCaptureSettings]: ...
    @overload
    @staticmethod
    def GetRectangle() -> Tuple[Result, Iterable[Point3d]]: ...
    @overload
    @staticmethod
    def GetRectangle(firstPrompt: str) -> Tuple[Result, Iterable[Point3d]]: ...
    @overload
    @staticmethod
    def GetRectangle(mode: GetBoxMode, firstPoint: Point3d, prompts: Iterable[str]) -> Tuple[Result, Iterable[Point3d]]: ...
    @overload
    @staticmethod
    def GetRectangleWithCounts(xMin: int, xCount: int, yMin: int, yCount: int) -> Tuple[Result, int, int, Iterable[Point3d]]: ...
    @overload
    @staticmethod
    def GetSpiral() -> Tuple[Result, NurbsCurve]: ...
    @overload
    @staticmethod
    def GetString(prompt: str, acceptNothing: bool, outputString: str) -> Tuple[Result, str]: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    @staticmethod
    def GetView(commandPrompt: str) -> Tuple[Result, RhinoView]: ...
    @overload
    @staticmethod
    def InGet(doc: RhinoDoc) -> bool: ...
    @overload
    @staticmethod
    def InGetObject(doc: RhinoDoc) -> bool: ...
    @overload
    @staticmethod
    def InGetPoint(doc: RhinoDoc) -> bool: ...
    @overload
    @staticmethod
    def StringToCommandOptionName(stringToConvert: str) -> str: ...
    @overload
    @staticmethod
    def StringToCommandOptionName(englishString: str, localizedString: str) -> LocalizeStringPair: ...
    @overload
    def ToString(self) -> str: ...


class StringParser:
    @overload
    def __init__(self): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    @staticmethod
    def ParseAngleExpession(expression: str, start_offset: int, expression_length: int, parse_settings_in: StringParserSettings, output_angle_unit_system: AngleUnitSystem, parse_results: StringParserSettings, parsed_unit_system: AngleUnitSystem) -> Tuple[int, float, StringParserSettings, AngleUnitSystem]: ...
    @overload
    @staticmethod
    def ParseAngleExpressionDegrees(expression: str) -> Tuple[bool, float]: ...
    @overload
    @staticmethod
    def ParseAngleExpressionRadians(expression: str) -> Tuple[bool, float]: ...
    @overload
    @staticmethod
    def ParseLengthExpession(expression: str, parse_settings_in: StringParserSettings, output_unit_system: UnitSystem) -> Tuple[int, float]: ...
    @overload
    @staticmethod
    def ParseLengthExpession(expression: str, start_offset: int, expression_length: int, parse_settings_in: StringParserSettings, output_unit_system: UnitSystem, parse_results: StringParserSettings, parsed_unit_system: UnitSystem) -> Tuple[int, float, StringParserSettings, UnitSystem]: ...
    @overload
    @staticmethod
    def ParseNumber(expression: str, max_count: int, settings_in: StringParserSettings, settings_out: StringParserSettings) -> Tuple[int, StringParserSettings, float]: ...
    @overload
    def ToString(self) -> str: ...


class StringParserSettings:
    @overload
    def __init__(self): ...
    @overload
    def Dispose(self) -> None: ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    @property
    def DefaultAngleUnitSystem(self) -> AngleUnitSystem: ...
    @overload
    @property
    def DefaultLengthUnitSystem(self) -> UnitSystem: ...
    @overload
    @property
    def DefaultParseSettings() -> StringParserSettings: ...
    @overload
    @property
    def ParseAddition(self) -> bool: ...
    @overload
    @property
    def ParseArcDegreesMinutesSeconds(self) -> bool: ...
    @overload
    @property
    def ParseArithmeticExpression(self) -> bool: ...
    @overload
    @property
    def ParseCommaAsDecimalPoint(self) -> bool: ...
    @overload
    @property
    def ParseCommaAsDigitSeparator(self) -> bool: ...
    @overload
    @property
    def ParseDAsExponentInScientificENotation(self) -> bool: ...
    @overload
    @property
    def ParseDivision(self) -> bool: ...
    @overload
    @property
    def ParseExplicitFormulaExpression(self) -> bool: ...
    @overload
    @property
    def ParseFeetInches(self) -> bool: ...
    @overload
    @property
    def ParseFullStopAsDecimalPoint(self) -> bool: ...
    @overload
    @property
    def ParseFullStopAsDigitSeparator(self) -> bool: ...
    @overload
    @property
    def ParseHyphenAsNumberDash(self) -> bool: ...
    @overload
    @property
    def ParseHyphenMinusAsNumberDash(self) -> bool: ...
    @overload
    @property
    def ParseIntegerDashFraction(self) -> bool: ...
    @overload
    @property
    def ParseLeadingWhiteSpace(self) -> bool: ...
    @overload
    @property
    def ParseMathFunctions(self) -> bool: ...
    @overload
    @property
    def ParseMultiplication(self) -> bool: ...
    @overload
    @property
    def ParsePairedParentheses(self) -> bool: ...
    @overload
    @property
    def ParsePi(self) -> bool: ...
    @overload
    @property
    def ParseRationalNumber(self) -> bool: ...
    @overload
    @property
    def ParseScientificENotation(self) -> bool: ...
    @overload
    @property
    def ParseSettingsDegrees() -> StringParserSettings: ...
    @overload
    @property
    def ParseSettingsDoubleNumber() -> StringParserSettings: ...
    @overload
    @property
    def ParseSettingsEmpty() -> StringParserSettings: ...
    @overload
    @property
    def ParseSettingsIntegerNumber() -> StringParserSettings: ...
    @overload
    @property
    def ParseSettingsRadians() -> StringParserSettings: ...
    @overload
    @property
    def ParseSettingsRationalNumber() -> StringParserSettings: ...
    @overload
    @property
    def ParseSettingsRealNumber() -> StringParserSettings: ...
    @overload
    @property
    def ParseSignificandDigitSeparators(self) -> bool: ...
    @overload
    @property
    def ParseSignificandFractionalPart(self) -> bool: ...
    @overload
    @property
    def ParseSignificandIntegerPart(self) -> bool: ...
    @overload
    @property
    def ParseSpaceAsDigitSeparator(self) -> bool: ...
    @overload
    @property
    def ParseSubtraction(self) -> bool: ...
    @overload
    @property
    def ParseSurveyorsNotation(self) -> bool: ...
    @overload
    @property
    def ParseUnaryMinus(self) -> bool: ...
    @overload
    @property
    def ParseUnaryPlus(self) -> bool: ...
    @overload
    @property
    def PreferedLocaleId(self) -> int: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    @DefaultAngleUnitSystem.setter
    def DefaultAngleUnitSystem(self, value: AngleUnitSystem) -> None: ...
    @overload
    @DefaultLengthUnitSystem.setter
    def DefaultLengthUnitSystem(self, value: UnitSystem) -> None: ...
    @overload
    @ParseAddition.setter
    def ParseAddition(self, value: bool) -> None: ...
    @overload
    @ParseArcDegreesMinutesSeconds.setter
    def ParseArcDegreesMinutesSeconds(self, value: bool) -> None: ...
    @overload
    @ParseArithmeticExpression.setter
    def ParseArithmeticExpression(self, value: bool) -> None: ...
    @overload
    @ParseCommaAsDecimalPoint.setter
    def ParseCommaAsDecimalPoint(self, value: bool) -> None: ...
    @overload
    @ParseCommaAsDigitSeparator.setter
    def ParseCommaAsDigitSeparator(self, value: bool) -> None: ...
    @overload
    @ParseDAsExponentInScientificENotation.setter
    def ParseDAsExponentInScientificENotation(self, value: bool) -> None: ...
    @overload
    @ParseDivision.setter
    def ParseDivision(self, value: bool) -> None: ...
    @overload
    @ParseExplicitFormulaExpression.setter
    def ParseExplicitFormulaExpression(self, value: bool) -> None: ...
    @overload
    @ParseFeetInches.setter
    def ParseFeetInches(self, value: bool) -> None: ...
    @overload
    @ParseFullStopAsDecimalPoint.setter
    def ParseFullStopAsDecimalPoint(self, value: bool) -> None: ...
    @overload
    @ParseFullStopAsDigitSeparator.setter
    def ParseFullStopAsDigitSeparator(self, value: bool) -> None: ...
    @overload
    @ParseHyphenAsNumberDash.setter
    def ParseHyphenAsNumberDash(self, value: bool) -> None: ...
    @overload
    @ParseHyphenMinusAsNumberDash.setter
    def ParseHyphenMinusAsNumberDash(self, value: bool) -> None: ...
    @overload
    @ParseIntegerDashFraction.setter
    def ParseIntegerDashFraction(self, value: bool) -> None: ...
    @overload
    @ParseLeadingWhiteSpace.setter
    def ParseLeadingWhiteSpace(self, value: bool) -> None: ...
    @overload
    @ParseMathFunctions.setter
    def ParseMathFunctions(self, value: bool) -> None: ...
    @overload
    @ParseMultiplication.setter
    def ParseMultiplication(self, value: bool) -> None: ...
    @overload
    @ParsePairedParentheses.setter
    def ParsePairedParentheses(self, value: bool) -> None: ...
    @overload
    @ParsePi.setter
    def ParsePi(self, value: bool) -> None: ...
    @overload
    @ParseRationalNumber.setter
    def ParseRationalNumber(self, value: bool) -> None: ...
    @overload
    @ParseScientificENotation.setter
    def ParseScientificENotation(self, value: bool) -> None: ...
    @overload
    @ParseSignificandDigitSeparators.setter
    def ParseSignificandDigitSeparators(self, value: bool) -> None: ...
    @overload
    @ParseSignificandFractionalPart.setter
    def ParseSignificandFractionalPart(self, value: bool) -> None: ...
    @overload
    @ParseSignificandIntegerPart.setter
    def ParseSignificandIntegerPart(self, value: bool) -> None: ...
    @overload
    @ParseSpaceAsDigitSeparator.setter
    def ParseSpaceAsDigitSeparator(self, value: bool) -> None: ...
    @overload
    @ParseSubtraction.setter
    def ParseSubtraction(self, value: bool) -> None: ...
    @overload
    @ParseSurveyorsNotation.setter
    def ParseSurveyorsNotation(self, value: bool) -> None: ...
    @overload
    @ParseUnaryMinus.setter
    def ParseUnaryMinus(self, value: bool) -> None: ...
    @overload
    @ParseUnaryPlus.setter
    def ParseUnaryPlus(self, value: bool) -> None: ...
    @overload
    @PreferedLocaleId.setter
    def PreferedLocaleId(self, value: int) -> None: ...
    @overload
    def SetAllExpressionSettingsToFalse(self) -> None: ...
    @overload
    def SetAllFieldsToFalse(self) -> None: ...
    @overload
    def ToString(self) -> str: ...
