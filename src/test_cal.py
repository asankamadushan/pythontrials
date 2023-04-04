"""
Test the calculator library
"""
import pytest
from main import Calculator

pytest.mark.parametrize("a, b, result", [(2, 2, 4), (3, 3, 6), (4, 4, 8)])
def test_add(a, b, result):
    calc = Calculator()
    assert calc.add(a, b) == result

def test_sub():
    calc = Calculator()
    assert calc.sub(2, 2) == 0

def test_mul():
    calc = Calculator()
    assert calc.mul(2, 2) == 4

def test_div():
    calc = Calculator()
    assert calc.div(2, 2) == 1