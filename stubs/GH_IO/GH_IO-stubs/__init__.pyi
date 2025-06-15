from typing import overload, Tuple, Iterable, Iterator, Sequence, MutableSequence
from enum import Enum

import Serialization
import Types
import UserInterface

__all__ = ['Serialization', 'Types', 'UserInterface']


class Branch(Enum):
    Unset = 0
    Developer = 1
    Trunk = 2
    ReleaseCandidate = 3
    Release = 4


from .Serialization import GH_IWriter
from .Serialization import GH_IReader
class GH_ISerializable:
    @overload
    def Read(self, reader: GH_IReader) -> bool: ...
    @overload
    def Write(self, writer: GH_IWriter) -> bool: ...


class VersionNumber:
    @overload
    def __init__(self, version: Version): ...
    @overload
    def __init__(self, majorVersionNumber: int, minorVersionNumber: int, versionQuartetYyddd: int, versionQuartetHhmmb: int): ...
    @overload
    def __init__(self, major: int, minor: int, time: DateTime, buildBranch: Branch): ...
    @overload
    def CompareTo(self, value: VersionNumber) -> int: ...
    @overload
    def CompareTo(self, value: Object) -> int: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @property
    def BuildBranch(self) -> Branch: ...
    @overload
    @property
    def IsValid(self) -> bool: ...
    @overload
    @property
    def Major(self) -> int: ...
    @overload
    @property
    def MaxMajorVersionNumber() -> int: ...
    @overload
    @property
    def MaxMinorVersionNumber() -> int: ...
    @overload
    @property
    def MaxValid() -> VersionNumber: ...
    @overload
    @property
    def MaxValidBuildBranch() -> Branch: ...
    @overload
    @property
    def MaxValidTime() -> DateTime: ...
    @overload
    @property
    def MinMajorVersionNumber() -> int: ...
    @overload
    @property
    def MinMinorVersionNumber() -> int: ...
    @overload
    @property
    def Minor(self) -> int: ...
    @overload
    @property
    def MinValid() -> VersionNumber: ...
    @overload
    @property
    def MinValidBuildBranch() -> Branch: ...
    @overload
    @property
    def MinValidTime() -> DateTime: ...
    @overload
    @property
    def Time(self) -> DateTime: ...
    @overload
    @property
    def Unset() -> VersionNumber: ...
    @overload
    @property
    def UnsetBuildBranch() -> Branch: ...
    @overload
    @property
    def UnsetTime() -> DateTime: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    def ToVersion(self) -> Version: ...
    @overload
    @staticmethod
    def TryParse(s: str) -> Tuple[bool, VersionNumber]: ...
    @overload
    @staticmethod
    def TryParse(v: Version) -> Tuple[bool, VersionNumber]: ...
