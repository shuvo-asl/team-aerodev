from __future__ import annotations

from occdocs.generators.base import Generator

_REGISTRY: dict[str, type[Generator]] = {}


def register(cls: type[Generator]) -> type[Generator]:
    _REGISTRY[cls.key] = cls
    return cls


def get_generator(key: str) -> Generator:
    try:
        return _REGISTRY[key]()
    except KeyError:
        available = ", ".join(sorted(_REGISTRY)) or "(none registered)"
        raise KeyError(f"No generator named '{key}'. Available: {available}") from None


def available_generators() -> list[str]:
    return sorted(_REGISTRY)
