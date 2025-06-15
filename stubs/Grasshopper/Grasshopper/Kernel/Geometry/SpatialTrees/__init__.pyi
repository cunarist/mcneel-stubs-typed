from typing import overload, Any, Iterable, Iterator, Sequence, MutableSequence, Callable
from enum import Enum

from Grasshopper.Kernel.Geometry import Node2
from Grasshopper.Kernel.Geometry import Node3
from Rhino import RhinoDoc
from Rhino.Geometry import BoundingBox
from Rhino.Geometry import Point
from Rhino.Geometry import Point2d
from Rhino.Geometry import Point3d
from System import AsyncCallback
from System import IAsyncResult
from System import IntPtr
from System.Reflection import MethodInfo
from System.Runtime.Serialization import SerializationInfo
from System.Runtime.Serialization import StreamingContext










class TreeDelegates:
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    @staticmethod
    def Node2Coordinates(pt: Node2, x: float, y: float, z: float) -> tuple[float, float, float]: ...
    @overload
    @staticmethod
    def Node3Coordinates(pt: Node3, x: float, y: float, z: float) -> tuple[float, float, float]: ...
    @overload
    @staticmethod
    def Point2dCoordinates(pt: Point2d, x: float, y: float, z: float) -> tuple[float, float, float]: ...
    @overload
    @staticmethod
    def Point2fCoordinates(pt: Point2d, x: float, y: float, z: float) -> tuple[float, float, float]: ...
    @overload
    @staticmethod
    def Point3dCoordinates(pt: Point3d, x: float, y: float, z: float) -> tuple[float, float, float]: ...
    @overload
    @staticmethod
    def Point3fCoordinates(pt: Point3d, x: float, y: float, z: float) -> tuple[float, float, float]: ...
    @overload
    @staticmethod
    def PointCoordinates(pt: Point, x: float, y: float, z: float) -> tuple[float, float, float]: ...
    @overload
    def ToString(self) -> str: ...


