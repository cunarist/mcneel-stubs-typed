from typing import overload, Tuple, Iterable, Iterator, Sequence, MutableSequence
from enum import Enum



class AppearanceSettings:
    @overload
    @staticmethod
    def DefaultPaintColor(whichColor: PaintColor) -> Color: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def CommandPromptBackgroundColor() -> Color: ...
    @overload
    @property
    def CommandPromptFontSize() -> int: ...
    @overload
    @property
    def CommandPromptHypertextColor() -> Color: ...
    @overload
    @property
    def CommandPromptPosition() -> CommandPromptPosition: ...
    @overload
    @property
    def CommandPromptTextColor() -> Color: ...
    @overload
    @property
    def CrosshairColor() -> Color: ...
    @overload
    @property
    def CurrentLayerBackgroundColor() -> Color: ...
    @overload
    @property
    def DefaultFontFaceName() -> str: ...
    @overload
    @property
    def DefaultLayerColor() -> Color: ...
    @overload
    @property
    def DefaultObjectColor() -> Color: ...
    @overload
    @property
    def EchoCommandsToHistoryWindow() -> bool: ...
    @overload
    @property
    def EchoPromptsToHistoryWindow() -> bool: ...
    @overload
    @property
    def EditCandidateColor() -> Color: ...
    @overload
    @property
    def FeedbackColor() -> Color: ...
    @overload
    @property
    def FrameBackgroundColor() -> Color: ...
    @overload
    @property
    def GridThickLineColor() -> Color: ...
    @overload
    @property
    def GridThinLineColor() -> Color: ...
    @overload
    @property
    def GridXAxisLineColor() -> Color: ...
    @overload
    @property
    def GridYAxisLineColor() -> Color: ...
    @overload
    @property
    def GridZAxisLineColor() -> Color: ...
    @overload
    @property
    def LanguageIdentifier() -> int: ...
    @overload
    @property
    def LockedObjectColor() -> Color: ...
    @overload
    @property
    def MenuVisible() -> bool: ...
    @overload
    @property
    def PageviewPaperColor() -> Color: ...
    @overload
    @property
    def PreviousLanguageIdentifier() -> int: ...
    @overload
    @property
    def SelectedObjectColor() -> Color: ...
    @overload
    @property
    def SelectionWindowCrossingFillColor() -> Color: ...
    @overload
    @property
    def SelectionWindowCrossingStrokeColor() -> Color: ...
    @overload
    @property
    def SelectionWindowFillColor() -> Color: ...
    @overload
    @property
    def SelectionWindowStrokeColor() -> Color: ...
    @overload
    @property
    def ShowCrosshairs() -> bool: ...
    @overload
    @property
    def ShowFullPathInTitleBar() -> bool: ...
    @overload
    @property
    def ShowOsnapBar() -> bool: ...
    @overload
    @property
    def ShowSideBar() -> bool: ...
    @overload
    @property
    def ShowStatusBar() -> bool: ...
    @overload
    @property
    def TrackingColor() -> Color: ...
    @overload
    @property
    def UsePaintColors() -> bool: ...
    @overload
    @property
    def ViewportBackgroundColor() -> Color: ...
    @overload
    @property
    def WorldCoordIconXAxisColor() -> Color: ...
    @overload
    @property
    def WorldCoordIconYAxisColor() -> Color: ...
    @overload
    @property
    def WorldCoordIconZAxisColor() -> Color: ...
    @overload
    @staticmethod
    def GetCurrentState() -> AppearanceSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> AppearanceSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    @staticmethod
    def GetPaintColor(whichColor: PaintColor) -> Color: ...
    @overload
    @staticmethod
    def GetPaintColor(whichColor: PaintColor, compute: bool) -> Color: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def GetWidgetColor(whichColor: WidgetColor) -> Color: ...
    @overload
    @staticmethod
    def InitialMainWindowPosition() -> Tuple[bool, Rectangle]: ...
    @overload
    @staticmethod
    def RestoreDefaults() -> None: ...
    @overload
    @CommandPromptBackgroundColor.setter
    def CommandPromptBackgroundColor() -> None: ...
    @overload
    @CommandPromptFontSize.setter
    def CommandPromptFontSize() -> None: ...
    @overload
    @CommandPromptHypertextColor.setter
    def CommandPromptHypertextColor() -> None: ...
    @overload
    @CommandPromptPosition.setter
    def CommandPromptPosition() -> None: ...
    @overload
    @CommandPromptTextColor.setter
    def CommandPromptTextColor() -> None: ...
    @overload
    @CrosshairColor.setter
    def CrosshairColor() -> None: ...
    @overload
    @CurrentLayerBackgroundColor.setter
    def CurrentLayerBackgroundColor() -> None: ...
    @overload
    @DefaultLayerColor.setter
    def DefaultLayerColor() -> None: ...
    @overload
    @DefaultObjectColor.setter
    def DefaultObjectColor() -> None: ...
    @overload
    @EchoCommandsToHistoryWindow.setter
    def EchoCommandsToHistoryWindow() -> None: ...
    @overload
    @EchoPromptsToHistoryWindow.setter
    def EchoPromptsToHistoryWindow() -> None: ...
    @overload
    @EditCandidateColor.setter
    def EditCandidateColor() -> None: ...
    @overload
    @FeedbackColor.setter
    def FeedbackColor() -> None: ...
    @overload
    @FrameBackgroundColor.setter
    def FrameBackgroundColor() -> None: ...
    @overload
    @GridThickLineColor.setter
    def GridThickLineColor() -> None: ...
    @overload
    @GridThinLineColor.setter
    def GridThinLineColor() -> None: ...
    @overload
    @GridXAxisLineColor.setter
    def GridXAxisLineColor() -> None: ...
    @overload
    @GridYAxisLineColor.setter
    def GridYAxisLineColor() -> None: ...
    @overload
    @GridZAxisLineColor.setter
    def GridZAxisLineColor() -> None: ...
    @overload
    @LanguageIdentifier.setter
    def LanguageIdentifier() -> None: ...
    @overload
    @LockedObjectColor.setter
    def LockedObjectColor() -> None: ...
    @overload
    @MenuVisible.setter
    def MenuVisible() -> None: ...
    @overload
    @PageviewPaperColor.setter
    def PageviewPaperColor() -> None: ...
    @overload
    @PreviousLanguageIdentifier.setter
    def PreviousLanguageIdentifier() -> None: ...
    @overload
    @SelectedObjectColor.setter
    def SelectedObjectColor() -> None: ...
    @overload
    @SelectionWindowCrossingFillColor.setter
    def SelectionWindowCrossingFillColor() -> None: ...
    @overload
    @SelectionWindowCrossingStrokeColor.setter
    def SelectionWindowCrossingStrokeColor() -> None: ...
    @overload
    @SelectionWindowFillColor.setter
    def SelectionWindowFillColor() -> None: ...
    @overload
    @SelectionWindowStrokeColor.setter
    def SelectionWindowStrokeColor() -> None: ...
    @overload
    @ShowCrosshairs.setter
    def ShowCrosshairs() -> None: ...
    @overload
    @ShowFullPathInTitleBar.setter
    def ShowFullPathInTitleBar() -> None: ...
    @overload
    @ShowOsnapBar.setter
    def ShowOsnapBar() -> None: ...
    @overload
    @ShowSideBar.setter
    def ShowSideBar() -> None: ...
    @overload
    @ShowStatusBar.setter
    def ShowStatusBar() -> None: ...
    @overload
    @TrackingColor.setter
    def TrackingColor() -> None: ...
    @overload
    @ViewportBackgroundColor.setter
    def ViewportBackgroundColor() -> None: ...
    @overload
    @WorldCoordIconXAxisColor.setter
    def WorldCoordIconXAxisColor() -> None: ...
    @overload
    @WorldCoordIconYAxisColor.setter
    def WorldCoordIconYAxisColor() -> None: ...
    @overload
    @WorldCoordIconZAxisColor.setter
    def WorldCoordIconZAxisColor() -> None: ...
    @overload
    @staticmethod
    def SetPaintColor(whichColor: PaintColor, c: Color) -> None: ...
    @overload
    @staticmethod
    def SetPaintColor(whichColor: PaintColor, c: Color, forceUiUpdate: bool) -> None: ...
    @overload
    @staticmethod
    def SetWidgetColor(whichColor: WidgetColor, c: Color) -> None: ...
    @overload
    @staticmethod
    def SetWidgetColor(whichColor: WidgetColor, c: Color, forceUiUpdate: bool) -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def UpdateFromState(state: AppearanceSettingsState) -> None: ...


class AppearanceSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def CommandPromptBackgroundColor(self) -> Color: ...
    @overload
    @property
    def CommandPromptFontSize(self) -> int: ...
    @overload
    @property
    def CommandPromptHypertextColor(self) -> Color: ...
    @overload
    @property
    def CommandPromptTextColor(self) -> Color: ...
    @overload
    @property
    def CrosshairColor(self) -> Color: ...
    @overload
    @property
    def CurrentLayerBackgroundColor(self) -> Color: ...
    @overload
    @property
    def DefaultFontFaceName(self) -> str: ...
    @overload
    @property
    def DefaultLayerColor(self) -> Color: ...
    @overload
    @property
    def DefaultObjectColor(self) -> Color: ...
    @overload
    @property
    def EchoCommandsToHistoryWindow(self) -> bool: ...
    @overload
    @property
    def EchoPromptsToHistoryWindow(self) -> bool: ...
    @overload
    @property
    def EditCandidateColor(self) -> Color: ...
    @overload
    @property
    def FeedbackColor(self) -> Color: ...
    @overload
    @property
    def FrameBackgroundColor(self) -> Color: ...
    @overload
    @property
    def GridThickLineColor(self) -> Color: ...
    @overload
    @property
    def GridThinLineColor(self) -> Color: ...
    @overload
    @property
    def GridXAxisLineColor(self) -> Color: ...
    @overload
    @property
    def GridYAxisLineColor(self) -> Color: ...
    @overload
    @property
    def GridZAxisLineColor(self) -> Color: ...
    @overload
    @property
    def LockedObjectColor(self) -> Color: ...
    @overload
    @property
    def PageviewPaperColor(self) -> Color: ...
    @overload
    @property
    def SelectedObjectColor(self) -> Color: ...
    @overload
    @property
    def SelectionWindowCrossingFillColor(self) -> Color: ...
    @overload
    @property
    def SelectionWindowCrossingStrokeColor(self) -> Color: ...
    @overload
    @property
    def SelectionWindowFillColor(self) -> Color: ...
    @overload
    @property
    def SelectionWindowStrokeColor(self) -> Color: ...
    @overload
    @property
    def ShowCrosshairs(self) -> bool: ...
    @overload
    @property
    def ShowFullPathInTitleBar(self) -> bool: ...
    @overload
    @property
    def TrackingColor(self) -> Color: ...
    @overload
    @property
    def ViewportBackgroundColor(self) -> Color: ...
    @overload
    @property
    def WorldCoordIconXAxisColor(self) -> Color: ...
    @overload
    @property
    def WorldCoordIconYAxisColor(self) -> Color: ...
    @overload
    @property
    def WorldCoordIconZAxisColor(self) -> Color: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @CommandPromptBackgroundColor.setter
    def CommandPromptBackgroundColor(self) -> MutableSequence[Color]: ...
    @overload
    @CommandPromptFontSize.setter
    def CommandPromptFontSize(self) -> MutableSequence[int]: ...
    @overload
    @CommandPromptHypertextColor.setter
    def CommandPromptHypertextColor(self) -> MutableSequence[Color]: ...
    @overload
    @CommandPromptTextColor.setter
    def CommandPromptTextColor(self) -> MutableSequence[Color]: ...
    @overload
    @CrosshairColor.setter
    def CrosshairColor(self) -> MutableSequence[Color]: ...
    @overload
    @CurrentLayerBackgroundColor.setter
    def CurrentLayerBackgroundColor(self) -> MutableSequence[Color]: ...
    @overload
    @DefaultFontFaceName.setter
    def DefaultFontFaceName(self) -> MutableSequence[str]: ...
    @overload
    @DefaultLayerColor.setter
    def DefaultLayerColor(self) -> MutableSequence[Color]: ...
    @overload
    @DefaultObjectColor.setter
    def DefaultObjectColor(self) -> MutableSequence[Color]: ...
    @overload
    @EchoCommandsToHistoryWindow.setter
    def EchoCommandsToHistoryWindow(self) -> MutableSequence[bool]: ...
    @overload
    @EchoPromptsToHistoryWindow.setter
    def EchoPromptsToHistoryWindow(self) -> MutableSequence[bool]: ...
    @overload
    @EditCandidateColor.setter
    def EditCandidateColor(self) -> MutableSequence[Color]: ...
    @overload
    @FeedbackColor.setter
    def FeedbackColor(self) -> MutableSequence[Color]: ...
    @overload
    @FrameBackgroundColor.setter
    def FrameBackgroundColor(self) -> MutableSequence[Color]: ...
    @overload
    @GridThickLineColor.setter
    def GridThickLineColor(self) -> MutableSequence[Color]: ...
    @overload
    @GridThinLineColor.setter
    def GridThinLineColor(self) -> MutableSequence[Color]: ...
    @overload
    @GridXAxisLineColor.setter
    def GridXAxisLineColor(self) -> MutableSequence[Color]: ...
    @overload
    @GridYAxisLineColor.setter
    def GridYAxisLineColor(self) -> MutableSequence[Color]: ...
    @overload
    @GridZAxisLineColor.setter
    def GridZAxisLineColor(self) -> MutableSequence[Color]: ...
    @overload
    @LockedObjectColor.setter
    def LockedObjectColor(self) -> MutableSequence[Color]: ...
    @overload
    @PageviewPaperColor.setter
    def PageviewPaperColor(self) -> MutableSequence[Color]: ...
    @overload
    @SelectedObjectColor.setter
    def SelectedObjectColor(self) -> MutableSequence[Color]: ...
    @overload
    @SelectionWindowCrossingFillColor.setter
    def SelectionWindowCrossingFillColor(self) -> MutableSequence[Color]: ...
    @overload
    @SelectionWindowCrossingStrokeColor.setter
    def SelectionWindowCrossingStrokeColor(self) -> MutableSequence[Color]: ...
    @overload
    @SelectionWindowFillColor.setter
    def SelectionWindowFillColor(self) -> MutableSequence[Color]: ...
    @overload
    @SelectionWindowStrokeColor.setter
    def SelectionWindowStrokeColor(self) -> MutableSequence[Color]: ...
    @overload
    @ShowCrosshairs.setter
    def ShowCrosshairs(self) -> MutableSequence[bool]: ...
    @overload
    @ShowFullPathInTitleBar.setter
    def ShowFullPathInTitleBar(self) -> MutableSequence[bool]: ...
    @overload
    @TrackingColor.setter
    def TrackingColor(self) -> MutableSequence[Color]: ...
    @overload
    @ViewportBackgroundColor.setter
    def ViewportBackgroundColor(self) -> MutableSequence[Color]: ...
    @overload
    @WorldCoordIconXAxisColor.setter
    def WorldCoordIconXAxisColor(self) -> MutableSequence[Color]: ...
    @overload
    @WorldCoordIconYAxisColor.setter
    def WorldCoordIconYAxisColor(self) -> MutableSequence[Color]: ...
    @overload
    @WorldCoordIconZAxisColor.setter
    def WorldCoordIconZAxisColor(self) -> MutableSequence[Color]: ...
    @overload
    def ToString(self) -> str: ...


class ClipboardState(Enum):
    KeepData = 0
    DeleteData = 1
    PromptWhenBig = 2


class CommandAliasList:
    @overload
    @staticmethod
    def Add(alias: str, macro: str) -> bool: ...
    @overload
    @staticmethod
    def Clear() -> None: ...
    @overload
    @staticmethod
    def Delete(alias: str) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def Count() -> int: ...
    @overload
    @staticmethod
    def GetDefaults() -> Dictionary: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    @staticmethod
    def GetMacro(alias: str) -> str: ...
    @overload
    @staticmethod
    def GetNames() -> Iterable[str]: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def IsAlias(alias: str) -> bool: ...
    @overload
    @staticmethod
    def IsDefault() -> bool: ...
    @overload
    @staticmethod
    def SetMacro(alias: str, macro: str) -> bool: ...
    @overload
    @staticmethod
    def ToDictionary() -> Dictionary: ...
    @overload
    def ToString(self) -> str: ...


class CommandPromptPosition(Enum):
    Top = 0
    Bottom = 1
    Floating = 2
    Hidden = 3


class CursorMode(Enum):
    # None = 0
    BlackOnWhite = 1
    WhiteOnBlack = 2


class CursorTooltipSettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AutoSuppress() -> bool: ...
    @overload
    @property
    def BackgroundColor() -> Color: ...
    @overload
    @property
    def CommandPromptPane() -> bool: ...
    @overload
    @property
    def DistancePane() -> bool: ...
    @overload
    @property
    def Offset() -> Point: ...
    @overload
    @property
    def OsnapPane() -> bool: ...
    @overload
    @property
    def PointPane() -> bool: ...
    @overload
    @property
    def RelativePointPane() -> bool: ...
    @overload
    @property
    def TextColor() -> Color: ...
    @overload
    @property
    def TooltipsEnabled() -> bool: ...
    @overload
    @staticmethod
    def GetCurrentState() -> CursorTooltipSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> CursorTooltipSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @AutoSuppress.setter
    def AutoSuppress() -> None: ...
    @overload
    @BackgroundColor.setter
    def BackgroundColor() -> None: ...
    @overload
    @CommandPromptPane.setter
    def CommandPromptPane() -> None: ...
    @overload
    @DistancePane.setter
    def DistancePane() -> None: ...
    @overload
    @Offset.setter
    def Offset() -> None: ...
    @overload
    @OsnapPane.setter
    def OsnapPane() -> None: ...
    @overload
    @PointPane.setter
    def PointPane() -> None: ...
    @overload
    @RelativePointPane.setter
    def RelativePointPane() -> None: ...
    @overload
    @TextColor.setter
    def TextColor() -> None: ...
    @overload
    @TooltipsEnabled.setter
    def TooltipsEnabled() -> None: ...
    @overload
    def ToString(self) -> str: ...


class CursorTooltipSettingsState:
    @overload
    def __init__(self): ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AutoSuppress(self) -> bool: ...
    @overload
    @property
    def BackgroundColor(self) -> Color: ...
    @overload
    @property
    def CommandPromptPane(self) -> bool: ...
    @overload
    @property
    def DistancePane(self) -> bool: ...
    @overload
    @property
    def Offset(self) -> Point: ...
    @overload
    @property
    def OsnapPane(self) -> bool: ...
    @overload
    @property
    def PointPane(self) -> bool: ...
    @overload
    @property
    def RelativePointPane(self) -> bool: ...
    @overload
    @property
    def TextColor(self) -> Color: ...
    @overload
    @property
    def TooltipsEnabled(self) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @AutoSuppress.setter
    def AutoSuppress(self) -> MutableSequence[bool]: ...
    @overload
    @BackgroundColor.setter
    def BackgroundColor(self) -> MutableSequence[Color]: ...
    @overload
    @CommandPromptPane.setter
    def CommandPromptPane(self) -> MutableSequence[bool]: ...
    @overload
    @DistancePane.setter
    def DistancePane(self) -> MutableSequence[bool]: ...
    @overload
    @Offset.setter
    def Offset(self) -> MutableSequence[Point]: ...
    @overload
    @OsnapPane.setter
    def OsnapPane(self) -> MutableSequence[bool]: ...
    @overload
    @PointPane.setter
    def PointPane(self) -> MutableSequence[bool]: ...
    @overload
    @RelativePointPane.setter
    def RelativePointPane(self) -> MutableSequence[bool]: ...
    @overload
    @TextColor.setter
    def TextColor(self) -> MutableSequence[Color]: ...
    @overload
    @TooltipsEnabled.setter
    def TooltipsEnabled(self) -> MutableSequence[bool]: ...
    @overload
    def ToString(self) -> str: ...


from ..Geometry import Interval
class CurvatureAnalysisSettings:
    @overload
    @staticmethod
    def CalculateCurvatureAutoRange(meshes: Iterable[Mesh], settings: CurvatureAnalysisSettingsState) -> Tuple[bool, CurvatureAnalysisSettingsState]: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def GaussRange() -> Interval: ...
    @overload
    @property
    def MaxRadiusRange() -> Interval: ...
    @overload
    @property
    def MeanRange() -> Interval: ...
    @overload
    @property
    def MinRadiusRange() -> Interval: ...
    @overload
    @property
    def Style() -> CurvatureStyle: ...
    @overload
    @staticmethod
    def GetCurrentState() -> CurvatureAnalysisSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> CurvatureAnalysisSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def RestoreDefaults() -> None: ...
    @overload
    @GaussRange.setter
    def GaussRange() -> None: ...
    @overload
    @MaxRadiusRange.setter
    def MaxRadiusRange() -> None: ...
    @overload
    @MeanRange.setter
    def MeanRange() -> None: ...
    @overload
    @MinRadiusRange.setter
    def MinRadiusRange() -> None: ...
    @overload
    @Style.setter
    def Style() -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def UpdateFromState(state: CurvatureAnalysisSettingsState) -> None: ...


from ..Geometry import Interval
class CurvatureAnalysisSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def GaussRange(self) -> Interval: ...
    @overload
    @property
    def MaxRadiusRange(self) -> Interval: ...
    @overload
    @property
    def MeanRange(self) -> Interval: ...
    @overload
    @property
    def MinRadiusRange(self) -> Interval: ...
    @overload
    @property
    def Style(self) -> CurvatureStyle: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @GaussRange.setter
    def GaussRange(self) -> MutableSequence[Interval]: ...
    @overload
    @MaxRadiusRange.setter
    def MaxRadiusRange(self) -> MutableSequence[Interval]: ...
    @overload
    @MeanRange.setter
    def MeanRange(self) -> MutableSequence[Interval]: ...
    @overload
    @MinRadiusRange.setter
    def MinRadiusRange(self) -> MutableSequence[Interval]: ...
    @overload
    @Style.setter
    def Style(self) -> MutableSequence[CurvatureStyle]: ...
    @overload
    def ToString(self) -> str: ...


class CurvatureStyle(Enum):
    Gaussian = 0
    Mean = 1
    MinRadius = 2
    MaxRadius = 3


from ..Geometry import Interval
from ..Geometry import Vector3d
class DraftAngleAnalysisSettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AngleRange() -> Interval: ...
    @overload
    @property
    def ShowIsoCurves() -> bool: ...
    @overload
    @property
    def UpDirection() -> Vector3d: ...
    @overload
    @staticmethod
    def GetCurrentState() -> DraftAngleAnalysisSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> DraftAngleAnalysisSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def RestoreDefaults() -> None: ...
    @overload
    @AngleRange.setter
    def AngleRange() -> None: ...
    @overload
    @ShowIsoCurves.setter
    def ShowIsoCurves() -> None: ...
    @overload
    @UpDirection.setter
    def UpDirection() -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def UpdateFromState(state: DraftAngleAnalysisSettingsState) -> None: ...


from ..Geometry import Interval
from ..Geometry import Vector3d
class DraftAngleAnalysisSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AngleRange(self) -> Interval: ...
    @overload
    @property
    def ShowIsoCurves(self) -> bool: ...
    @overload
    @property
    def UpDirection(self) -> Vector3d: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @AngleRange.setter
    def AngleRange(self) -> MutableSequence[Interval]: ...
    @overload
    @ShowIsoCurves.setter
    def ShowIsoCurves(self) -> MutableSequence[bool]: ...
    @overload
    @UpDirection.setter
    def UpDirection(self) -> MutableSequence[Vector3d]: ...
    @overload
    def ToString(self) -> str: ...


class EdgeAnalysisSettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def ShowEdgeColor() -> Color: ...
    @overload
    @property
    def ShowEdges() -> int: ...
    @overload
    @staticmethod
    def GetCurrentState() -> EdgeAnalysisSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> EdgeAnalysisSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def RestoreDefaults() -> None: ...
    @overload
    @ShowEdgeColor.setter
    def ShowEdgeColor() -> None: ...
    @overload
    @ShowEdges.setter
    def ShowEdges() -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def UpdateFromState(state: EdgeAnalysisSettingsState) -> None: ...


class EdgeAnalysisSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def ShowEdgeColor(self) -> Color: ...
    @overload
    @property
    def ShowEdges(self) -> int: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @ShowEdgeColor.setter
    def ShowEdgeColor(self) -> MutableSequence[Color]: ...
    @overload
    @ShowEdges.setter
    def ShowEdges(self) -> MutableSequence[int]: ...
    @overload
    def ToString(self) -> str: ...


class FileSettings:
    @overload
    @staticmethod
    def AddSearchPath(folder: str, index: int) -> int: ...
    @overload
    @staticmethod
    def AutoSaveBeforeCommands() -> Iterable[str]: ...
    @overload
    @staticmethod
    def DeleteSearchPath(folder: str) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @staticmethod
    def FindFile(fileName: str) -> str: ...
    @overload
    @property
    def AutoSaveEnabled() -> bool: ...
    @overload
    @property
    def AutoSaveFile() -> str: ...
    @overload
    @property
    def AutoSaveInterval() -> TimeSpan: ...
    @overload
    @property
    def AutoSaveMeshes() -> bool: ...
    @overload
    @property
    def ClipboardCopyToPreviousRhinoVersion() -> bool: ...
    @overload
    @property
    def ClipboardOnExit() -> ClipboardState: ...
    @overload
    @property
    def CreateBackupFiles() -> bool: ...
    @overload
    @property
    def DefaultRuiFile() -> str: ...
    @overload
    @property
    def ExecutableFolder() -> str: ...
    @overload
    @property
    def FileLockingEnabled() -> bool: ...
    @overload
    @property
    def FileLockingOpenWarning() -> bool: ...
    @overload
    @property
    def HelpFilePath() -> str: ...
    @overload
    @property
    def InstallFolder() -> DirectoryInfo: ...
    @overload
    @property
    def LocalProfileDataFolder() -> str: ...
    @overload
    @property
    def SaveViewChanges() -> bool: ...
    @overload
    @property
    def SearchPathCount() -> int: ...
    @overload
    @property
    def TemplateFile() -> str: ...
    @overload
    @property
    def TemplateFolder() -> str: ...
    @overload
    @property
    def WorkingFolder() -> str: ...
    @overload
    @staticmethod
    def GetCurrentState() -> FileSettingsState: ...
    @overload
    @staticmethod
    def GetDataFolder(currentUser: bool) -> str: ...
    @overload
    @staticmethod
    def GetDefaultState() -> FileSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    @staticmethod
    def GetSearchPaths() -> Iterable[str]: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def RecentlyOpenedFiles() -> Iterable[str]: ...
    @overload
    @AutoSaveEnabled.setter
    def AutoSaveEnabled() -> None: ...
    @overload
    @AutoSaveFile.setter
    def AutoSaveFile() -> None: ...
    @overload
    @AutoSaveInterval.setter
    def AutoSaveInterval() -> None: ...
    @overload
    @AutoSaveMeshes.setter
    def AutoSaveMeshes() -> None: ...
    @overload
    @ClipboardCopyToPreviousRhinoVersion.setter
    def ClipboardCopyToPreviousRhinoVersion() -> None: ...
    @overload
    @ClipboardOnExit.setter
    def ClipboardOnExit() -> None: ...
    @overload
    @CreateBackupFiles.setter
    def CreateBackupFiles() -> None: ...
    @overload
    @FileLockingEnabled.setter
    def FileLockingEnabled() -> None: ...
    @overload
    @FileLockingOpenWarning.setter
    def FileLockingOpenWarning() -> None: ...
    @overload
    @SaveViewChanges.setter
    def SaveViewChanges() -> None: ...
    @overload
    @TemplateFile.setter
    def TemplateFile() -> None: ...
    @overload
    @TemplateFolder.setter
    def TemplateFolder() -> None: ...
    @overload
    @WorkingFolder.setter
    def WorkingFolder() -> None: ...
    @overload
    @staticmethod
    def SetAutoSaveBeforeCommands(commands: Iterable[str]) -> None: ...
    @overload
    def ToString(self) -> str: ...


class FileSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AutoSaveEnabled(self) -> bool: ...
    @overload
    @property
    def AutoSaveInterval(self) -> TimeSpan: ...
    @overload
    @property
    def AutoSaveMeshes(self) -> bool: ...
    @overload
    @property
    def ClipboardCopyToPreviousRhinoVersion(self) -> bool: ...
    @overload
    @property
    def ClipboardOnExit(self) -> ClipboardState: ...
    @overload
    @property
    def CreateBackupFiles(self) -> bool: ...
    @overload
    @property
    def FileLockingEnabled(self) -> bool: ...
    @overload
    @property
    def FileLockingOpenWarning(self) -> bool: ...
    @overload
    @property
    def SaveViewChanges(self) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @AutoSaveEnabled.setter
    def AutoSaveEnabled(self) -> MutableSequence[bool]: ...
    @overload
    @AutoSaveInterval.setter
    def AutoSaveInterval(self) -> MutableSequence[TimeSpan]: ...
    @overload
    @AutoSaveMeshes.setter
    def AutoSaveMeshes(self) -> MutableSequence[bool]: ...
    @overload
    @ClipboardCopyToPreviousRhinoVersion.setter
    def ClipboardCopyToPreviousRhinoVersion(self) -> MutableSequence[bool]: ...
    @overload
    @ClipboardOnExit.setter
    def ClipboardOnExit(self) -> MutableSequence[ClipboardState]: ...
    @overload
    @CreateBackupFiles.setter
    def CreateBackupFiles(self) -> MutableSequence[bool]: ...
    @overload
    @FileLockingEnabled.setter
    def FileLockingEnabled(self) -> MutableSequence[bool]: ...
    @overload
    @FileLockingOpenWarning.setter
    def FileLockingOpenWarning(self) -> MutableSequence[bool]: ...
    @overload
    @SaveViewChanges.setter
    def SaveViewChanges(self) -> MutableSequence[bool]: ...
    @overload
    def ToString(self) -> str: ...


class GeneralSettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AutoUpdateCommandHelp() -> bool: ...
    @overload
    @property
    def ContextMenuDelay() -> TimeSpan: ...
    @overload
    @property
    def EnableContextMenu() -> bool: ...
    @overload
    @property
    def MaximumPopupMenuLines() -> int: ...
    @overload
    @property
    def MaximumUndoMemoryMb() -> int: ...
    @overload
    @property
    def MiddleMouseMacro() -> str: ...
    @overload
    @property
    def MiddleMouseMode() -> MiddleMouseMode: ...
    @overload
    @property
    def MiddleMousePopupToolbar() -> str: ...
    @overload
    @property
    def MinimumUndoSteps() -> int: ...
    @overload
    @property
    def MouseSelectMode() -> MouseSelectMode: ...
    @overload
    @property
    def NewObjectIsoparmCount() -> int: ...
    @overload
    @property
    def UseExtrusions() -> bool: ...
    @overload
    @staticmethod
    def GetCurrentState() -> GeneralSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> GeneralSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @AutoUpdateCommandHelp.setter
    def AutoUpdateCommandHelp() -> None: ...
    @overload
    @ContextMenuDelay.setter
    def ContextMenuDelay() -> None: ...
    @overload
    @EnableContextMenu.setter
    def EnableContextMenu() -> None: ...
    @overload
    @MaximumPopupMenuLines.setter
    def MaximumPopupMenuLines() -> None: ...
    @overload
    @MaximumUndoMemoryMb.setter
    def MaximumUndoMemoryMb() -> None: ...
    @overload
    @MiddleMouseMacro.setter
    def MiddleMouseMacro() -> None: ...
    @overload
    @MiddleMouseMode.setter
    def MiddleMouseMode() -> None: ...
    @overload
    @MiddleMousePopupToolbar.setter
    def MiddleMousePopupToolbar() -> None: ...
    @overload
    @MinimumUndoSteps.setter
    def MinimumUndoSteps() -> None: ...
    @overload
    @MouseSelectMode.setter
    def MouseSelectMode() -> None: ...
    @overload
    @NewObjectIsoparmCount.setter
    def NewObjectIsoparmCount() -> None: ...
    @overload
    def ToString(self) -> str: ...


class GeneralSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AutoUpdateCommandHelp(self) -> bool: ...
    @overload
    @property
    def ContextMenuDelay(self) -> TimeSpan: ...
    @overload
    @property
    def EnableContextMenu(self) -> bool: ...
    @overload
    @property
    def MaximumPopupMenuLines(self) -> int: ...
    @overload
    @property
    def MaximumUndoMemoryMb(self) -> int: ...
    @overload
    @property
    def MiddleMouseMacro(self) -> str: ...
    @overload
    @property
    def MiddleMouseMode(self) -> MiddleMouseMode: ...
    @overload
    @property
    def MiddleMousePopupToolbar(self) -> str: ...
    @overload
    @property
    def MinimumUndoSteps(self) -> int: ...
    @overload
    @property
    def MouseSelectMode(self) -> MouseSelectMode: ...
    @overload
    @property
    def NewObjectIsoparmCount(self) -> int: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @AutoUpdateCommandHelp.setter
    def AutoUpdateCommandHelp(self) -> MutableSequence[bool]: ...
    @overload
    @ContextMenuDelay.setter
    def ContextMenuDelay(self) -> MutableSequence[TimeSpan]: ...
    @overload
    @EnableContextMenu.setter
    def EnableContextMenu(self) -> MutableSequence[bool]: ...
    @overload
    @MaximumPopupMenuLines.setter
    def MaximumPopupMenuLines(self) -> MutableSequence[int]: ...
    @overload
    @MaximumUndoMemoryMb.setter
    def MaximumUndoMemoryMb(self) -> MutableSequence[int]: ...
    @overload
    @MiddleMouseMacro.setter
    def MiddleMouseMacro(self) -> MutableSequence[str]: ...
    @overload
    @MiddleMouseMode.setter
    def MiddleMouseMode(self) -> MutableSequence[MiddleMouseMode]: ...
    @overload
    @MiddleMousePopupToolbar.setter
    def MiddleMousePopupToolbar(self) -> MutableSequence[str]: ...
    @overload
    @MinimumUndoSteps.setter
    def MinimumUndoSteps(self) -> MutableSequence[int]: ...
    @overload
    @MouseSelectMode.setter
    def MouseSelectMode(self) -> MutableSequence[MouseSelectMode]: ...
    @overload
    @NewObjectIsoparmCount.setter
    def NewObjectIsoparmCount(self) -> MutableSequence[int]: ...
    @overload
    def ToString(self) -> str: ...


class HistorySettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def BrokenRecordWarningEnabled() -> bool: ...
    @overload
    @property
    def ObjectLockingEnabled() -> bool: ...
    @overload
    @property
    def RecordingEnabled() -> bool: ...
    @overload
    @property
    def UpdateEnabled() -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @BrokenRecordWarningEnabled.setter
    def BrokenRecordWarningEnabled() -> None: ...
    @overload
    @ObjectLockingEnabled.setter
    def ObjectLockingEnabled() -> None: ...
    @overload
    @RecordingEnabled.setter
    def RecordingEnabled() -> None: ...
    @overload
    @UpdateEnabled.setter
    def UpdateEnabled() -> None: ...
    @overload
    def ToString(self) -> str: ...


class Installation(Enum):
    Undefined = 0
    Commercial = 1
    Educational = 2
    EducationalLab = 3
    NotForResale = 4
    NotForResaleLab = 5
    Beta = 6
    BetaLab = 7
    Evaluation = 8
    Corporate = 9
    EvaluationTimed = 10


class LicenseNode(Enum):
    Standalone = 0
    Network = 1
    NetworkCheckedOut = 2


class MiddleMouseMode(Enum):
    PopupMenu = 0
    PopupToolbar = 1
    RunMacro = 2


class ModelAidSettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AltPlusArrow() -> bool: ...
    @overload
    @property
    def AutoGumballEnabled() -> bool: ...
    @overload
    @property
    def ControlPolygonDisplayDensity() -> int: ...
    @overload
    @property
    def CtrlNudgeKeyStep() -> float: ...
    @overload
    @property
    def DisplayControlPolygon() -> bool: ...
    @overload
    @property
    def ExtendToApparentIntersection() -> bool: ...
    @overload
    @property
    def ExtendTrimLines() -> bool: ...
    @overload
    @property
    def GridSnap() -> bool: ...
    @overload
    @property
    def HighlightControlPolygon() -> bool: ...
    @overload
    @property
    def MousePickboxRadius() -> int: ...
    @overload
    @property
    def NudgeKeyStep() -> float: ...
    @overload
    @property
    def NudgeMode() -> int: ...
    @overload
    @property
    def Ortho() -> bool: ...
    @overload
    @property
    def OrthoAngle() -> float: ...
    @overload
    @property
    def Osnap() -> bool: ...
    @overload
    @property
    def OsnapCursorMode() -> CursorMode: ...
    @overload
    @property
    def OsnapModes() -> OsnapModes: ...
    @overload
    @property
    def OsnapPickboxRadius() -> int: ...
    @overload
    @property
    def Planar() -> bool: ...
    @overload
    @property
    def PointDisplay() -> PointDisplayMode: ...
    @overload
    @property
    def ProjectSnapToCPlane() -> bool: ...
    @overload
    @property
    def ShiftNudgeKeyStep() -> float: ...
    @overload
    @property
    def SnappyGumballEnabled() -> bool: ...
    @overload
    @property
    def SnapToLocked() -> bool: ...
    @overload
    @property
    def UniversalConstructionPlaneMode() -> bool: ...
    @overload
    @property
    def UseHorizontalDialog() -> bool: ...
    @overload
    @staticmethod
    def GetCurrentState() -> ModelAidSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> ModelAidSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @AltPlusArrow.setter
    def AltPlusArrow() -> None: ...
    @overload
    @AutoGumballEnabled.setter
    def AutoGumballEnabled() -> None: ...
    @overload
    @ControlPolygonDisplayDensity.setter
    def ControlPolygonDisplayDensity() -> None: ...
    @overload
    @CtrlNudgeKeyStep.setter
    def CtrlNudgeKeyStep() -> None: ...
    @overload
    @DisplayControlPolygon.setter
    def DisplayControlPolygon() -> None: ...
    @overload
    @ExtendToApparentIntersection.setter
    def ExtendToApparentIntersection() -> None: ...
    @overload
    @ExtendTrimLines.setter
    def ExtendTrimLines() -> None: ...
    @overload
    @GridSnap.setter
    def GridSnap() -> None: ...
    @overload
    @HighlightControlPolygon.setter
    def HighlightControlPolygon() -> None: ...
    @overload
    @MousePickboxRadius.setter
    def MousePickboxRadius() -> None: ...
    @overload
    @NudgeKeyStep.setter
    def NudgeKeyStep() -> None: ...
    @overload
    @NudgeMode.setter
    def NudgeMode() -> None: ...
    @overload
    @Ortho.setter
    def Ortho() -> None: ...
    @overload
    @OrthoAngle.setter
    def OrthoAngle() -> None: ...
    @overload
    @Osnap.setter
    def Osnap() -> None: ...
    @overload
    @OsnapCursorMode.setter
    def OsnapCursorMode() -> None: ...
    @overload
    @OsnapModes.setter
    def OsnapModes() -> None: ...
    @overload
    @OsnapPickboxRadius.setter
    def OsnapPickboxRadius() -> None: ...
    @overload
    @Planar.setter
    def Planar() -> None: ...
    @overload
    @PointDisplay.setter
    def PointDisplay() -> None: ...
    @overload
    @ProjectSnapToCPlane.setter
    def ProjectSnapToCPlane() -> None: ...
    @overload
    @ShiftNudgeKeyStep.setter
    def ShiftNudgeKeyStep() -> None: ...
    @overload
    @SnappyGumballEnabled.setter
    def SnappyGumballEnabled() -> None: ...
    @overload
    @SnapToLocked.setter
    def SnapToLocked() -> None: ...
    @overload
    @UniversalConstructionPlaneMode.setter
    def UniversalConstructionPlaneMode() -> None: ...
    @overload
    @UseHorizontalDialog.setter
    def UseHorizontalDialog() -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def UpdateFromState(state: ModelAidSettingsState) -> None: ...


class ModelAidSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AltPlusArrow(self) -> bool: ...
    @overload
    @property
    def ControlPolygonDisplayDensity(self) -> int: ...
    @overload
    @property
    def CtrlNudgeKeyStep(self) -> float: ...
    @overload
    @property
    def DisplayControlPolygon(self) -> bool: ...
    @overload
    @property
    def ExtendToApparentIntersection(self) -> bool: ...
    @overload
    @property
    def ExtendTrimLines(self) -> bool: ...
    @overload
    @property
    def GridSnap(self) -> bool: ...
    @overload
    @property
    def HighlightControlPolygon(self) -> bool: ...
    @overload
    @property
    def MousePickboxRadius(self) -> int: ...
    @overload
    @property
    def NudgeKeyStep(self) -> float: ...
    @overload
    @property
    def NudgeMode(self) -> int: ...
    @overload
    @property
    def Ortho(self) -> bool: ...
    @overload
    @property
    def OrthoAngle(self) -> float: ...
    @overload
    @property
    def Osnap(self) -> bool: ...
    @overload
    @property
    def OsnapCursorMode(self) -> CursorMode: ...
    @overload
    @property
    def OsnapModes(self) -> OsnapModes: ...
    @overload
    @property
    def OsnapPickboxRadius(self) -> int: ...
    @overload
    @property
    def Planar(self) -> bool: ...
    @overload
    @property
    def PointDisplay(self) -> PointDisplayMode: ...
    @overload
    @property
    def ProjectSnapToCPlane(self) -> bool: ...
    @overload
    @property
    def ShiftNudgeKeyStep(self) -> float: ...
    @overload
    @property
    def SnapToLocked(self) -> bool: ...
    @overload
    @property
    def UniversalConstructionPlaneMode(self) -> bool: ...
    @overload
    @property
    def UseHorizontalDialog(self) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @AltPlusArrow.setter
    def AltPlusArrow(self) -> MutableSequence[bool]: ...
    @overload
    @ControlPolygonDisplayDensity.setter
    def ControlPolygonDisplayDensity(self) -> MutableSequence[int]: ...
    @overload
    @CtrlNudgeKeyStep.setter
    def CtrlNudgeKeyStep(self) -> MutableSequence[float]: ...
    @overload
    @DisplayControlPolygon.setter
    def DisplayControlPolygon(self) -> MutableSequence[bool]: ...
    @overload
    @ExtendToApparentIntersection.setter
    def ExtendToApparentIntersection(self) -> MutableSequence[bool]: ...
    @overload
    @ExtendTrimLines.setter
    def ExtendTrimLines(self) -> MutableSequence[bool]: ...
    @overload
    @GridSnap.setter
    def GridSnap(self) -> MutableSequence[bool]: ...
    @overload
    @HighlightControlPolygon.setter
    def HighlightControlPolygon(self) -> MutableSequence[bool]: ...
    @overload
    @MousePickboxRadius.setter
    def MousePickboxRadius(self) -> MutableSequence[int]: ...
    @overload
    @NudgeKeyStep.setter
    def NudgeKeyStep(self) -> MutableSequence[float]: ...
    @overload
    @NudgeMode.setter
    def NudgeMode(self) -> MutableSequence[int]: ...
    @overload
    @Ortho.setter
    def Ortho(self) -> MutableSequence[bool]: ...
    @overload
    @OrthoAngle.setter
    def OrthoAngle(self) -> MutableSequence[float]: ...
    @overload
    @Osnap.setter
    def Osnap(self) -> MutableSequence[bool]: ...
    @overload
    @OsnapCursorMode.setter
    def OsnapCursorMode(self) -> MutableSequence[CursorMode]: ...
    @overload
    @OsnapModes.setter
    def OsnapModes(self) -> MutableSequence[OsnapModes]: ...
    @overload
    @OsnapPickboxRadius.setter
    def OsnapPickboxRadius(self) -> MutableSequence[int]: ...
    @overload
    @Planar.setter
    def Planar(self) -> MutableSequence[bool]: ...
    @overload
    @PointDisplay.setter
    def PointDisplay(self) -> MutableSequence[PointDisplayMode]: ...
    @overload
    @ProjectSnapToCPlane.setter
    def ProjectSnapToCPlane(self) -> MutableSequence[bool]: ...
    @overload
    @ShiftNudgeKeyStep.setter
    def ShiftNudgeKeyStep(self) -> MutableSequence[float]: ...
    @overload
    @SnapToLocked.setter
    def SnapToLocked(self) -> MutableSequence[bool]: ...
    @overload
    @UniversalConstructionPlaneMode.setter
    def UniversalConstructionPlaneMode(self) -> MutableSequence[bool]: ...
    @overload
    @UseHorizontalDialog.setter
    def UseHorizontalDialog(self) -> MutableSequence[bool]: ...
    @overload
    def ToString(self) -> str: ...


class MouseSelectMode(Enum):
    Crossing = 0
    Window = 1
    Combo = 2


class NeverRepeatList:
    @overload
    @staticmethod
    def CommandNames() -> Iterable[str]: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def UseNeverRepeatList() -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def SetList(commandNames: Iterable[str]) -> int: ...
    @overload
    def ToString(self) -> str: ...


class OpenGLSettings:
    @overload
    def __init__(self): ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AntialiasLevel() -> AntialiasLevel: ...
    @overload
    @staticmethod
    def GetCurrentState() -> OpenGLSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> OpenGLSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def RestoreDefaults() -> None: ...
    @overload
    @AntialiasLevel.setter
    def AntialiasLevel() -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def UpdateFromState(state: OpenGLSettingsState) -> None: ...


class OpenGLSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AntialiasLevel(self) -> AntialiasLevel: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @AntialiasLevel.setter
    def AntialiasLevel(self) -> MutableSequence[AntialiasLevel]: ...
    @overload
    def ToString(self) -> str: ...


class OsnapModes(Enum):
    # None = 0
    Near = 2
    Focus = 8
    Center = 32
    Vertex = 64
    Knot = 128
    Quadrant = 512
    Midpoint = 2048
    Intersection = 8192
    End = 131072
    Perpendicular = 524288
    Tangent = 2097152
    Point = 134217728


class PackageManagerSettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def Sources() -> str: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @Sources.setter
    def Sources() -> None: ...
    @overload
    def ToString(self) -> str: ...


class PaintColor(Enum):
    NormalStart = 0
    NormalEnd = 1
    NormalBorder = 2
    HotStart = 3
    HotEnd = 4
    HotBorder = 5
    PressedStart = 6
    PressedEnd = 7
    PressedBorder = 8
    TextEnabled = 9
    TextDisabled = 10
    MouseOverControlStart = 11
    MouseOverControlEnd = 12
    MouseOverControlBorder = 13
    ActiveCaption = 14
    InactiveCaption = 15
    PanelBackground = 16
    ActiveViewportTitle = 17
    InactiveViewportTitle = 18
    ModifiedValueControlColor = 19
    EditBoxBackground = 20
    GridLinesOnPanelBackground = 21
    GridLinesOnEditBoxBackground = 22
    InactiveTabBackground = 23


class PointDisplayMode(Enum):
    WorldPoint = 0
    CplanePoint = 1


from ..DocObjects import ObjectType
class SelectionFilterSettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def Enabled() -> bool: ...
    @overload
    @property
    def GlobalGeometryFilter() -> ObjectType: ...
    @overload
    @property
    def OneShotGeometryFilter() -> ObjectType: ...
    @overload
    @property
    def SubObjectSelect() -> bool: ...
    @overload
    @staticmethod
    def GetCurrentState() -> SelectionFilterSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> SelectionFilterSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def RestoreDefaults() -> None: ...
    @overload
    @Enabled.setter
    def Enabled() -> None: ...
    @overload
    @GlobalGeometryFilter.setter
    def GlobalGeometryFilter() -> None: ...
    @overload
    @OneShotGeometryFilter.setter
    def OneShotGeometryFilter() -> None: ...
    @overload
    @SubObjectSelect.setter
    def SubObjectSelect() -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def UpdateFromState(state: SelectionFilterSettingsState) -> None: ...


from ..DocObjects import ObjectType
class SelectionFilterSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def Enabled(self) -> bool: ...
    @overload
    @property
    def GlobalGeometryFilter(self) -> ObjectType: ...
    @overload
    @property
    def OneShotGeometryFilter(self) -> ObjectType: ...
    @overload
    @property
    def SubObjectSelect(self) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @Enabled.setter
    def Enabled(self) -> MutableSequence[bool]: ...
    @overload
    @GlobalGeometryFilter.setter
    def GlobalGeometryFilter(self) -> MutableSequence[ObjectType]: ...
    @overload
    @OneShotGeometryFilter.setter
    def OneShotGeometryFilter(self) -> MutableSequence[ObjectType]: ...
    @overload
    @SubObjectSelect.setter
    def SubObjectSelect(self) -> MutableSequence[bool]: ...
    @overload
    def ToString(self) -> str: ...


class ShortcutKey(Enum):
    F1 = 0
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 4
    F6 = 5
    F7 = 6
    F8 = 7
    F9 = 8
    F10 = 9
    F11 = 10
    F12 = 11
    CtrlF1 = 12
    CtrlF2 = 13
    CtrlF3 = 14
    CtrlF4 = 15
    CtrlF5 = 16
    CtrlF6 = 17
    CtrlF7 = 18
    CtrlF8 = 19
    CtrlF9 = 20
    CtrlF10 = 21
    CtrlF11 = 22
    CtrlF12 = 23
    ShiftCtrlF1 = 24
    ShiftCtrlF2 = 25
    ShiftCtrlF3 = 26
    ShiftCtrlF4 = 27
    ShiftCtrlF5 = 28
    ShiftCtrlF6 = 29
    ShiftCtrlF7 = 30
    ShiftCtrlF8 = 31
    ShiftCtrlF9 = 32
    ShiftCtrlF10 = 33
    ShiftCtrlF11 = 34
    ShiftCtrlF12 = 35
    AltCtrlF1 = 36
    AltCtrlF2 = 37
    AltCtrlF3 = 38
    AltCtrlF4 = 39
    AltCtrlF5 = 40
    AltCtrlF6 = 41
    AltCtrlF7 = 42
    AltCtrlF8 = 43
    AltCtrlF9 = 44
    AltCtrlF10 = 45
    AltCtrlF11 = 46
    AltCtrlF12 = 47
    CtrlA = 48
    CtrlB = 49
    CtrlC = 50
    CtrlD = 51
    CtrlE = 52
    CtrlF = 53
    CtrlG = 54
    CtrlH = 55
    CtrlI = 56
    CtrlJ = 57
    CtrlK = 58
    CtrlL = 59
    CtrlM = 60
    CtrlN = 61
    CtrlO = 62
    CtrlP = 63
    CtrlQ = 64
    CtrlR = 65
    CtrlS = 66
    CtrlT = 67
    CtrlU = 68
    CtrlV = 69
    CtrlW = 70
    CtrlX = 71
    CtrlY = 72
    CtrlZ = 73
    ShiftCtrlA = 74
    ShiftCtrlB = 75
    ShiftCtrlC = 76
    ShiftCtrlD = 77
    ShiftCtrlE = 78
    ShiftCtrlF = 79
    ShiftCtrlG = 80
    ShiftCtrlH = 81
    ShiftCtrlI = 82
    ShiftCtrlJ = 83
    ShiftCtrlK = 84
    ShiftCtrlL = 85
    ShiftCtrlM = 86
    ShiftCtrlN = 87
    ShiftCtrlO = 88
    ShiftCtrlP = 89
    ShiftCtrlQ = 90
    ShiftCtrlR = 91
    ShiftCtrlS = 92
    ShiftCtrlT = 93
    ShiftCtrlU = 94
    ShiftCtrlV = 95
    ShiftCtrlW = 96
    ShiftCtrlX = 97
    ShiftCtrlY = 98
    ShiftCtrlZ = 99
    AltCtrlA = 100
    AltCtrlB = 101
    AltCtrlC = 102
    AltCtrlD = 103
    AltCtrlE = 104
    AltCtrlF = 105
    AltCtrlG = 106
    AltCtrlH = 107
    AltCtrlI = 108
    AltCtrlJ = 109
    AltCtrlK = 110
    AltCtrlL = 111
    AltCtrlM = 112
    AltCtrlN = 113
    AltCtrlO = 114
    AltCtrlP = 115
    AltCtrlQ = 116
    AltCtrlR = 117
    AltCtrlS = 118
    AltCtrlT = 119
    AltCtrlU = 120
    AltCtrlV = 121
    AltCtrlW = 122
    AltCtrlX = 123
    AltCtrlY = 124
    AltCtrlZ = 125
    Ctrl0 = 126
    Ctrl1 = 127
    Ctrl2 = 128
    Ctrl3 = 129
    Ctrl4 = 130
    Ctrl5 = 131
    Ctrl6 = 132
    Ctrl7 = 133
    Ctrl8 = 134
    Ctrl9 = 135
    ShiftCtrl0 = 136
    ShiftCtrl1 = 137
    ShiftCtrl2 = 138
    ShiftCtrl3 = 139
    ShiftCtrl4 = 140
    ShiftCtrl5 = 141
    ShiftCtrl6 = 142
    ShiftCtrl7 = 143
    ShiftCtrl8 = 144
    ShiftCtrl9 = 145
    AltCtrl0 = 146
    AltCtrl1 = 147
    AltCtrl2 = 148
    AltCtrl3 = 149
    AltCtrl4 = 150
    AltCtrl5 = 151
    AltCtrl6 = 152
    AltCtrl7 = 153
    AltCtrl8 = 154
    AltCtrl9 = 155
    Home = 156
    End = 157
    CtrlHome = 158
    CtrlEnd = 159
    ShiftHome = 160
    ShiftEnd = 161
    ShiftCtrlHome = 162
    ShiftCtrlEnd = 163
    AltCtrlHome = 164
    AltCtrlEnd = 165
    PageUp = 166
    PageDown = 167
    ShiftPageUp = 168
    ShiftPageDown = 169
    CtrlPageUp = 170
    CtrlPageDown = 171
    ShiftCtrlPageUp = 172
    ShiftCtrlPageDown = 173
    AltCtrlPageUp = 174
    AltCtrlPageDown = 175


class ShortcutKeySettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    @staticmethod
    def GetMacro(key: ShortcutKey) -> str: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def SetMacro(key: ShortcutKey, macro: str) -> None: ...
    @overload
    def ToString(self) -> str: ...


class SmartTrackSettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def ActivationDelayMilliseconds() -> int: ...
    @overload
    @property
    def ActivePointColor() -> Color: ...
    @overload
    @property
    def LineColor() -> Color: ...
    @overload
    @property
    def MaxSmartPoints() -> int: ...
    @overload
    @property
    def PointColor() -> Color: ...
    @overload
    @property
    def SmartOrtho() -> bool: ...
    @overload
    @property
    def SmartTangents() -> bool: ...
    @overload
    @property
    def TanPerpLineColor() -> Color: ...
    @overload
    @property
    def UseDottedLines() -> bool: ...
    @overload
    @property
    def UseSmartTrack() -> bool: ...
    @overload
    @staticmethod
    def GetCurrentState() -> SmartTrackSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> SmartTrackSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @ActivationDelayMilliseconds.setter
    def ActivationDelayMilliseconds() -> None: ...
    @overload
    @ActivePointColor.setter
    def ActivePointColor() -> None: ...
    @overload
    @LineColor.setter
    def LineColor() -> None: ...
    @overload
    @MaxSmartPoints.setter
    def MaxSmartPoints() -> None: ...
    @overload
    @PointColor.setter
    def PointColor() -> None: ...
    @overload
    @SmartOrtho.setter
    def SmartOrtho() -> None: ...
    @overload
    @SmartTangents.setter
    def SmartTangents() -> None: ...
    @overload
    @TanPerpLineColor.setter
    def TanPerpLineColor() -> None: ...
    @overload
    @UseDottedLines.setter
    def UseDottedLines() -> None: ...
    @overload
    @UseSmartTrack.setter
    def UseSmartTrack() -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def UpdateFromState(state: SmartTrackSettingsState) -> None: ...


class SmartTrackSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def ActivationDelayMilliseconds(self) -> int: ...
    @overload
    @property
    def ActivePointColor(self) -> Color: ...
    @overload
    @property
    def LineColor(self) -> Color: ...
    @overload
    @property
    def MaxSmartPoints() -> int: ...
    @overload
    @property
    def PointColor(self) -> Color: ...
    @overload
    @property
    def SmartOrtho(self) -> bool: ...
    @overload
    @property
    def SmartTangents(self) -> bool: ...
    @overload
    @property
    def TanPerpLineColor(self) -> Color: ...
    @overload
    @property
    def UseDottedLines(self) -> bool: ...
    @overload
    @property
    def UseSmartTrack(self) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @ActivationDelayMilliseconds.setter
    def ActivationDelayMilliseconds(self) -> MutableSequence[int]: ...
    @overload
    @ActivePointColor.setter
    def ActivePointColor(self) -> MutableSequence[Color]: ...
    @overload
    @LineColor.setter
    def LineColor(self) -> MutableSequence[Color]: ...
    @overload
    @MaxSmartPoints.setter
    def MaxSmartPoints() -> None: ...
    @overload
    @PointColor.setter
    def PointColor(self) -> MutableSequence[Color]: ...
    @overload
    @SmartOrtho.setter
    def SmartOrtho(self) -> MutableSequence[bool]: ...
    @overload
    @SmartTangents.setter
    def SmartTangents(self) -> MutableSequence[bool]: ...
    @overload
    @TanPerpLineColor.setter
    def TanPerpLineColor(self) -> MutableSequence[Color]: ...
    @overload
    @UseDottedLines.setter
    def UseDottedLines(self) -> MutableSequence[bool]: ...
    @overload
    @UseSmartTrack.setter
    def UseSmartTrack(self) -> MutableSequence[bool]: ...
    @overload
    def ToString(self) -> str: ...


class ViewSettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AlwaysPanParallelViews() -> bool: ...
    @overload
    @property
    def DefinedViewSetCPlane() -> bool: ...
    @overload
    @property
    def DefinedViewSetProjection() -> bool: ...
    @overload
    @property
    def LinkedViewports() -> bool: ...
    @overload
    @property
    def PanReverseKeyboardAction() -> bool: ...
    @overload
    @property
    def PanScreenFraction() -> float: ...
    @overload
    @property
    def RotateCircleIncrement() -> int: ...
    @overload
    @property
    def RotateReverseKeyboard() -> bool: ...
    @overload
    @property
    def RotateToView() -> bool: ...
    @overload
    @property
    def SingleClickMaximize() -> bool: ...
    @overload
    @property
    def ZoomExtentsParallelViewBorder() -> float: ...
    @overload
    @property
    def ZoomExtentsPerspectiveViewBorder() -> float: ...
    @overload
    @property
    def ZoomScale() -> float: ...
    @overload
    @staticmethod
    def GetCurrentState() -> ViewSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> ViewSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def RestoreDefaults() -> None: ...
    @overload
    @AlwaysPanParallelViews.setter
    def AlwaysPanParallelViews() -> None: ...
    @overload
    @DefinedViewSetCPlane.setter
    def DefinedViewSetCPlane() -> None: ...
    @overload
    @DefinedViewSetProjection.setter
    def DefinedViewSetProjection() -> None: ...
    @overload
    @LinkedViewports.setter
    def LinkedViewports() -> None: ...
    @overload
    @PanReverseKeyboardAction.setter
    def PanReverseKeyboardAction() -> None: ...
    @overload
    @PanScreenFraction.setter
    def PanScreenFraction() -> None: ...
    @overload
    @RotateCircleIncrement.setter
    def RotateCircleIncrement() -> None: ...
    @overload
    @RotateReverseKeyboard.setter
    def RotateReverseKeyboard() -> None: ...
    @overload
    @RotateToView.setter
    def RotateToView() -> None: ...
    @overload
    @SingleClickMaximize.setter
    def SingleClickMaximize() -> None: ...
    @overload
    @ZoomExtentsParallelViewBorder.setter
    def ZoomExtentsParallelViewBorder() -> None: ...
    @overload
    @ZoomExtentsPerspectiveViewBorder.setter
    def ZoomExtentsPerspectiveViewBorder() -> None: ...
    @overload
    @ZoomScale.setter
    def ZoomScale() -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def UpdateFromState(state: ViewSettingsState) -> None: ...


class ViewSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AlwaysPanParallelViews(self) -> bool: ...
    @overload
    @property
    def DefinedViewSetCPlane(self) -> bool: ...
    @overload
    @property
    def DefinedViewSetProjection(self) -> bool: ...
    @overload
    @property
    def LinkedViewports(self) -> bool: ...
    @overload
    @property
    def PanReverseKeyboardAction(self) -> bool: ...
    @overload
    @property
    def PanScreenFraction(self) -> float: ...
    @overload
    @property
    def RotateCircleIncrement(self) -> int: ...
    @overload
    @property
    def RotateReverseKeyboard(self) -> bool: ...
    @overload
    @property
    def RotateToView(self) -> bool: ...
    @overload
    @property
    def SingleClickMaximize(self) -> bool: ...
    @overload
    @property
    def ZoomExtentsParallelViewBorder(self) -> float: ...
    @overload
    @property
    def ZoomExtentsPerspectiveViewBorder(self) -> float: ...
    @overload
    @property
    def ZoomScale(self) -> float: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @AlwaysPanParallelViews.setter
    def AlwaysPanParallelViews(self) -> MutableSequence[bool]: ...
    @overload
    @DefinedViewSetCPlane.setter
    def DefinedViewSetCPlane(self) -> MutableSequence[bool]: ...
    @overload
    @DefinedViewSetProjection.setter
    def DefinedViewSetProjection(self) -> MutableSequence[bool]: ...
    @overload
    @LinkedViewports.setter
    def LinkedViewports(self) -> MutableSequence[bool]: ...
    @overload
    @PanReverseKeyboardAction.setter
    def PanReverseKeyboardAction(self) -> MutableSequence[bool]: ...
    @overload
    @PanScreenFraction.setter
    def PanScreenFraction(self) -> MutableSequence[float]: ...
    @overload
    @RotateCircleIncrement.setter
    def RotateCircleIncrement(self) -> MutableSequence[int]: ...
    @overload
    @RotateReverseKeyboard.setter
    def RotateReverseKeyboard(self) -> MutableSequence[bool]: ...
    @overload
    @RotateToView.setter
    def RotateToView(self) -> MutableSequence[bool]: ...
    @overload
    @SingleClickMaximize.setter
    def SingleClickMaximize(self) -> MutableSequence[bool]: ...
    @overload
    @ZoomExtentsParallelViewBorder.setter
    def ZoomExtentsParallelViewBorder(self) -> MutableSequence[float]: ...
    @overload
    @ZoomExtentsPerspectiveViewBorder.setter
    def ZoomExtentsPerspectiveViewBorder(self) -> MutableSequence[float]: ...
    @overload
    @ZoomScale.setter
    def ZoomScale(self) -> MutableSequence[float]: ...
    @overload
    def ToString(self) -> str: ...


class WidgetColor(Enum):
    UAxisColor = 0
    VAxisColor = 1
    WAxisColor = 2


class ZebraAnalysisSettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def ShowIsoCurves() -> bool: ...
    @overload
    @property
    def StripeColor() -> Color: ...
    @overload
    @property
    def StripeThickness() -> int: ...
    @overload
    @property
    def VerticalStripes() -> bool: ...
    @overload
    @staticmethod
    def GetCurrentState() -> ZebraAnalysisSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> ZebraAnalysisSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def RestoreDefaults() -> None: ...
    @overload
    @ShowIsoCurves.setter
    def ShowIsoCurves() -> None: ...
    @overload
    @StripeColor.setter
    def StripeColor() -> None: ...
    @overload
    @StripeThickness.setter
    def StripeThickness() -> None: ...
    @overload
    @VerticalStripes.setter
    def VerticalStripes() -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def UpdateFromState(state: ZebraAnalysisSettingsState) -> None: ...


class ZebraAnalysisSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def ShowIsoCurves(self) -> bool: ...
    @overload
    @property
    def StripeColor(self) -> Color: ...
    @overload
    @property
    def StripeThickness(self) -> int: ...
    @overload
    @property
    def VerticalStripes(self) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @ShowIsoCurves.setter
    def ShowIsoCurves(self) -> MutableSequence[bool]: ...
    @overload
    @StripeColor.setter
    def StripeColor(self) -> MutableSequence[Color]: ...
    @overload
    @StripeThickness.setter
    def StripeThickness(self) -> MutableSequence[int]: ...
    @overload
    @VerticalStripes.setter
    def VerticalStripes(self) -> MutableSequence[bool]: ...
    @overload
    def ToString(self) -> str: ...
