from dataclasses import dataclass

@dataclass(frozen=True)
class BoolValueObject():
    _value: bool

    @property
    def value(self):
        return self._value