from typing import overload, Any, Iterable, Iterator, Sequence, MutableSequence, Callable
from enum import Enum

from GH_IO.Serialization import GH_IReader
from GH_IO.Serialization import GH_IWriter
from System import DateTime
from System import IFormatProvider
from System import TypeCode
from System import Version

from . import Serialization
from . import Types
from . import UserInterface

__all__ = ['Serialization', 'Types', 'UserInterface']



class Branch(Enum):
    Unset = 0
    Developer = 1
    Trunk = 2
    ReleaseCandidate = 3
    Release = 4


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
    def CompareTo(self, value: object) -> int: ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @property
    def BuildBranch(self) -> Branch: ...
    @property
    def IsValid(self) -> bool: ...
    @property
    def Major(self) -> int: ...
    @property
    @classmethod
    def MaxMajorVersionNumber(cls) -> int: ...
    @property
    @classmethod
    def MaxMinorVersionNumber(cls) -> int: ...
    @property
    @classmethod
    def MaxValid(cls) -> VersionNumber: ...
    @property
    @classmethod
    def MaxValidBuildBranch(cls) -> Branch: ...
    @property
    @classmethod
    def MaxValidTime(cls) -> DateTime: ...
    @property
    @classmethod
    def MinMajorVersionNumber(cls) -> int: ...
    @property
    @classmethod
    def MinMinorVersionNumber(cls) -> int: ...
    @property
    def Minor(self) -> int: ...
    @property
    @classmethod
    def MinValid(cls) -> VersionNumber: ...
    @property
    @classmethod
    def MinValidBuildBranch(cls) -> Branch: ...
    @property
    @classmethod
    def MinValidTime(cls) -> DateTime: ...
    @property
    def Time(self) -> DateTime: ...
    @property
    @classmethod
    def Unset(cls) -> VersionNumber: ...
    @property
    @classmethod
    def UnsetBuildBranch(cls) -> Branch: ...
    @property
    @classmethod
    def UnsetTime(cls) -> DateTime: ...
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
    def TryParse(s: str) -> tuple[bool, VersionNumber]: ...
    @overload
    @staticmethod
    def TryParse(v: Version) -> tuple[bool, VersionNumber]: ...
