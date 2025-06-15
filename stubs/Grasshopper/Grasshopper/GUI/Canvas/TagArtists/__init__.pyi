from typing import overload, Any, Iterable, Iterator, Sequence, MutableSequence, Callable
from enum import Enum



from System import Guid
from Grasshopper.GUI.Canvas import GH_Canvas
from Grasshopper.GUI.Canvas import GH_CanvasChannel
class GH_TagArtist:
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def ID(self) -> Guid: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    def Paint(self, canvas: GH_Canvas, channel: GH_CanvasChannel) -> None: ...
    @overload
    def ToString(self) -> str: ...


from Grasshopper.Kernel import IGH_Param
from System.Drawing import Color
from System import Guid
from Grasshopper.GUI.Canvas import GH_Canvas
from Grasshopper.GUI.Canvas import GH_CanvasChannel
class GH_TagArtist_WirePainter(GH_TagArtist):
    @overload
    def __init__(self, source: IGH_Param, target: IGH_Param, colour: Color, width: int): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def ID(self) -> Guid: ...
    @property
    @classmethod
    def WirePainter_ID(cls) -> Guid: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    def Paint(self, canvas: GH_Canvas, channel: GH_CanvasChannel) -> None: ...
    @overload
    def ToString(self) -> str: ...


from System import Guid
from Grasshopper.GUI.Canvas import GH_Canvas
from Grasshopper.GUI.Canvas import GH_CanvasChannel
class IGH_TagArtist:
    @property
    def ID(self) -> Guid: ...
    @overload
    def Paint(self, canvas: GH_Canvas, channel: GH_CanvasChannel) -> None: ...
