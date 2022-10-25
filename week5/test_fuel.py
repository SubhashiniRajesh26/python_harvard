from fuel import convert, gauge 
from pytest import raises
import pytest

def test_integer():
    assert convert('1/4') == 25
    assert convert('0/4') == 0
    assert convert('4/4') == 100

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert('100/0')

def test_valid_type():
    with pytest.raises(ValueError):
        convert('three/four')
        convert('2/1')


def test_gauge():
    # assert gauge(.75) == 'E'
    assert gauge(1.0) == 'E'
    assert gauge(100.0) == 'F'
    assert gauge(99.0) == 'F'
    assert gauge(45.0) == '45%'
    assert gauge(105.0) == 'F'
    assert gauge(0.0) == 'E'
