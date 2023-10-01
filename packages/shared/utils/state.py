import copy
from typing import Any, Callable, Generic, List, Protocol, TypeVar, Awaitable

T = TypeVar('T')
P = TypeVar('P')


class UseState(Generic[T]):
    def __init__(self, defaultValue: T) -> None:
        self.value = defaultValue
        self.observers: List[Callable[[T, T], Awaitable[None]]] = []
    
    def bind(self, observer: Callable[[T, T], Awaitable[None]]):
        self.observers.append(observer)
    
    async def set(self, value: T):
        prevent_value = list(self.value) if isinstance(self.value, list) else copy.deepcopy(self.value)
        self.value = value
        for observer in self.observers:
            await observer(prevent_value, value)

    async def get(self) -> T:
        return self.value