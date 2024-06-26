"""
This type stub file was generated by pyright.
"""

from collections.abc import Iterator

from .iso639 import Lang

Lang = ...

def iter_langs() -> Iterator[Lang]:
    """Iterate through all not deprecated ISO 639 languages

    Yields
    -------
    Lang
        Lang instances ordered alphabetically by name
    """
    ...
