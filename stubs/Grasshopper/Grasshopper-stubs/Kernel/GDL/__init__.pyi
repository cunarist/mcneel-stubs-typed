from typing import overload, Any, Tuple, Iterable, Iterator, Sequence, MutableSequence
from enum import Enum
from System import *
from System.Drawing import *



class GH_GDLParser:
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    @staticmethod
    def ParseGDL(lines: Iterable[str]) -> Tuple[GH_Document, Iterable[str]]: ...
    @overload
    def ToString(self) -> str: ...
