from typing import overload, Tuple, Iterable, Iterator, Sequence, MutableSequence
from enum import Enum



class AppearanceSettings:
    @overload
    @staticmethod
    def DefaultPaintColor(whichColor: PaintColor) -> Color: ...
    @overload
    @staticmethod
    def DefaultPaintColor(whichColor: PaintColor, darkMode: bool) -> Color: ...
    @overload
    @staticmethod
    def DefaultWidgetColor(whichColor: WidgetColor) -> Color: ...
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
    def DirectionArrowIconHeadSize() -> int: ...
    @overload
    @property
    def DirectionArrowIconShaftSize() -> int: ...
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
    def ShowLayoutDropShadow() -> bool: ...
    @overload
    @property
    def ShowOsnapBar() -> bool: ...
    @overload
    @property
    def ShowSelectionFilterBar() -> bool: ...
    @overload
    @property
    def ShowSideBar() -> bool: ...
    @overload
    @property
    def ShowStatusBar() -> bool: ...
    @overload
    @property
    def ShowTitleBar() -> bool: ...
    @overload
    @property
    def ShowViewportTitles() -> bool: ...
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
    def ViewportTabsVisibleAtStart() -> bool: ...
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
    @staticmethod
    def GetDefaultState(darkMode: bool) -> AppearanceSettingsState: ...
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
    def CommandPromptBackgroundColor(value: Color) -> None: ...
    @overload
    @CommandPromptFontSize.setter
    def CommandPromptFontSize(value: int) -> None: ...
    @overload
    @CommandPromptHypertextColor.setter
    def CommandPromptHypertextColor(value: Color) -> None: ...
    @overload
    @CommandPromptPosition.setter
    def CommandPromptPosition(value: CommandPromptPosition) -> None: ...
    @overload
    @CommandPromptTextColor.setter
    def CommandPromptTextColor(value: Color) -> None: ...
    @overload
    @CrosshairColor.setter
    def CrosshairColor(value: Color) -> None: ...
    @overload
    @CurrentLayerBackgroundColor.setter
    def CurrentLayerBackgroundColor(value: Color) -> None: ...
    @overload
    @DefaultLayerColor.setter
    def DefaultLayerColor(value: Color) -> None: ...
    @overload
    @DefaultObjectColor.setter
    def DefaultObjectColor(value: Color) -> None: ...
    @overload
    @DirectionArrowIconHeadSize.setter
    def DirectionArrowIconHeadSize(value: int) -> None: ...
    @overload
    @DirectionArrowIconShaftSize.setter
    def DirectionArrowIconShaftSize(value: int) -> None: ...
    @overload
    @EchoCommandsToHistoryWindow.setter
    def EchoCommandsToHistoryWindow(value: bool) -> None: ...
    @overload
    @EchoPromptsToHistoryWindow.setter
    def EchoPromptsToHistoryWindow(value: bool) -> None: ...
    @overload
    @EditCandidateColor.setter
    def EditCandidateColor(value: Color) -> None: ...
    @overload
    @FeedbackColor.setter
    def FeedbackColor(value: Color) -> None: ...
    @overload
    @FrameBackgroundColor.setter
    def FrameBackgroundColor(value: Color) -> None: ...
    @overload
    @GridThickLineColor.setter
    def GridThickLineColor(value: Color) -> None: ...
    @overload
    @GridThinLineColor.setter
    def GridThinLineColor(value: Color) -> None: ...
    @overload
    @GridXAxisLineColor.setter
    def GridXAxisLineColor(value: Color) -> None: ...
    @overload
    @GridYAxisLineColor.setter
    def GridYAxisLineColor(value: Color) -> None: ...
    @overload
    @GridZAxisLineColor.setter
    def GridZAxisLineColor(value: Color) -> None: ...
    @overload
    @LanguageIdentifier.setter
    def LanguageIdentifier(value: int) -> None: ...
    @overload
    @LockedObjectColor.setter
    def LockedObjectColor(value: Color) -> None: ...
    @overload
    @MenuVisible.setter
    def MenuVisible(value: bool) -> None: ...
    @overload
    @PageviewPaperColor.setter
    def PageviewPaperColor(value: Color) -> None: ...
    @overload
    @PreviousLanguageIdentifier.setter
    def PreviousLanguageIdentifier(value: int) -> None: ...
    @overload
    @SelectedObjectColor.setter
    def SelectedObjectColor(value: Color) -> None: ...
    @overload
    @SelectionWindowCrossingFillColor.setter
    def SelectionWindowCrossingFillColor(value: Color) -> None: ...
    @overload
    @SelectionWindowCrossingStrokeColor.setter
    def SelectionWindowCrossingStrokeColor(value: Color) -> None: ...
    @overload
    @SelectionWindowFillColor.setter
    def SelectionWindowFillColor(value: Color) -> None: ...
    @overload
    @SelectionWindowStrokeColor.setter
    def SelectionWindowStrokeColor(value: Color) -> None: ...
    @overload
    @ShowCrosshairs.setter
    def ShowCrosshairs(value: bool) -> None: ...
    @overload
    @ShowFullPathInTitleBar.setter
    def ShowFullPathInTitleBar(value: bool) -> None: ...
    @overload
    @ShowLayoutDropShadow.setter
    def ShowLayoutDropShadow(value: bool) -> None: ...
    @overload
    @ShowOsnapBar.setter
    def ShowOsnapBar(value: bool) -> None: ...
    @overload
    @ShowSelectionFilterBar.setter
    def ShowSelectionFilterBar(value: bool) -> None: ...
    @overload
    @ShowSideBar.setter
    def ShowSideBar(value: bool) -> None: ...
    @overload
    @ShowStatusBar.setter
    def ShowStatusBar(value: bool) -> None: ...
    @overload
    @ShowTitleBar.setter
    def ShowTitleBar(value: bool) -> None: ...
    @overload
    @ShowViewportTitles.setter
    def ShowViewportTitles(value: bool) -> None: ...
    @overload
    @TrackingColor.setter
    def TrackingColor(value: Color) -> None: ...
    @overload
    @ViewportBackgroundColor.setter
    def ViewportBackgroundColor(value: Color) -> None: ...
    @overload
    @ViewportTabsVisibleAtStart.setter
    def ViewportTabsVisibleAtStart(value: bool) -> None: ...
    @overload
    @WorldCoordIconXAxisColor.setter
    def WorldCoordIconXAxisColor(value: Color) -> None: ...
    @overload
    @WorldCoordIconYAxisColor.setter
    def WorldCoordIconYAxisColor(value: Color) -> None: ...
    @overload
    @WorldCoordIconZAxisColor.setter
    def WorldCoordIconZAxisColor(value: Color) -> None: ...
    @overload
    @staticmethod
    def SetPaintColor(whichColor: PaintColor, c: Color) -> None: ...
    @overload
    @staticmethod
    def SetPaintColor(whichColor: PaintColor, c: Color, forceUiUpdate: bool) -> None: ...
    @overload
    @staticmethod
    def SetToDarkMode() -> bool: ...
    @overload
    @staticmethod
    def SetToLightMode() -> bool: ...
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
    @overload
    @staticmethod
    def UsingDefaultDarkModeColors() -> bool: ...
    @overload
    @staticmethod
    def UsingDefaultLightModeColors() -> bool: ...


class AppearanceSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def CommandPromptBackgroundColor(self) -> Color: ...
    @overload
    @property
    def CommandPromptFontName(self) -> str: ...
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
    def DirectionArrowIconHeadSize(self) -> int: ...
    @overload
    @property
    def DirectionArrowIconShaftSize(self) -> int: ...
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
    def MenuVisible(self) -> bool: ...
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
    def ShowLayoutDropShadow(self) -> bool: ...
    @overload
    @property
    def ShowStatusBar(self) -> bool: ...
    @overload
    @property
    def ShowTitleBar(self) -> bool: ...
    @overload
    @property
    def ShowViewportTitles(self) -> bool: ...
    @overload
    @property
    def TrackingColor(self) -> Color: ...
    @overload
    @property
    def ViewportBackgroundColor(self) -> Color: ...
    @overload
    @property
    def ViewportTabsVisibleAtStart(self) -> bool: ...
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
    def CommandPromptBackgroundColor(self, value: Color) -> None: ...
    @overload
    @CommandPromptFontName.setter
    def CommandPromptFontName(self, value: str) -> None: ...
    @overload
    @CommandPromptFontSize.setter
    def CommandPromptFontSize(self, value: int) -> None: ...
    @overload
    @CommandPromptHypertextColor.setter
    def CommandPromptHypertextColor(self, value: Color) -> None: ...
    @overload
    @CommandPromptTextColor.setter
    def CommandPromptTextColor(self, value: Color) -> None: ...
    @overload
    @CrosshairColor.setter
    def CrosshairColor(self, value: Color) -> None: ...
    @overload
    @CurrentLayerBackgroundColor.setter
    def CurrentLayerBackgroundColor(self, value: Color) -> None: ...
    @overload
    @DefaultFontFaceName.setter
    def DefaultFontFaceName(self, value: str) -> None: ...
    @overload
    @DefaultLayerColor.setter
    def DefaultLayerColor(self, value: Color) -> None: ...
    @overload
    @DefaultObjectColor.setter
    def DefaultObjectColor(self, value: Color) -> None: ...
    @overload
    @DirectionArrowIconHeadSize.setter
    def DirectionArrowIconHeadSize(self, value: int) -> None: ...
    @overload
    @DirectionArrowIconShaftSize.setter
    def DirectionArrowIconShaftSize(self, value: int) -> None: ...
    @overload
    @EchoCommandsToHistoryWindow.setter
    def EchoCommandsToHistoryWindow(self, value: bool) -> None: ...
    @overload
    @EchoPromptsToHistoryWindow.setter
    def EchoPromptsToHistoryWindow(self, value: bool) -> None: ...
    @overload
    @EditCandidateColor.setter
    def EditCandidateColor(self, value: Color) -> None: ...
    @overload
    @FeedbackColor.setter
    def FeedbackColor(self, value: Color) -> None: ...
    @overload
    @FrameBackgroundColor.setter
    def FrameBackgroundColor(self, value: Color) -> None: ...
    @overload
    @GridThickLineColor.setter
    def GridThickLineColor(self, value: Color) -> None: ...
    @overload
    @GridThinLineColor.setter
    def GridThinLineColor(self, value: Color) -> None: ...
    @overload
    @GridXAxisLineColor.setter
    def GridXAxisLineColor(self, value: Color) -> None: ...
    @overload
    @GridYAxisLineColor.setter
    def GridYAxisLineColor(self, value: Color) -> None: ...
    @overload
    @GridZAxisLineColor.setter
    def GridZAxisLineColor(self, value: Color) -> None: ...
    @overload
    @LockedObjectColor.setter
    def LockedObjectColor(self, value: Color) -> None: ...
    @overload
    @MenuVisible.setter
    def MenuVisible(self, value: bool) -> None: ...
    @overload
    @PageviewPaperColor.setter
    def PageviewPaperColor(self, value: Color) -> None: ...
    @overload
    @SelectedObjectColor.setter
    def SelectedObjectColor(self, value: Color) -> None: ...
    @overload
    @SelectionWindowCrossingFillColor.setter
    def SelectionWindowCrossingFillColor(self, value: Color) -> None: ...
    @overload
    @SelectionWindowCrossingStrokeColor.setter
    def SelectionWindowCrossingStrokeColor(self, value: Color) -> None: ...
    @overload
    @SelectionWindowFillColor.setter
    def SelectionWindowFillColor(self, value: Color) -> None: ...
    @overload
    @SelectionWindowStrokeColor.setter
    def SelectionWindowStrokeColor(self, value: Color) -> None: ...
    @overload
    @ShowCrosshairs.setter
    def ShowCrosshairs(self, value: bool) -> None: ...
    @overload
    @ShowFullPathInTitleBar.setter
    def ShowFullPathInTitleBar(self, value: bool) -> None: ...
    @overload
    @ShowLayoutDropShadow.setter
    def ShowLayoutDropShadow(self, value: bool) -> None: ...
    @overload
    @ShowStatusBar.setter
    def ShowStatusBar(self, value: bool) -> None: ...
    @overload
    @ShowTitleBar.setter
    def ShowTitleBar(self, value: bool) -> None: ...
    @overload
    @ShowViewportTitles.setter
    def ShowViewportTitles(self, value: bool) -> None: ...
    @overload
    @TrackingColor.setter
    def TrackingColor(self, value: Color) -> None: ...
    @overload
    @ViewportBackgroundColor.setter
    def ViewportBackgroundColor(self, value: Color) -> None: ...
    @overload
    @ViewportTabsVisibleAtStart.setter
    def ViewportTabsVisibleAtStart(self, value: bool) -> None: ...
    @overload
    @WorldCoordIconXAxisColor.setter
    def WorldCoordIconXAxisColor(self, value: Color) -> None: ...
    @overload
    @WorldCoordIconYAxisColor.setter
    def WorldCoordIconYAxisColor(self, value: Color) -> None: ...
    @overload
    @WorldCoordIconZAxisColor.setter
    def WorldCoordIconZAxisColor(self, value: Color) -> None: ...
    @overload
    def ToString(self) -> str: ...


class ChooseOneObjectSettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AutomaticResize() -> bool: ...
    @overload
    @property
    def DynamicHighlight() -> bool: ...
    @overload
    @property
    def FollowCursor() -> bool: ...
    @overload
    @property
    def HighlightColor() -> Color: ...
    @overload
    @property
    def MaxAutoResizeItems() -> int: ...
    @overload
    @property
    def ShowAllOption() -> bool: ...
    @overload
    @property
    def ShowObjectColor() -> bool: ...
    @overload
    @property
    def ShowObjectLayer() -> bool: ...
    @overload
    @property
    def ShowObjectName() -> bool: ...
    @overload
    @property
    def ShowObjectType() -> bool: ...
    @overload
    @property
    def ShowObjectTypeDetails() -> bool: ...
    @overload
    @property
    def ShowTitlebarAndBorder() -> bool: ...
    @overload
    @property
    def UseCustomColor() -> bool: ...
    @overload
    @property
    def XOffset() -> int: ...
    @overload
    @property
    def YOffset() -> int: ...
    @overload
    @staticmethod
    def GetCurrentState() -> ChooseOneObjectSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> ChooseOneObjectSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def RestoreDefaults() -> None: ...
    @overload
    @AutomaticResize.setter
    def AutomaticResize(value: bool) -> None: ...
    @overload
    @DynamicHighlight.setter
    def DynamicHighlight(value: bool) -> None: ...
    @overload
    @FollowCursor.setter
    def FollowCursor(value: bool) -> None: ...
    @overload
    @HighlightColor.setter
    def HighlightColor(value: Color) -> None: ...
    @overload
    @MaxAutoResizeItems.setter
    def MaxAutoResizeItems(value: int) -> None: ...
    @overload
    @ShowAllOption.setter
    def ShowAllOption(value: bool) -> None: ...
    @overload
    @ShowObjectColor.setter
    def ShowObjectColor(value: bool) -> None: ...
    @overload
    @ShowObjectLayer.setter
    def ShowObjectLayer(value: bool) -> None: ...
    @overload
    @ShowObjectName.setter
    def ShowObjectName(value: bool) -> None: ...
    @overload
    @ShowObjectType.setter
    def ShowObjectType(value: bool) -> None: ...
    @overload
    @ShowObjectTypeDetails.setter
    def ShowObjectTypeDetails(value: bool) -> None: ...
    @overload
    @ShowTitlebarAndBorder.setter
    def ShowTitlebarAndBorder(value: bool) -> None: ...
    @overload
    @UseCustomColor.setter
    def UseCustomColor(value: bool) -> None: ...
    @overload
    @XOffset.setter
    def XOffset(value: int) -> None: ...
    @overload
    @YOffset.setter
    def YOffset(value: int) -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def UpdateFromState(state: ChooseOneObjectSettingsState) -> None: ...


class ChooseOneObjectSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AutomaticResize(self) -> bool: ...
    @overload
    @property
    def DynamicHighlight(self) -> bool: ...
    @overload
    @property
    def FollowCursor(self) -> bool: ...
    @overload
    @property
    def HighlightColor(self) -> Color: ...
    @overload
    @property
    def MaxAutoResizeItems(self) -> int: ...
    @overload
    @property
    def ShowAllOption(self) -> bool: ...
    @overload
    @property
    def ShowObjectColor(self) -> bool: ...
    @overload
    @property
    def ShowObjectLayer(self) -> bool: ...
    @overload
    @property
    def ShowObjectName(self) -> bool: ...
    @overload
    @property
    def ShowObjectType(self) -> bool: ...
    @overload
    @property
    def ShowObjectTypeDetails(self) -> bool: ...
    @overload
    @property
    def ShowTitlebarAndBorder(self) -> bool: ...
    @overload
    @property
    def UseCustomColor(self) -> bool: ...
    @overload
    @property
    def XOffset(self) -> int: ...
    @overload
    @property
    def YOffset(self) -> int: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @AutomaticResize.setter
    def AutomaticResize(self, value: bool) -> None: ...
    @overload
    @DynamicHighlight.setter
    def DynamicHighlight(self, value: bool) -> None: ...
    @overload
    @FollowCursor.setter
    def FollowCursor(self, value: bool) -> None: ...
    @overload
    @HighlightColor.setter
    def HighlightColor(self, value: Color) -> None: ...
    @overload
    @MaxAutoResizeItems.setter
    def MaxAutoResizeItems(self, value: int) -> None: ...
    @overload
    @ShowAllOption.setter
    def ShowAllOption(self, value: bool) -> None: ...
    @overload
    @ShowObjectColor.setter
    def ShowObjectColor(self, value: bool) -> None: ...
    @overload
    @ShowObjectLayer.setter
    def ShowObjectLayer(self, value: bool) -> None: ...
    @overload
    @ShowObjectName.setter
    def ShowObjectName(self, value: bool) -> None: ...
    @overload
    @ShowObjectType.setter
    def ShowObjectType(self, value: bool) -> None: ...
    @overload
    @ShowObjectTypeDetails.setter
    def ShowObjectTypeDetails(self, value: bool) -> None: ...
    @overload
    @ShowTitlebarAndBorder.setter
    def ShowTitlebarAndBorder(self, value: bool) -> None: ...
    @overload
    @UseCustomColor.setter
    def UseCustomColor(self, value: bool) -> None: ...
    @overload
    @XOffset.setter
    def XOffset(self, value: int) -> None: ...
    @overload
    @YOffset.setter
    def YOffset(self, value: int) -> None: ...
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
    def EnableGumballToolTips() -> bool: ...
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
    def AutoSuppress(value: bool) -> None: ...
    @overload
    @BackgroundColor.setter
    def BackgroundColor(value: Color) -> None: ...
    @overload
    @CommandPromptPane.setter
    def CommandPromptPane(value: bool) -> None: ...
    @overload
    @DistancePane.setter
    def DistancePane(value: bool) -> None: ...
    @overload
    @EnableGumballToolTips.setter
    def EnableGumballToolTips(value: bool) -> None: ...
    @overload
    @Offset.setter
    def Offset(value: Point) -> None: ...
    @overload
    @OsnapPane.setter
    def OsnapPane(value: bool) -> None: ...
    @overload
    @PointPane.setter
    def PointPane(value: bool) -> None: ...
    @overload
    @RelativePointPane.setter
    def RelativePointPane(value: bool) -> None: ...
    @overload
    @TextColor.setter
    def TextColor(value: Color) -> None: ...
    @overload
    @TooltipsEnabled.setter
    def TooltipsEnabled(value: bool) -> None: ...
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
    def EnableGumballToolTips(self) -> bool: ...
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
    def AutoSuppress(self, value: bool) -> None: ...
    @overload
    @BackgroundColor.setter
    def BackgroundColor(self, value: Color) -> None: ...
    @overload
    @CommandPromptPane.setter
    def CommandPromptPane(self, value: bool) -> None: ...
    @overload
    @DistancePane.setter
    def DistancePane(self, value: bool) -> None: ...
    @overload
    @EnableGumballToolTips.setter
    def EnableGumballToolTips(self, value: bool) -> None: ...
    @overload
    @Offset.setter
    def Offset(self, value: Point) -> None: ...
    @overload
    @OsnapPane.setter
    def OsnapPane(self, value: bool) -> None: ...
    @overload
    @PointPane.setter
    def PointPane(self, value: bool) -> None: ...
    @overload
    @RelativePointPane.setter
    def RelativePointPane(self, value: bool) -> None: ...
    @overload
    @TextColor.setter
    def TextColor(self, value: Color) -> None: ...
    @overload
    @TooltipsEnabled.setter
    def TooltipsEnabled(self, value: bool) -> None: ...
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
    def GaussRange(value: Interval) -> None: ...
    @overload
    @MaxRadiusRange.setter
    def MaxRadiusRange(value: Interval) -> None: ...
    @overload
    @MeanRange.setter
    def MeanRange(value: Interval) -> None: ...
    @overload
    @MinRadiusRange.setter
    def MinRadiusRange(value: Interval) -> None: ...
    @overload
    @Style.setter
    def Style(value: CurvatureStyle) -> None: ...
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
    def GaussRange(self, value: Interval) -> None: ...
    @overload
    @MaxRadiusRange.setter
    def MaxRadiusRange(self, value: Interval) -> None: ...
    @overload
    @MeanRange.setter
    def MeanRange(self, value: Interval) -> None: ...
    @overload
    @MinRadiusRange.setter
    def MinRadiusRange(self, value: Interval) -> None: ...
    @overload
    @Style.setter
    def Style(self, value: CurvatureStyle) -> None: ...
    @overload
    def ToString(self) -> str: ...


class CurvatureGraphSettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def CurveHairColor() -> Color: ...
    @overload
    @property
    def HairDensity() -> int: ...
    @overload
    @property
    def HairScale() -> int: ...
    @overload
    @property
    def SampleDensity() -> int: ...
    @overload
    @property
    def SrfUHair() -> bool: ...
    @overload
    @property
    def SrfVHair() -> bool: ...
    @overload
    @property
    def SurfaceUHairColor() -> Color: ...
    @overload
    @property
    def SurfaceVHairColor() -> Color: ...
    @overload
    @staticmethod
    def GetCurrentState() -> CurvatureGraphSettingsState: ...
    @overload
    @staticmethod
    def GetDefaultState() -> CurvatureGraphSettingsState: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def RestoreDefaults() -> None: ...
    @overload
    @CurveHairColor.setter
    def CurveHairColor(value: Color) -> None: ...
    @overload
    @HairDensity.setter
    def HairDensity(value: int) -> None: ...
    @overload
    @HairScale.setter
    def HairScale(value: int) -> None: ...
    @overload
    @SampleDensity.setter
    def SampleDensity(value: int) -> None: ...
    @overload
    @SrfUHair.setter
    def SrfUHair(value: bool) -> None: ...
    @overload
    @SrfVHair.setter
    def SrfVHair(value: bool) -> None: ...
    @overload
    @SurfaceUHairColor.setter
    def SurfaceUHairColor(value: Color) -> None: ...
    @overload
    @SurfaceVHairColor.setter
    def SurfaceVHairColor(value: Color) -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def UpdateFromState(state: CurvatureGraphSettingsState) -> None: ...


class CurvatureGraphSettingsState:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def CurveHairColor(self) -> Color: ...
    @overload
    @property
    def HairDensity(self) -> int: ...
    @overload
    @property
    def HairScale(self) -> int: ...
    @overload
    @property
    def SampleDensity(self) -> int: ...
    @overload
    @property
    def SrfUHair(self) -> bool: ...
    @overload
    @property
    def SrfVHair(self) -> bool: ...
    @overload
    @property
    def SurfaceUHairColor(self) -> Color: ...
    @overload
    @property
    def SurfaceVHairColor(self) -> Color: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @CurveHairColor.setter
    def CurveHairColor(self, value: Color) -> None: ...
    @overload
    @HairDensity.setter
    def HairDensity(self, value: int) -> None: ...
    @overload
    @HairScale.setter
    def HairScale(self, value: int) -> None: ...
    @overload
    @SampleDensity.setter
    def SampleDensity(self, value: int) -> None: ...
    @overload
    @SrfUHair.setter
    def SrfUHair(self, value: bool) -> None: ...
    @overload
    @SrfVHair.setter
    def SrfVHair(self, value: bool) -> None: ...
    @overload
    @SurfaceUHairColor.setter
    def SurfaceUHairColor(self, value: Color) -> None: ...
    @overload
    @SurfaceVHairColor.setter
    def SurfaceVHairColor(self, value: Color) -> None: ...
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
    def AngleRange(value: Interval) -> None: ...
    @overload
    @ShowIsoCurves.setter
    def ShowIsoCurves(value: bool) -> None: ...
    @overload
    @UpDirection.setter
    def UpDirection(value: Vector3d) -> None: ...
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
    def AngleRange(self, value: Interval) -> None: ...
    @overload
    @ShowIsoCurves.setter
    def ShowIsoCurves(self, value: bool) -> None: ...
    @overload
    @UpDirection.setter
    def UpDirection(self, value: Vector3d) -> None: ...
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
    def ShowEdgeColor(value: Color) -> None: ...
    @overload
    @ShowEdges.setter
    def ShowEdges(value: int) -> None: ...
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
    def ShowEdgeColor(self, value: Color) -> None: ...
    @overload
    @ShowEdges.setter
    def ShowEdges(self, value: int) -> None: ...
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
    def DefaultTemplateFolderForLanguageID(languageID: int) -> str: ...
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
    def AutoSaveEnabled(value: bool) -> None: ...
    @overload
    @AutoSaveFile.setter
    def AutoSaveFile(value: str) -> None: ...
    @overload
    @AutoSaveInterval.setter
    def AutoSaveInterval(value: TimeSpan) -> None: ...
    @overload
    @AutoSaveMeshes.setter
    def AutoSaveMeshes(value: bool) -> None: ...
    @overload
    @ClipboardCopyToPreviousRhinoVersion.setter
    def ClipboardCopyToPreviousRhinoVersion(value: bool) -> None: ...
    @overload
    @ClipboardOnExit.setter
    def ClipboardOnExit(value: ClipboardState) -> None: ...
    @overload
    @CreateBackupFiles.setter
    def CreateBackupFiles(value: bool) -> None: ...
    @overload
    @FileLockingEnabled.setter
    def FileLockingEnabled(value: bool) -> None: ...
    @overload
    @FileLockingOpenWarning.setter
    def FileLockingOpenWarning(value: bool) -> None: ...
    @overload
    @SaveViewChanges.setter
    def SaveViewChanges(value: bool) -> None: ...
    @overload
    @TemplateFile.setter
    def TemplateFile(value: str) -> None: ...
    @overload
    @TemplateFolder.setter
    def TemplateFolder(value: str) -> None: ...
    @overload
    @WorkingFolder.setter
    def WorkingFolder(value: str) -> None: ...
    @overload
    @staticmethod
    def SetAutoSaveBeforeCommands(commands: Iterable[str]) -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def UpdateFromState(state: FileSettingsState) -> None: ...


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
    @property
    def TemplateFileDir(self) -> str: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @AutoSaveEnabled.setter
    def AutoSaveEnabled(self, value: bool) -> None: ...
    @overload
    @AutoSaveInterval.setter
    def AutoSaveInterval(self, value: TimeSpan) -> None: ...
    @overload
    @AutoSaveMeshes.setter
    def AutoSaveMeshes(self, value: bool) -> None: ...
    @overload
    @ClipboardCopyToPreviousRhinoVersion.setter
    def ClipboardCopyToPreviousRhinoVersion(self, value: bool) -> None: ...
    @overload
    @ClipboardOnExit.setter
    def ClipboardOnExit(self, value: ClipboardState) -> None: ...
    @overload
    @CreateBackupFiles.setter
    def CreateBackupFiles(self, value: bool) -> None: ...
    @overload
    @FileLockingEnabled.setter
    def FileLockingEnabled(self, value: bool) -> None: ...
    @overload
    @FileLockingOpenWarning.setter
    def FileLockingOpenWarning(self, value: bool) -> None: ...
    @overload
    @SaveViewChanges.setter
    def SaveViewChanges(self, value: bool) -> None: ...
    @overload
    @TemplateFileDir.setter
    def TemplateFileDir(self, value: str) -> None: ...
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
    def AutoUpdateCommandHelp(value: bool) -> None: ...
    @overload
    @ContextMenuDelay.setter
    def ContextMenuDelay(value: TimeSpan) -> None: ...
    @overload
    @EnableContextMenu.setter
    def EnableContextMenu(value: bool) -> None: ...
    @overload
    @MaximumPopupMenuLines.setter
    def MaximumPopupMenuLines(value: int) -> None: ...
    @overload
    @MaximumUndoMemoryMb.setter
    def MaximumUndoMemoryMb(value: int) -> None: ...
    @overload
    @MiddleMouseMacro.setter
    def MiddleMouseMacro(value: str) -> None: ...
    @overload
    @MiddleMouseMode.setter
    def MiddleMouseMode(value: MiddleMouseMode) -> None: ...
    @overload
    @MiddleMousePopupToolbar.setter
    def MiddleMousePopupToolbar(value: str) -> None: ...
    @overload
    @MinimumUndoSteps.setter
    def MinimumUndoSteps(value: int) -> None: ...
    @overload
    @MouseSelectMode.setter
    def MouseSelectMode(value: MouseSelectMode) -> None: ...
    @overload
    @NewObjectIsoparmCount.setter
    def NewObjectIsoparmCount(value: int) -> None: ...
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
    def AutoUpdateCommandHelp(self, value: bool) -> None: ...
    @overload
    @ContextMenuDelay.setter
    def ContextMenuDelay(self, value: TimeSpan) -> None: ...
    @overload
    @EnableContextMenu.setter
    def EnableContextMenu(self, value: bool) -> None: ...
    @overload
    @MaximumPopupMenuLines.setter
    def MaximumPopupMenuLines(self, value: int) -> None: ...
    @overload
    @MaximumUndoMemoryMb.setter
    def MaximumUndoMemoryMb(self, value: int) -> None: ...
    @overload
    @MiddleMouseMacro.setter
    def MiddleMouseMacro(self, value: str) -> None: ...
    @overload
    @MiddleMouseMode.setter
    def MiddleMouseMode(self, value: MiddleMouseMode) -> None: ...
    @overload
    @MiddleMousePopupToolbar.setter
    def MiddleMousePopupToolbar(self, value: str) -> None: ...
    @overload
    @MinimumUndoSteps.setter
    def MinimumUndoSteps(self, value: int) -> None: ...
    @overload
    @MouseSelectMode.setter
    def MouseSelectMode(self, value: MouseSelectMode) -> None: ...
    @overload
    @NewObjectIsoparmCount.setter
    def NewObjectIsoparmCount(self, value: int) -> None: ...
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
    def RecordNextCommand() -> bool: ...
    @overload
    @property
    def UpdateEnabled() -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @BrokenRecordWarningEnabled.setter
    def BrokenRecordWarningEnabled(value: bool) -> None: ...
    @overload
    @ObjectLockingEnabled.setter
    def ObjectLockingEnabled(value: bool) -> None: ...
    @overload
    @RecordingEnabled.setter
    def RecordingEnabled(value: bool) -> None: ...
    @overload
    @RecordNextCommand.setter
    def RecordNextCommand(value: bool) -> None: ...
    @overload
    @UpdateEnabled.setter
    def UpdateEnabled(value: bool) -> None: ...
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


from ..UI import ModifierKey
from ..UI import KeyboardKey
class KeyboardShortcut:
    @overload
    def __init__(self): ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def Key(self) -> KeyboardKey: ...
    @overload
    @property
    def Macro(self) -> str: ...
    @overload
    @property
    def Modifier(self) -> ModifierKey: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @Key.setter
    def Key(self, value: KeyboardKey) -> None: ...
    @overload
    @Macro.setter
    def Macro(self, value: str) -> None: ...
    @overload
    @Modifier.setter
    def Modifier(self, value: ModifierKey) -> None: ...
    @overload
    def ToString(self) -> str: ...


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
    def AutoAlignCPlane() -> bool: ...
    @overload
    @property
    def AutoCPlaneAlignment() -> int: ...
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
    def GumballAutoReset() -> bool: ...
    @overload
    @property
    def GumballExtrudeMergeFaces() -> bool: ...
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
    def OnlySnapToSelected() -> bool: ...
    @overload
    @property
    def OrientAutoCPlaneToView() -> bool: ...
    @overload
    @property
    def Ortho() -> bool: ...
    @overload
    @property
    def OrthoAngle() -> float: ...
    @overload
    @property
    def OrthoUseZ() -> bool: ...
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
    def SnapToFiltered() -> bool: ...
    @overload
    @property
    def SnapToLocked() -> bool: ...
    @overload
    @property
    def SnapToOccluded() -> bool: ...
    @overload
    @property
    def StickyAutoCPlane() -> bool: ...
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
    def AltPlusArrow(value: bool) -> None: ...
    @overload
    @AutoAlignCPlane.setter
    def AutoAlignCPlane(value: bool) -> None: ...
    @overload
    @AutoCPlaneAlignment.setter
    def AutoCPlaneAlignment(value: int) -> None: ...
    @overload
    @AutoGumballEnabled.setter
    def AutoGumballEnabled(value: bool) -> None: ...
    @overload
    @ControlPolygonDisplayDensity.setter
    def ControlPolygonDisplayDensity(value: int) -> None: ...
    @overload
    @CtrlNudgeKeyStep.setter
    def CtrlNudgeKeyStep(value: float) -> None: ...
    @overload
    @DisplayControlPolygon.setter
    def DisplayControlPolygon(value: bool) -> None: ...
    @overload
    @ExtendToApparentIntersection.setter
    def ExtendToApparentIntersection(value: bool) -> None: ...
    @overload
    @ExtendTrimLines.setter
    def ExtendTrimLines(value: bool) -> None: ...
    @overload
    @GridSnap.setter
    def GridSnap(value: bool) -> None: ...
    @overload
    @GumballAutoReset.setter
    def GumballAutoReset(value: bool) -> None: ...
    @overload
    @GumballExtrudeMergeFaces.setter
    def GumballExtrudeMergeFaces(value: bool) -> None: ...
    @overload
    @HighlightControlPolygon.setter
    def HighlightControlPolygon(value: bool) -> None: ...
    @overload
    @MousePickboxRadius.setter
    def MousePickboxRadius(value: int) -> None: ...
    @overload
    @NudgeKeyStep.setter
    def NudgeKeyStep(value: float) -> None: ...
    @overload
    @NudgeMode.setter
    def NudgeMode(value: int) -> None: ...
    @overload
    @OnlySnapToSelected.setter
    def OnlySnapToSelected(value: bool) -> None: ...
    @overload
    @OrientAutoCPlaneToView.setter
    def OrientAutoCPlaneToView(value: bool) -> None: ...
    @overload
    @Ortho.setter
    def Ortho(value: bool) -> None: ...
    @overload
    @OrthoAngle.setter
    def OrthoAngle(value: float) -> None: ...
    @overload
    @OrthoUseZ.setter
    def OrthoUseZ(value: bool) -> None: ...
    @overload
    @Osnap.setter
    def Osnap(value: bool) -> None: ...
    @overload
    @OsnapCursorMode.setter
    def OsnapCursorMode(value: CursorMode) -> None: ...
    @overload
    @OsnapModes.setter
    def OsnapModes(value: OsnapModes) -> None: ...
    @overload
    @OsnapPickboxRadius.setter
    def OsnapPickboxRadius(value: int) -> None: ...
    @overload
    @Planar.setter
    def Planar(value: bool) -> None: ...
    @overload
    @PointDisplay.setter
    def PointDisplay(value: PointDisplayMode) -> None: ...
    @overload
    @ProjectSnapToCPlane.setter
    def ProjectSnapToCPlane(value: bool) -> None: ...
    @overload
    @ShiftNudgeKeyStep.setter
    def ShiftNudgeKeyStep(value: float) -> None: ...
    @overload
    @SnappyGumballEnabled.setter
    def SnappyGumballEnabled(value: bool) -> None: ...
    @overload
    @SnapToFiltered.setter
    def SnapToFiltered(value: bool) -> None: ...
    @overload
    @SnapToLocked.setter
    def SnapToLocked(value: bool) -> None: ...
    @overload
    @SnapToOccluded.setter
    def SnapToOccluded(value: bool) -> None: ...
    @overload
    @StickyAutoCPlane.setter
    def StickyAutoCPlane(value: bool) -> None: ...
    @overload
    @UniversalConstructionPlaneMode.setter
    def UniversalConstructionPlaneMode(value: bool) -> None: ...
    @overload
    @UseHorizontalDialog.setter
    def UseHorizontalDialog(value: bool) -> None: ...
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
    def AutoAlignCPlane(self) -> bool: ...
    @overload
    @property
    def AutoCPlaneAlignment(self) -> int: ...
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
    def OrientAutoCPlaneToView(self) -> bool: ...
    @overload
    @property
    def Ortho(self) -> bool: ...
    @overload
    @property
    def OrthoAngle(self) -> float: ...
    @overload
    @property
    def OrthoUseZ(self) -> bool: ...
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
    def StickyAutoCPlane(self) -> bool: ...
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
    def AltPlusArrow(self, value: bool) -> None: ...
    @overload
    @AutoAlignCPlane.setter
    def AutoAlignCPlane(self, value: bool) -> None: ...
    @overload
    @AutoCPlaneAlignment.setter
    def AutoCPlaneAlignment(self, value: int) -> None: ...
    @overload
    @ControlPolygonDisplayDensity.setter
    def ControlPolygonDisplayDensity(self, value: int) -> None: ...
    @overload
    @CtrlNudgeKeyStep.setter
    def CtrlNudgeKeyStep(self, value: float) -> None: ...
    @overload
    @DisplayControlPolygon.setter
    def DisplayControlPolygon(self, value: bool) -> None: ...
    @overload
    @ExtendToApparentIntersection.setter
    def ExtendToApparentIntersection(self, value: bool) -> None: ...
    @overload
    @ExtendTrimLines.setter
    def ExtendTrimLines(self, value: bool) -> None: ...
    @overload
    @GridSnap.setter
    def GridSnap(self, value: bool) -> None: ...
    @overload
    @HighlightControlPolygon.setter
    def HighlightControlPolygon(self, value: bool) -> None: ...
    @overload
    @MousePickboxRadius.setter
    def MousePickboxRadius(self, value: int) -> None: ...
    @overload
    @NudgeKeyStep.setter
    def NudgeKeyStep(self, value: float) -> None: ...
    @overload
    @NudgeMode.setter
    def NudgeMode(self, value: int) -> None: ...
    @overload
    @OrientAutoCPlaneToView.setter
    def OrientAutoCPlaneToView(self, value: bool) -> None: ...
    @overload
    @Ortho.setter
    def Ortho(self, value: bool) -> None: ...
    @overload
    @OrthoAngle.setter
    def OrthoAngle(self, value: float) -> None: ...
    @overload
    @OrthoUseZ.setter
    def OrthoUseZ(self, value: bool) -> None: ...
    @overload
    @Osnap.setter
    def Osnap(self, value: bool) -> None: ...
    @overload
    @OsnapCursorMode.setter
    def OsnapCursorMode(self, value: CursorMode) -> None: ...
    @overload
    @OsnapModes.setter
    def OsnapModes(self, value: OsnapModes) -> None: ...
    @overload
    @OsnapPickboxRadius.setter
    def OsnapPickboxRadius(self, value: int) -> None: ...
    @overload
    @Planar.setter
    def Planar(self, value: bool) -> None: ...
    @overload
    @PointDisplay.setter
    def PointDisplay(self, value: PointDisplayMode) -> None: ...
    @overload
    @ProjectSnapToCPlane.setter
    def ProjectSnapToCPlane(self, value: bool) -> None: ...
    @overload
    @ShiftNudgeKeyStep.setter
    def ShiftNudgeKeyStep(self, value: float) -> None: ...
    @overload
    @SnapToLocked.setter
    def SnapToLocked(self, value: bool) -> None: ...
    @overload
    @StickyAutoCPlane.setter
    def StickyAutoCPlane(self, value: bool) -> None: ...
    @overload
    @UniversalConstructionPlaneMode.setter
    def UniversalConstructionPlaneMode(self, value: bool) -> None: ...
    @overload
    @UseHorizontalDialog.setter
    def UseHorizontalDialog(self, value: bool) -> None: ...
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
    def AntialiasLevel(value: AntialiasLevel) -> None: ...
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
    def AntialiasLevel(self, value: AntialiasLevel) -> None: ...
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
    def Sources(value: str) -> None: ...
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
    def Enabled(value: bool) -> None: ...
    @overload
    @GlobalGeometryFilter.setter
    def GlobalGeometryFilter(value: ObjectType) -> None: ...
    @overload
    @OneShotGeometryFilter.setter
    def OneShotGeometryFilter(value: ObjectType) -> None: ...
    @overload
    @SubObjectSelect.setter
    def SubObjectSelect(value: bool) -> None: ...
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
    def Enabled(self, value: bool) -> None: ...
    @overload
    @GlobalGeometryFilter.setter
    def GlobalGeometryFilter(self, value: ObjectType) -> None: ...
    @overload
    @OneShotGeometryFilter.setter
    def OneShotGeometryFilter(self, value: ObjectType) -> None: ...
    @overload
    @SubObjectSelect.setter
    def SubObjectSelect(self, value: bool) -> None: ...
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
    Tab = 166
    PageUp = 167
    PageDown = 168
    ShiftPageUp = 169
    ShiftPageDown = 170
    CtrlPageUp = 171
    CtrlPageDown = 172
    ShiftCtrlPageUp = 173
    ShiftCtrlPageDown = 174
    AltCtrlPageUp = 175
    AltCtrlPageDown = 176
    # None = 177
    AltHome = 178
    AltEnd = 179
    AltA = 180
    AltB = 181
    AltC = 182
    AltD = 183
    AltE = 184
    AltF = 185
    AltG = 186
    AltH = 187
    AltI = 188
    AltJ = 189
    AltK = 190
    AltL = 191
    AltM = 192
    AltN = 193
    AltO = 194
    AltP = 195
    AltQ = 196
    AltR = 197
    AltS = 198
    AltT = 199
    AltU = 200
    AltV = 201
    AltW = 202
    AltX = 203
    AltY = 204
    AltZ = 205
    Alt0 = 206
    Alt1 = 207
    Alt2 = 208
    Alt3 = 209
    Alt4 = 210
    Alt5 = 211
    Alt6 = 212
    Alt7 = 213
    Alt8 = 214
    Alt9 = 215
    AltF1 = 216
    AltF2 = 217
    AltF3 = 218
    AltF4 = 219
    AltF5 = 220
    AltF6 = 221
    AltF7 = 222
    AltF8 = 223
    AltF9 = 224
    AltF10 = 225
    AltF11 = 226
    AltF12 = 227
    AltShiftHome = 228
    AltShiftEnd = 229
    AltShiftA = 230
    AltShiftB = 231
    AltShiftC = 232
    AltShiftD = 233
    AltShiftE = 234
    AltShiftF = 235
    AltShiftG = 236
    AltShiftH = 237
    AltShiftI = 238
    AltShiftJ = 239
    AltShiftK = 240
    AltShiftL = 241
    AltShiftM = 242
    AltShiftN = 243
    AltShiftO = 244
    AltShiftP = 245
    AltShiftQ = 246
    AltShiftR = 247
    AltShiftS = 248
    AltShiftT = 249
    AltShiftU = 250
    AltShiftV = 251
    AltShiftW = 252
    AltShiftX = 253
    AltShiftY = 254
    AltShiftZ = 255
    AltShift0 = 256
    AltShift1 = 257
    AltShift2 = 258
    AltShift3 = 259
    AltShift4 = 260
    AltShift5 = 261
    AltShift6 = 262
    AltShift7 = 263
    AltShift8 = 264
    AltShift9 = 265
    AltShiftF1 = 266
    AltShiftF2 = 267
    AltShiftF3 = 268
    AltShiftF4 = 269
    AltShiftF5 = 270
    AltShiftF6 = 271
    AltShiftF7 = 272
    AltShiftF8 = 273
    AltShiftF9 = 274
    AltShiftF10 = 275
    AltShiftF11 = 276
    AltShiftF12 = 277
    MacControlHome = 278
    MacControlEnd = 279
    MacControlA = 280
    MacControlB = 281
    MacControlC = 282
    MacControlD = 283
    MacControlE = 284
    MacControlF = 285
    MacControlG = 286
    MacControlH = 287
    MacControlI = 288
    MacControlJ = 289
    MacControlK = 290
    MacControlL = 291
    MacControlM = 292
    MacControlN = 293
    MacControlO = 294
    MacControlP = 295
    MacControlQ = 296
    MacControlR = 297
    MacControlS = 298
    MacControlT = 299
    MacControlU = 300
    MacControlV = 301
    MacControlW = 302
    MacControlX = 303
    MacControlY = 304
    MacControlZ = 305
    MacControl0 = 306
    MacControl1 = 307
    MacControl2 = 308
    MacControl3 = 309
    MacControl4 = 310
    MacControl5 = 311
    MacControl6 = 312
    MacControl7 = 313
    MacControl8 = 314
    MacControl9 = 315
    MacControlF1 = 316
    MacControlF2 = 317
    MacControlF3 = 318
    MacControlF4 = 319
    MacControlF5 = 320
    MacControlF6 = 321
    MacControlF7 = 322
    MacControlF8 = 323
    MacControlF9 = 324
    MacControlF10 = 325
    MacControlF11 = 326
    MacControlF12 = 327
    MacControlAltHome = 328
    MacControlAltEnd = 329
    MacControlAltA = 330
    MacControlAltB = 331
    MacControlAltC = 332
    MacControlAltD = 333
    MacControlAltE = 334
    MacControlAltF = 335
    MacControlAltG = 336
    MacControlAltH = 337
    MacControlAltI = 338
    MacControlAltJ = 339
    MacControlAltK = 340
    MacControlAltL = 341
    MacControlAltM = 342
    MacControlAltN = 343
    MacControlAltO = 344
    MacControlAltP = 345
    MacControlAltQ = 346
    MacControlAltR = 347
    MacControlAltS = 348
    MacControlAltT = 349
    MacControlAltU = 350
    MacControlAltV = 351
    MacControlAltW = 352
    MacControlAltX = 353
    MacControlAltY = 354
    MacControlAltZ = 355
    MacControlAlt0 = 356
    MacControlAlt1 = 357
    MacControlAlt2 = 358
    MacControlAlt3 = 359
    MacControlAlt4 = 360
    MacControlAlt5 = 361
    MacControlAlt6 = 362
    MacControlAlt7 = 363
    MacControlAlt8 = 364
    MacControlAlt9 = 365
    MacControlAltF1 = 366
    MacControlAltF2 = 367
    MacControlAltF3 = 368
    MacControlAltF4 = 369
    MacControlAltF5 = 370
    MacControlAltF6 = 371
    MacControlAltF7 = 372
    MacControlAltF8 = 373
    MacControlAltF9 = 374
    MacControlAltF10 = 375
    MacControlAltF11 = 376
    MacControlAltF12 = 377
    MacControlOptionHome = 378
    MacControlOptionEnd = 379
    MacControlOptionA = 380
    MacControlOptionB = 381
    MacControlOptionC = 382
    MacControlOptionD = 383
    MacControlOptionE = 384
    MacControlOptionF = 385
    MacControlOptionG = 386
    MacControlOptionH = 387
    MacControlOptionI = 388
    MacControlOptionJ = 389
    MacControlOptionK = 390
    MacControlOptionL = 391
    MacControlOptionM = 392
    MacControlOptionN = 393
    MacControlOptionO = 394
    MacControlOptionP = 395
    MacControlOptionQ = 396
    MacControlOptionR = 397
    MacControlOptionS = 398
    MacControlOptionT = 399
    MacControlOptionU = 400
    MacControlOptionV = 401
    MacControlOptionW = 402
    MacControlOptionX = 403
    MacControlOptionY = 404
    MacControlOptionZ = 405
    MacControlOption0 = 406
    MacControlOption1 = 407
    MacControlOption2 = 408
    MacControlOption3 = 409
    MacControlOption4 = 410
    MacControlOption5 = 411
    MacControlOption6 = 412
    MacControlOption7 = 413
    MacControlOption8 = 414
    MacControlOption9 = 415
    MacControlOptionF1 = 416
    MacControlOptionF2 = 417
    MacControlOptionF3 = 418
    MacControlOptionF4 = 419
    MacControlOptionF5 = 420
    MacControlOptionF6 = 421
    MacControlOptionF7 = 422
    MacControlOptionF8 = 423
    MacControlOptionF9 = 424
    MacControlOptionF10 = 425
    MacControlOptionF11 = 426
    MacControlOptionF12 = 427
    MacControlShiftHome = 428
    MacControlShiftEnd = 429
    MacControlShiftA = 430
    MacControlShiftB = 431
    MacControlShiftC = 432
    MacControlShiftD = 433
    MacControlShiftE = 434
    MacControlShiftF = 435
    MacControlShiftG = 436
    MacControlShiftH = 437
    MacControlShiftI = 438
    MacControlShiftJ = 439
    MacControlShiftK = 440
    MacControlShiftL = 441
    MacControlShiftM = 442
    MacControlShiftN = 443
    MacControlShiftO = 444
    MacControlShiftP = 445
    MacControlShiftQ = 446
    MacControlShiftR = 447
    MacControlShiftS = 448
    MacControlShiftT = 449
    MacControlShiftU = 450
    MacControlShiftV = 451
    MacControlShiftW = 452
    MacControlShiftX = 453
    MacControlShiftY = 454
    MacControlShiftZ = 455
    MacControlShift0 = 456
    MacControlShift1 = 457
    MacControlShift2 = 458
    MacControlShift3 = 459
    MacControlShift4 = 460
    MacControlShift5 = 461
    MacControlShift6 = 462
    MacControlShift7 = 463
    MacControlShift8 = 464
    MacControlShift9 = 465
    MacControlShiftF1 = 466
    MacControlShiftF2 = 467
    MacControlShiftF3 = 468
    MacControlShiftF4 = 469
    MacControlShiftF5 = 470
    MacControlShiftF6 = 471
    MacControlShiftF7 = 472
    MacControlShiftF8 = 473
    MacControlShiftF9 = 474
    MacControlShiftF10 = 475
    MacControlShiftF11 = 476
    MacControlShiftF12 = 477


from ..UI import KeyboardKey
from ..UI import ModifierKey
class ShortcutKeySettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @staticmethod
    def GetDefaults() -> Iterable[KeyboardShortcut]: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    @staticmethod
    def GetLabel(key: ShortcutKey) -> str: ...
    @overload
    @staticmethod
    def GetMacro(key: ShortcutKey) -> str: ...
    @overload
    @staticmethod
    def GetShortcuts() -> Iterable[KeyboardShortcut]: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def IsAcceptableKeyCombo(key: KeyboardKey, modifier: ModifierKey) -> bool: ...
    @overload
    @staticmethod
    def SetMacro(key: ShortcutKey, macro: str) -> None: ...
    @overload
    @staticmethod
    def SetMacro(key: KeyboardKey, modifier: ModifierKey, macro: str) -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def Update(shortcuts: Iterable[KeyboardShortcut], replaceAll: bool) -> None: ...


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
    def GuideColor() -> Color: ...
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
    def ActivationDelayMilliseconds(value: int) -> None: ...
    @overload
    @ActivePointColor.setter
    def ActivePointColor(value: Color) -> None: ...
    @overload
    @GuideColor.setter
    def GuideColor(value: Color) -> None: ...
    @overload
    @LineColor.setter
    def LineColor(value: Color) -> None: ...
    @overload
    @MaxSmartPoints.setter
    def MaxSmartPoints(value: int) -> None: ...
    @overload
    @PointColor.setter
    def PointColor(value: Color) -> None: ...
    @overload
    @SmartOrtho.setter
    def SmartOrtho(value: bool) -> None: ...
    @overload
    @SmartTangents.setter
    def SmartTangents(value: bool) -> None: ...
    @overload
    @TanPerpLineColor.setter
    def TanPerpLineColor(value: Color) -> None: ...
    @overload
    @UseDottedLines.setter
    def UseDottedLines(value: bool) -> None: ...
    @overload
    @UseSmartTrack.setter
    def UseSmartTrack(value: bool) -> None: ...
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
    def GuideColor(self) -> Color: ...
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
    def ActivationDelayMilliseconds(self, value: int) -> None: ...
    @overload
    @ActivePointColor.setter
    def ActivePointColor(self, value: Color) -> None: ...
    @overload
    @GuideColor.setter
    def GuideColor(self, value: Color) -> None: ...
    @overload
    @LineColor.setter
    def LineColor(self, value: Color) -> None: ...
    @overload
    @MaxSmartPoints.setter
    def MaxSmartPoints(value: int) -> None: ...
    @overload
    @PointColor.setter
    def PointColor(self, value: Color) -> None: ...
    @overload
    @SmartOrtho.setter
    def SmartOrtho(self, value: bool) -> None: ...
    @overload
    @SmartTangents.setter
    def SmartTangents(self, value: bool) -> None: ...
    @overload
    @TanPerpLineColor.setter
    def TanPerpLineColor(self, value: Color) -> None: ...
    @overload
    @UseDottedLines.setter
    def UseDottedLines(self, value: bool) -> None: ...
    @overload
    @UseSmartTrack.setter
    def UseSmartTrack(self, value: bool) -> None: ...
    @overload
    def ToString(self) -> str: ...


class ViewRotationStyle(Enum):
    RotateAroundWorldAxes = 0
    RotateRelativeToView = 1
    RotateRelativeToViewV2Style = 2
    RotateAroundCplaneZaxis = 3


class ViewSettings:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def AlwaysPanParallelViews() -> bool: ...
    @overload
    @property
    def AutoAdjustTargetDepth() -> bool: ...
    @overload
    @property
    def DefinedViewSetClippingPlanes() -> bool: ...
    @overload
    @property
    def DefinedViewSetCPlane() -> bool: ...
    @overload
    @property
    def DefinedViewSetDisplayMode() -> bool: ...
    @overload
    @property
    def DefinedViewSetProjection() -> bool: ...
    @overload
    @property
    def LinkedViewports() -> bool: ...
    @overload
    @property
    def PanPlanParallelViewsWithControlShiftRMB() -> bool: ...
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
    def RotateViewAroundAutogumball() -> bool: ...
    @overload
    @property
    def RotateViewAroundObjectAtMouseCursor() -> bool: ...
    @overload
    @property
    def SingleClickMaximize() -> bool: ...
    @overload
    @property
    def ThreePointPerspectiveLensLength() -> float: ...
    @overload
    @property
    def TwoPointPerspectiveLensLength() -> float: ...
    @overload
    @property
    def ViewRotation() -> ViewRotationStyle: ...
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
    def AlwaysPanParallelViews(value: bool) -> None: ...
    @overload
    @AutoAdjustTargetDepth.setter
    def AutoAdjustTargetDepth(value: bool) -> None: ...
    @overload
    @DefinedViewSetClippingPlanes.setter
    def DefinedViewSetClippingPlanes(value: bool) -> None: ...
    @overload
    @DefinedViewSetCPlane.setter
    def DefinedViewSetCPlane(value: bool) -> None: ...
    @overload
    @DefinedViewSetDisplayMode.setter
    def DefinedViewSetDisplayMode(value: bool) -> None: ...
    @overload
    @DefinedViewSetProjection.setter
    def DefinedViewSetProjection(value: bool) -> None: ...
    @overload
    @LinkedViewports.setter
    def LinkedViewports(value: bool) -> None: ...
    @overload
    @PanPlanParallelViewsWithControlShiftRMB.setter
    def PanPlanParallelViewsWithControlShiftRMB(value: bool) -> None: ...
    @overload
    @PanReverseKeyboardAction.setter
    def PanReverseKeyboardAction(value: bool) -> None: ...
    @overload
    @PanScreenFraction.setter
    def PanScreenFraction(value: float) -> None: ...
    @overload
    @RotateCircleIncrement.setter
    def RotateCircleIncrement(value: int) -> None: ...
    @overload
    @RotateReverseKeyboard.setter
    def RotateReverseKeyboard(value: bool) -> None: ...
    @overload
    @RotateToView.setter
    def RotateToView(value: bool) -> None: ...
    @overload
    @RotateViewAroundAutogumball.setter
    def RotateViewAroundAutogumball(value: bool) -> None: ...
    @overload
    @RotateViewAroundObjectAtMouseCursor.setter
    def RotateViewAroundObjectAtMouseCursor(value: bool) -> None: ...
    @overload
    @SingleClickMaximize.setter
    def SingleClickMaximize(value: bool) -> None: ...
    @overload
    @ViewRotation.setter
    def ViewRotation(value: ViewRotationStyle) -> None: ...
    @overload
    @ZoomExtentsParallelViewBorder.setter
    def ZoomExtentsParallelViewBorder(value: float) -> None: ...
    @overload
    @ZoomExtentsPerspectiveViewBorder.setter
    def ZoomExtentsPerspectiveViewBorder(value: float) -> None: ...
    @overload
    @ZoomScale.setter
    def ZoomScale(value: float) -> None: ...
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
    def ThreePointPerspectiveLensLength(self) -> float: ...
    @overload
    @property
    def TwoPointPerspectiveLensLength(self) -> float: ...
    @overload
    @property
    def ViewRotation(self) -> ViewRotationStyle: ...
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
    def AlwaysPanParallelViews(self, value: bool) -> None: ...
    @overload
    @DefinedViewSetCPlane.setter
    def DefinedViewSetCPlane(self, value: bool) -> None: ...
    @overload
    @DefinedViewSetProjection.setter
    def DefinedViewSetProjection(self, value: bool) -> None: ...
    @overload
    @LinkedViewports.setter
    def LinkedViewports(self, value: bool) -> None: ...
    @overload
    @PanReverseKeyboardAction.setter
    def PanReverseKeyboardAction(self, value: bool) -> None: ...
    @overload
    @PanScreenFraction.setter
    def PanScreenFraction(self, value: float) -> None: ...
    @overload
    @RotateCircleIncrement.setter
    def RotateCircleIncrement(self, value: int) -> None: ...
    @overload
    @RotateReverseKeyboard.setter
    def RotateReverseKeyboard(self, value: bool) -> None: ...
    @overload
    @RotateToView.setter
    def RotateToView(self, value: bool) -> None: ...
    @overload
    @SingleClickMaximize.setter
    def SingleClickMaximize(self, value: bool) -> None: ...
    @overload
    @ViewRotation.setter
    def ViewRotation(self, value: ViewRotationStyle) -> None: ...
    @overload
    @ZoomExtentsParallelViewBorder.setter
    def ZoomExtentsParallelViewBorder(self, value: float) -> None: ...
    @overload
    @ZoomExtentsPerspectiveViewBorder.setter
    def ZoomExtentsPerspectiveViewBorder(self, value: float) -> None: ...
    @overload
    @ZoomScale.setter
    def ZoomScale(self, value: float) -> None: ...
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
    def ShowIsoCurves(value: bool) -> None: ...
    @overload
    @StripeColor.setter
    def StripeColor(value: Color) -> None: ...
    @overload
    @StripeThickness.setter
    def StripeThickness(value: int) -> None: ...
    @overload
    @VerticalStripes.setter
    def VerticalStripes(value: bool) -> None: ...
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
    def ShowIsoCurves(self, value: bool) -> None: ...
    @overload
    @StripeColor.setter
    def StripeColor(self, value: Color) -> None: ...
    @overload
    @StripeThickness.setter
    def StripeThickness(self, value: int) -> None: ...
    @overload
    @VerticalStripes.setter
    def VerticalStripes(self, value: bool) -> None: ...
    @overload
    def ToString(self) -> str: ...
