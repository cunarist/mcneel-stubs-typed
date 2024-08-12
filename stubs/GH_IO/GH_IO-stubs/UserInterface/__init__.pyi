from typing import Tuple, Iterable, overload
from enum import Enum



from ..Serialization import GH_Archive
class GH_ArchiveMessageViewer:
    def __init__(self): ...
    def SetArchive(self, nArchive: GH_Archive) -> None: ...


class GH_DeveloperDetails:
    @property
    def DefaultDeveloperContact() -> str: ...
    @property
    def DeveloperContact() -> str: ...
    @DeveloperContact.setter
    def DeveloperContact(value: str) -> None: ...
