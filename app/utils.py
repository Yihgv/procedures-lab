"""
Utility procedures student implement and test.
"""

# This import is important later to understand what's going on
from typing import Dict, Optional

def add(a: float, b: float) -> float:
    """
    Return a + b.
    """
    # TODO: Implement
    raise NotImplementedError

def fib(n: int) -> int:
    """
    Return the n-th Fibonacci number with fib(0) == 0, fib(1) == 1.
    """
    # TODO: implement
    raise NotImplementedError

"""
Simple "database"
Hi again! We imported `typing.Dict` because it's more readable type wise.
That is, so you can tell what we types of variables (string, integer, etc.) we want to use in our dictionary.
"""
_DB: Dict[str, Dict] = {}

def create_item(key: str, value: Dict) -> None:
    """
    Create or replace an item at key with value.
    """
    # TODO: implement
    raise NotImplementedError

def read_item(key: str) -> Optional[Dict]:
    """
    Return the stored value or None if missing.
    """
    # TODO: implement
    raise NotImplementedError

def update_item(key: str, patch: Dict) -> bool:
    """
    Update a stored dictionary item with the keys/values from path.
    Return True if item exists and was updated, False if item missing.
    """
    # TODO: implement
    raise NotImplementedError

def delete_item(key: str) -> bool:
    """
    Delete item at key. Return True if deleted, False if item missing.
    """
    # TODO: implement
    raise NotImplementedError

def clear_db() -> None:
    """Helper for tests (remove all items)."""
    global _DB
    _DB = {}
from typing import Dict, Optional

_DB: Dict[str, Dict] = {}

def add(a: float, b: float) -> float:
    """Return the sum of two float arguments."""
    return a + b

def fib(n: int) -> int:
    """Return the n-th Fibonacci number with fib(0) == 0, fib(1) == 1."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def create_item(key: str, value: Dict) -> None:
    """Store a copy of value under key. Replacing existing value is fine."""
    _DB[key] = value.copy()

def read_item(key: str) -> Optional[Dict]:
    """Return a copy of the stored dict or None if absent."""
    if key in _DB:
        return _DB[key].copy()
    return None

def update_item(key: str, patch: Dict) -> bool:
    """If the key exists, merge patch into the stored dict and return True. If key missing, return False."""
    if key in _DB:
        _DB[key].update(patch)
        return True
    return False

def delete_item(key: str) -> bool:
    """Delete the key if present; return True if deleted, False otherwise."""
    if key in _DB:
        del _DB[key]
        return True
    return False

def clear_db():
    """Clear the database (for tests)."""
    _DB.clear()