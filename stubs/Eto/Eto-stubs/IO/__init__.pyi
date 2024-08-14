from typing import overload, Tuple, Iterable, Iterator, Sequence, MutableSequence
from enum import Enum



class IconSize(Enum):
    Large = 0
    Small = 1


from ..Drawing import Icon
class IHandler:
    @overload
    def GetFileIcon(self, fileName: str, size: IconSize) -> Icon: ...
    @overload
    def GetStaticIcon(self, type: StaticIconType, size: IconSize) -> Icon: ...


class StaticIconType(Enum):
    OpenDirectory = 0
    CloseDirectory = 1


from ..Drawing import Icon
class SystemIcons:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    @staticmethod
    def GetFileIcon(fileName: str, size: IconSize) -> Icon: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    @staticmethod
    def GetStaticIcon(type: StaticIconType, size: IconSize) -> Icon: ...
    @overload
    def GetType(self) -> Type: ...
    @overload
    def ToString(self) -> str: ...
