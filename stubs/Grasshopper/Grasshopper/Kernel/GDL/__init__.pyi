from typing import overload, Any, Iterable, Iterator, Sequence, MutableSequence, Callable
from enum import Enum



from Grasshopper.Kernel import GH_Document
class GH_GDLParser:
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    @staticmethod
    def ParseGDL(lines: Iterable[str]) -> tuple[GH_Document, Iterable[str]]: ...
    @overload
    def ToString(self) -> str: ...
