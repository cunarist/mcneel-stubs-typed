from typing import overload, Any, Tuple, Iterable, Iterator, Sequence, MutableSequence
from enum import Enum
from System import *
from System.Drawing import *



class CreaseEdges(Enum):
    NakedFixed = 0
    NakedSmooth = 1
    CornerFixedOtherCreased = 2
    Auto = 3


class LoopFormula(Enum):
    Loop = 0
    Warren = 1
    WarrenWeimer = 2


class RefinementSettings:
    @overload
    def __init__(self): ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def ContinueRequest(self) -> CancellationToken: ...
    @property
    def HasPull(self) -> bool: ...
    @property
    def Level(self) -> int: ...
    @property
    def NakedEdgeMode(self) -> CreaseEdges: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @ContinueRequest.setter
    def ContinueRequest(self, value: CancellationToken) -> None: ...
    @Level.setter
    def Level(self, value: int) -> None: ...
    @NakedEdgeMode.setter
    def NakedEdgeMode(self, value: CreaseEdges) -> None: ...
    @overload
    def ToString(self) -> str: ...
