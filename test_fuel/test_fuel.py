from fuel import convert, gauge
import pytest

def test_convert_valid():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1

def test_convert_invalid_values():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("10/5")
    with pytest.raises(ValueError):
        convert("-1/4")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
