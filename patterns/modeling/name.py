from dataclasses import dataclass
from typing import NamedTuple
from collections import namedtuple
import pytest 


@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str

class Money(NamedTuple):
    currency: str
    value: int

class Person:
    """persistent identity"""
    def __init__(self, name: Name):
        self.name = name

Line = namedtuple('Line', ['sku', 'qty'])

def test_equality():
    assert Money('gdp', 10) == Money('gdp', 10)
    assert Money('Harry', 'Percival') != Name('Bob', 'Gregory')
    assert Line('RED-CHAIR', 5) == Line('RED-CHAIR', 5)

def test_name_equality():
    assert Name("Harry", "Percival") != Name("Barry", "Percival")

# math operators
fiver = Money('gdp', 5)
tenner = Money('gdp', 10)

def can_add_values_for_the_same_currency():
    assert fiver + fiver == tenner

def can_subtract_money_values():
    assert tenner - fiver == fiver

def adding_different_currencies_fails():
    with pytest.raises(ValueError):
        Money('usd', 10) + Money('gdp', 10)

def can_multiply_money_by_a_number():
    assert fiver * 5 == Money('gdp', 25)

def multiplying_two_money_values_is_an_error():
    with pytest.raises(TypeError):
        tenner * fiver
        
def test_barry_is_harry():
    harry = Person(Name("Harry", "Percival"))
    barry = harry

    barry.name = Name("Barry", "Percival")

    assert harry is barry and barry is harry