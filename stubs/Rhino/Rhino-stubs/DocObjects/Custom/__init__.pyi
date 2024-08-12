from typing import Tuple, Set, Iterable, List, overload
from enum import Enum



class ClassIdAttribute:
    def __init__(self, id: str): ...
    @property
    def Id(self) -> Guid: ...


from ...Geometry import ComponentIndex
from ...Display import VisualAnalysisMode
from ...FileIO import TextLog
from ...Geometry import MeshType
from ...Geometry import MeshingParameters
from ...UI.Gumball import GumballFrame
from ...Display import DisplayPipelineAttributes
from ...Geometry import BoundingBox
from ...Geometry import Transform
from ...Render import TextureMapping
from ...Render import RenderMaterial
from ...Display import RhinoViewport
from ...Geometry import ComponentStatus
from ...FileIO import SerializationOptions
class CustomBrepObject(BrepObject):
    pass


from ...Geometry import ComponentIndex
from ...Display import VisualAnalysisMode
from ...FileIO import TextLog
from ...Geometry import MeshType
from ...Geometry import MeshingParameters
from ...UI.Gumball import GumballFrame
from ...Display import DisplayPipelineAttributes
from ...Geometry import BoundingBox
from ...Geometry import Transform
from ...Render import TextureMapping
from ...Render import RenderMaterial
from ...Display import RhinoViewport
from ...Geometry import ComponentStatus
from ...FileIO import SerializationOptions
class CustomCurveObject(CurveObject):
    @overload
    def Dispose(self) -> None: ...


from ...Geometry import Point3d
from ...Geometry import Transform
from ...Geometry import Vector3d
from ...Geometry import ComponentIndex
from ...Display import VisualAnalysisMode
from ...FileIO import TextLog
from ...Geometry import MeshType
from ...Geometry import MeshingParameters
from ...UI.Gumball import GumballFrame
from ...Display import DisplayPipelineAttributes
from ...Geometry import BoundingBox
from ...Render import TextureMapping
from ...Render import RenderMaterial
from ...Display import RhinoViewport
from ...Geometry import ComponentStatus
from ...FileIO import SerializationOptions
class CustomGripObject(GripObject):
    def __init__(self): ...
    @overload
    def Dispose(self) -> None: ...
    @property
    def Index(self) -> int: ...
    @property
    def OriginalLocation(self) -> Point3d: ...
    @property
    def Weight(self) -> float: ...
    def NewLocation(self) -> None: ...
    @Index.setter
    def Index(self, value: int) -> None: ...
    @OriginalLocation.setter
    def OriginalLocation(self, value: Point3d) -> None: ...
    @Weight.setter
    def Weight(self, value: float) -> None: ...


from ...Geometry import ComponentIndex
from ...Display import VisualAnalysisMode
from ...FileIO import TextLog
from ...Geometry import MeshType
from ...Geometry import MeshingParameters
from ...UI.Gumball import GumballFrame
from ...Display import DisplayPipelineAttributes
from ...Geometry import BoundingBox
from ...Geometry import Transform
from ...Render import TextureMapping
from ...Render import RenderMaterial
from ...Display import RhinoViewport
from ...Geometry import ComponentStatus
from ...FileIO import SerializationOptions
class CustomMeshObject(MeshObject):
    @overload
    def Dispose(self) -> None: ...


class CustomObjectGrips:
    def Dispose(self) -> None: ...
    def Dragging() -> bool: ...
    @property
    def GripCount(self) -> int: ...
    @property
    def GripsMoved(self) -> bool: ...
    @property
    def NewLocation(self) -> bool: ...
    @property
    def OwnerObject(self) -> RhinoObject: ...
    def Grip(self, index: int) -> CustomGripObject: ...
    def RegisterGripsEnabler(enabler: TurnOnGripsEventHandler, customGripsType: Type) -> None: ...
    @NewLocation.setter
    def NewLocation(self, value: bool) -> None: ...


from ...Geometry import ComponentIndex
from ...Display import VisualAnalysisMode
from ...FileIO import TextLog
from ...Geometry import MeshType
from ...Geometry import MeshingParameters
from ...UI.Gumball import GumballFrame
from ...Display import DisplayPipelineAttributes
from ...Geometry import BoundingBox
from ...Geometry import Transform
from ...Render import TextureMapping
from ...Render import RenderMaterial
from ...Display import RhinoViewport
from ...Geometry import ComponentStatus
from ...FileIO import SerializationOptions
class CustomPointObject(PointObject):
    @overload
    def Dispose(self) -> None: ...


from ...Geometry import Line
from ...Geometry import Point3d
from ...Display import DrawEventArgs
class GripsDrawEventArgs(DrawEventArgs):
    @overload
    def DrawControlPolygonLine(self, line: Line, startStatus: GripStatus, endStatus: GripStatus) -> None: ...
    @overload
    def DrawControlPolygonLine(self, line: Line, startStatus: int, endStatus: int) -> None: ...
    @overload
    def DrawControlPolygonLine(self, start: Point3d, end: Point3d, startStatus: int, endStatus: int) -> None: ...
    @property
    def ControlPolygonStyle(self) -> int: ...
    @property
    def DrawDynamicStuff(self) -> bool: ...
    @property
    def DrawStaticStuff(self) -> bool: ...
    @property
    def GripColor(self) -> Color: ...
    @property
    def GripStatusCount(self) -> int: ...
    @property
    def LockedGripColor(self) -> Color: ...
    @property
    def SelectedGripColor(self) -> Color: ...
    def GripStatus(self, index: int) -> GripStatus: ...
    def RestoreViewportSettings(self) -> None: ...
    @ControlPolygonStyle.setter
    def ControlPolygonStyle(self, value: int) -> None: ...
    @GripColor.setter
    def GripColor(self, value: Color) -> None: ...
    @LockedGripColor.setter
    def LockedGripColor(self, value: Color) -> None: ...
    @SelectedGripColor.setter
    def SelectedGripColor(self, value: Color) -> None: ...


class GripStatus:
    @property
    def Culled(self) -> bool: ...
    @property
    def Visible(self) -> bool: ...
    @Culled.setter
    def Culled(self, value: bool) -> None: ...


class TurnOnGripsEventHandler:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, rhObj: RhinoObject, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, rhObj: RhinoObject) -> None: ...


class UnknownUserData(UserData):
    def __init__(self, pointerNativeUserData: IntPtr): ...


from ...Runtime import CommonObject
class UserData:
    def Copy(source: CommonObject, destination: CommonObject) -> None: ...
    def Dispose(self) -> None: ...
    @property
    def Description(self) -> str: ...
    @property
    def ShouldWrite(self) -> bool: ...
    @property
    def Transform(self) -> Transform: ...
    def MoveUserDataFrom(objectWithUserData: CommonObject) -> Guid: ...
    def MoveUserDataTo(objectToGetUserData: CommonObject, id: Guid, append: bool) -> None: ...


class UserDataList:
    def Add(self, userdata: UserData) -> bool: ...
    def Contains(self, userdataId: Guid) -> bool: ...
    def Find(self, userdataType: Type) -> UserData: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> UserData: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Purge(self) -> None: ...
    def Remove(self, userdata: UserData) -> bool: ...


class UserDataListEnumerator:
    def __init__(self, udl: UserDataList): ...
    def Dispose(self) -> None: ...
    @property
    def Current(self) -> UserData: ...
    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...


class UserDictionary(UserData):
    def __init__(self): ...
    @property
    def Description(self) -> str: ...
    @property
    def Dictionary(self) -> ArchivableDictionary: ...
    @property
    def ShouldWrite(self) -> bool: ...
