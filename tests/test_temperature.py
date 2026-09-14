import pytest
from services.temperature import TemperatureService

def test_temperature_status():
    assert TemperatureService.check_status(37.0) == "Normal"
    assert TemperatureService.check_status(39.0) == "High Risk (Fever)"
    assert TemperatureService.check_status(34.0) == "Low (Hypothermia)"

def test_celsius_to_fahrenheit():
    assert TemperatureService.celsius_to_fahrenheit(0) == 32.0
    assert TemperatureService.celsius_to_fahrenheit(100) == 212.0