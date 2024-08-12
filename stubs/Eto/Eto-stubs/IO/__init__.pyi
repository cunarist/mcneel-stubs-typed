from typing import Tuple, Iterable, overload
from enum import Enum



class IconSize(Enum):
    Large = 0
    Small = 1


class IHandler:
    def GetFileIcon(self, fileName: str, size: IconSize) -> Icon: ...
    def GetStaticIcon(self, type: StaticIconType, size: IconSize) -> Icon: ...


class StaticIconType(Enum):
    OpenDirectory = 0
    CloseDirectory = 1


class SystemIcons:
    def GetFileIcon(fileName: str, size: IconSize) -> Icon: ...
    def GetStaticIcon(type: StaticIconType, size: IconSize) -> Icon: ...
