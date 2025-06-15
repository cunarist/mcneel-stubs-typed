from typing import overload, Any
from collections.abc import Iterable, Iterator, Sequence, MutableSequence, Callable
from enum import Enum

from System.Drawing import Rectangle



class GH_GenericLayout:
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    @staticmethod
    def Horizontal_ByIndex(area: Rectangle, stack: MutableSequence[Rectangle], expand: bool) -> MutableSequence[Rectangle]: ...
    @overload
    @staticmethod
    def Horizontal_ByPosition(area: Rectangle, stack: MutableSequence[Rectangle], expand: bool) -> MutableSequence[Rectangle]: ...
    @overload
    @staticmethod
    def Horizontal_ByPosition(area: Rectangle, stack: MutableSequence[Rectangle], expand: bool, radical: int) -> MutableSequence[Rectangle]: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    @staticmethod
    def Vertical_ByIndex(area: Rectangle, stack: MutableSequence[Rectangle], expand: bool) -> MutableSequence[Rectangle]: ...
    @overload
    @staticmethod
    def Vertical_ByPosition(area: Rectangle, stack: MutableSequence[Rectangle], expand: bool) -> MutableSequence[Rectangle]: ...
    @overload
    @staticmethod
    def Vertical_ByPosition(area: Rectangle, stack: MutableSequence[Rectangle], expand: bool, radical: int) -> MutableSequence[Rectangle]: ...
