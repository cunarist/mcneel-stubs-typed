from typing import overload, Tuple, Iterable, Iterator, Sequence, MutableSequence
from enum import Enum



class GH_Align(Enum):
    # None = 0
    Left = 1
    Right = 2
    Top = 3
    Bottom = 4
    Vertical = 5
    Horizontal = 6


class GH_Distribute(Enum):
    # None = 0
    Vertical = 1
    Horizontal = 2


class GH_Solver:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, boxes: Iterable[RectangleF]): ...
    @overload
    def AddBox(self, box: RectangleF) -> None: ...
    @overload
    @staticmethod
    def Align_Bottom(region: RectangleF, boxes: List) -> List: ...
    @overload
    @staticmethod
    def Align_Horizontal(region: RectangleF, boxes: List) -> List: ...
    @overload
    @staticmethod
    def Align_Left(region: RectangleF, boxes: List) -> List: ...
    @overload
    @staticmethod
    def Align_Right(region: RectangleF, boxes: List) -> List: ...
    @overload
    @staticmethod
    def Align_Top(region: RectangleF, boxes: List) -> List: ...
    @overload
    @staticmethod
    def Align_Vertical(region: RectangleF, boxes: List) -> List: ...
    @overload
    def CreateAutoRegion(self) -> None: ...
    @overload
    @staticmethod
    def Distribute_Horizontal(region: RectangleF, boxes: List) -> List: ...
    @overload
    @staticmethod
    def Distribute_Vertical(region: RectangleF, boxes: List) -> List: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def Region(self) -> RectangleF: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    def Inflate(self, x: Single, y: Single) -> None: ...
    @overload
    @Region.setter
    def Region(self, Value: RectangleF) -> None: ...
    @overload
    def Solve(self, align: GH_Align, distribute: GH_Distribute) -> List: ...
    @overload
    def ToString(self) -> str: ...
