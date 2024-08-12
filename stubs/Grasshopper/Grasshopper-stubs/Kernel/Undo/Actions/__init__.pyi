from typing import Tuple, Iterable, overload
from enum import Enum



from .. import IGH_DocumentObject
from .. import GH_Document
class GH_AddObjectAction(GH_UndoAction):
    def __init__(self, obj: IGH_DocumentObject): ...
    @property
    def ExpiresSolution(self) -> bool: ...


from .. import GH_State
from .. import GH_Document
class GH_AddStateAction(GH_ArchivedUndoAction):
    def __init__(self, index: int, state: GH_State): ...
    def Read(self, reader: GH_IReader) -> bool: ...
    def Write(self, writer: GH_IWriter) -> bool: ...


from .. import IGH_Component
from .. import GH_Document
class GH_DataMatchingAction(GH_ObjectUndoAction):
    def __init__(self, obj: IGH_Component): ...
    @property
    def ExpiresSolution(self) -> bool: ...


from .. import IGH_Param
from .. import GH_Document
class GH_DataModificationAction(GH_ObjectUndoAction):
    def __init__(self, obj: IGH_Param): ...
    @property
    def ExpiresSolution(self) -> bool: ...


from .. import IGH_DocumentObject
from .. import GH_Document
class GH_GenericObjectAction(GH_ArchivedUndoAction):
    def __init__(self, obj: IGH_DocumentObject): ...
    @property
    def ExpiresSolution(self) -> bool: ...


from .. import IGH_ActiveObject
from .. import GH_Document
class GH_HiddenAction(GH_ObjectUndoAction):
    def __init__(self, obj: IGH_ActiveObject): ...
    @property
    def ExpiresDisplay(self) -> bool: ...


from .. import IGH_DocumentObject
from .. import GH_Document
class GH_IconDisplayAction(GH_ObjectUndoAction):
    def __init__(self, obj: IGH_DocumentObject): ...


from .. import IGH_DocumentObject
from .. import GH_Document
class GH_IconOverrideAction(GH_ObjectUndoAction):
    def __init__(self, obj: IGH_DocumentObject): ...


from .. import IGH_DocumentObject
from .. import GH_Document
class GH_LayoutAction(GH_ObjectUndoAction):
    def __init__(self, obj: IGH_DocumentObject): ...


from .. import IGH_ActiveObject
from .. import GH_Document
class GH_LockedAction(GH_ObjectUndoAction):
    def __init__(self, obj: IGH_ActiveObject): ...
    @property
    def ExpiresSolution(self) -> bool: ...


from .. import IGH_DocumentObject
from .. import GH_Document
class GH_NickNameAction(GH_ObjectUndoAction):
    def __init__(self, obj: IGH_DocumentObject): ...




from .. import IGH_DocumentObject
from .. import GH_Document
class GH_PivotAction(GH_ObjectUndoAction):
    def __init__(self, obj: IGH_DocumentObject): ...


from .. import IGH_DocumentObject
from .. import GH_Document
class GH_RemoveObjectAction(GH_ArchivedUndoAction):
    def __init__(self, obj: IGH_DocumentObject): ...
    @property
    def ExpiresSolution(self) -> bool: ...


from .. import GH_State
from .. import GH_Document
class GH_RemoveStateAction(GH_ArchivedUndoAction):
    def __init__(self, index: int, state: GH_State): ...
    def Read(self, reader: GH_IReader) -> bool: ...
    def Write(self, writer: GH_IWriter) -> bool: ...


from .. import IGH_Param
from .. import GH_Document
class GH_WireAction(GH_UndoAction):
    def __init__(self, param: IGH_Param): ...
    @property
    def ExpiresSolution(self) -> bool: ...


from .. import IGH_Param
from .. import GH_Document
class GH_WireDisplayAction(GH_ObjectUndoAction):
    def __init__(self, obj: IGH_Param): ...
