from typing import overload, Any, Tuple, Iterable, Iterator, Sequence, MutableSequence
from enum import Enum









from Rhino.Geometry import Point
from Rhino.Geometry import Point3d
from Rhino.Geometry import Point2d
from Grasshopper.Kernel.Geometry import Node3
from Grasshopper.Kernel.Geometry import Node2
class TreeDelegates:
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    @staticmethod
    def Node2Coordinates(pt: Node2, x: float, y: float, z: float) -> Tuple[float, float, float]: ...
    @overload
    @staticmethod
    def Node3Coordinates(pt: Node3, x: float, y: float, z: float) -> Tuple[float, float, float]: ...
    @overload
    @staticmethod
    def Point2dCoordinates(pt: Point2d, x: float, y: float, z: float) -> Tuple[float, float, float]: ...
    @overload
    @staticmethod
    def Point2fCoordinates(pt: Point2d, x: float, y: float, z: float) -> Tuple[float, float, float]: ...
    @overload
    @staticmethod
    def Point3dCoordinates(pt: Point3d, x: float, y: float, z: float) -> Tuple[float, float, float]: ...
    @overload
    @staticmethod
    def Point3fCoordinates(pt: Point3d, x: float, y: float, z: float) -> Tuple[float, float, float]: ...
    @overload
    @staticmethod
    def PointCoordinates(pt: Point, x: float, y: float, z: float) -> Tuple[float, float, float]: ...
    @overload
    def ToString(self) -> str: ...


