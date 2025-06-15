from typing import overload, Tuple, Iterable, Iterator, Sequence, MutableSequence
from enum import Enum



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
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def ContinueRequest(self) -> CancellationToken: ...
    @overload
    @property
    def HasPull(self) -> bool: ...
    @overload
    @property
    def Level(self) -> int: ...
    @overload
    @property
    def NakedEdgeMode(self) -> CreaseEdges: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    @ContinueRequest.setter
    def ContinueRequest(self, value: CancellationToken) -> None: ...
    @overload
    @Level.setter
    def Level(self, value: int) -> None: ...
    @overload
    @NakedEdgeMode.setter
    def NakedEdgeMode(self, value: CreaseEdges) -> None: ...
    @overload
    def ToString(self) -> str: ...
