from typing import overload, Any
from collections.abc import Iterable, Iterator, Sequence, MutableSequence, Callable
from enum import Enum

from System import Action
from System import IFormatProvider
from System import IntPtr
from System import TypeCode



class RhinoCore:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, args: Iterable[str]): ...
    @overload
    def __init__(self, args: Iterable[str], windowStyle: WindowStyle): ...
    @overload
    def __init__(self, args: Iterable[str], windowStyle: WindowStyle, hostWnd: IntPtr): ...
    @overload
    def Dispose(self) -> None: ...
    @overload
    def DoEvents(self) -> bool: ...
    @overload
    def DoIdle(self) -> bool: ...
    @overload
    def Equals(self, obj: object) -> bool: ...
    @overload
    def GetHashCode(self) -> int: ...
    @overload
    def GetType(self) -> type: ...
    @overload
    def InvokeInHostContext(self, action: Action) -> None: ...
    @overload
    def InvokeInHostContext(self, func: Callable[..., Any]) -> T: ...
    @overload
    def RaiseIdle(self) -> None: ...
    @overload
    def Run(self) -> int: ...
    @overload
    def ToString(self) -> str: ...


class WindowStyle(Enum):
    Normal = 0
    Hidden = 1
    Minimized = 2
    Maximized = 3
    NoWindow = -1
