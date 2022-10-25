from dataclasses import dataclass
from collections import namedtuple
from typing import Any

@dataclass
class DataClassCard:
    rank : str
    suit : str


@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42

obj = WithoutExplicitTypes(1)
print(obj)

queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts)

NamedTupleCard = namedtuple('NamedTupleCard', ('rank', 'suit'))
queen_of_hearts = NamedTupleCard('Q', 'Hearts')
print(queen_of_hearts)