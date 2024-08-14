from typing import overload, Tuple, Iterable, Iterator, Sequence, MutableSequence
from enum import Enum



class IconSize(Enum):
    Large = 0
    Small = 1


from ..Drawing import Icon
class IHandler:
    def GetFileIcon(self, fileName: str, size: IconSize) -> Icon: ...
    def GetStaticIcon(self, type: StaticIconType, size: IconSize) -> Icon: ...


class StaticIconType(Enum):
    OpenDirectory = 0
    CloseDirectory = 1


from ..Drawing import Icon
class SystemIcons:
    def Equals(self, obj: Object) -> bool: ...
    @staticmethod
    def GetFileIcon(fileName: str, size: IconSize) -> Icon: ...
    def GetHashCode(self) -> int: ...
    @staticmethod
    def GetStaticIcon(type: StaticIconType, size: IconSize) -> Icon: ...
    def GetType(self) -> Type: ...
    def ToString(self) -> str: ...
