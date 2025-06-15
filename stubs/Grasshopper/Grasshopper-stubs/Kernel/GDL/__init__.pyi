from typing import overload, Tuple, Iterable, Iterator, Sequence, MutableSequence
from enum import Enum



class GH_GDLParser:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    @staticmethod
    def ParseGDL(lines: Iterable[str]) -> Tuple[GH_Document, Iterable[str]]: ...
    @overload
    def ToString(self) -> str: ...
