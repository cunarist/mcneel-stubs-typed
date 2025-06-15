from typing import overload, Any
from collections.abc import Iterable, Iterator, Sequence, MutableSequence, Callable
from enum import Enum

from Grasshopper.Kernel.Geometry import Node2List
from Grasshopper.Kernel.Geometry import Plane
from Grasshopper.Kernel.Types import GH_Point
from Rhino.Geometry import Polyline



class Solver:
    @overload
    @staticmethod
    def Compute(nodes: Node2List, hull: MutableSequence[int]) -> bool: ...
    @overload
    @staticmethod
    def ComputeHull(GH_pts: Iterable[GH_Point]) -> Polyline: ...
    @overload
    @staticmethod
    def ComputeHull(pts: Node2List) -> Polyline: ...
    @overload
    @staticmethod
    def ComputeHull(GH_pts: Iterable[GH_Point], plane: Plane) -> tuple[Polyline, Plane]: ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    def ToString(self) -> str: ...
