import pytest
from services.humidity import classify_humidity

def test_humidity_normal():
    assert classify_humidity(50) == "NORMAL"

def test_humidity_warning():
    assert classify_humidity(35) == "WARNING"
    assert classify_humidity(65) == "WARNING"

def test_humidity_critical():
    assert classify_humidity(20) == "CRITICAL"
    assert classify_humidity(85) == "CRITICAL"

def test_humidity_invalid():
    with pytest.raises(ValueError):
        classify_humidity(-5)
    with pytest.raises(ValueError):
        classify_humidity(105)