from typing import Any, TypeVar


async def common_elements(list1: list[dict[str, Any]], list2: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    list1_keys = [item1[key] for item1 in list1]
    difference_elements = [
        item2
        for item2 in list2
        if item2[key] not in list1_keys
    ]
    return difference_elements