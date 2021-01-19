import attr
from functools import partial, wraps
from typing import Callable, List

from .fields_converter import fields_converter
from .serializer import serializer


def _frozen(_, __, ___):
    """
    Prevent an attribute to be modified.

    .. versionadded:: 20.1.0
    """
    raise attr.exceptions.FrozenAttributeError()


asdict = wraps(attr.asdict)(
    partial(
        attr.asdict,
        value_serializer=serializer,
    )
)
dataclass = wraps(attr.attrs)(
    partial(
        attr.attrs,
        auto_attribs=True,
        field_transformer=fields_converter,
        kw_only=True,
    )
)
sdataclass = wraps(attr.attrs)(
    partial(
        attr.attrs,
        auto_attribs=True,
        field_transformer=fields_converter,
        slots=True,
        kw_only=True,
    )
)
field = attr.attrib
freeze = wraps(field)(partial(field, on_setattr=_frozen))


def fields(converter: Callable, **kwargs):
    def conv(d: List[dict]):
        results: List = list()
        if not isinstance(d, list):
            return results
        for result in results:
            results.append(converter(**result))
        return results

    return field(converter=conv, factory=list, **kwargs)