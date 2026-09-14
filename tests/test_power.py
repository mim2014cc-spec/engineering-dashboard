# tests/test_power.py
import pytest
from services.power import calculate_power, classify_power

# ----------------- ทดสอบ calculate_power -----------------

def test_calculate_power_normal():
    """คำนวณกำลังไฟฟ้าปกติ P = 220V * 2A = 440W"""
    assert calculate_power(220, 2) == 440.0

def test_calculate_power_zero_current():
    """กระแสเป็น 0 ได้ กำลังไฟฟ้าต้องเป็น 0W"""
    assert calculate_power(220, 0) == 0.0

def test_calculate_power_invalid_voltage():
    """Voltage <= 0 ต้องเกิด ValueError"""
    with pytest.raises(ValueError):
        calculate_power(0, 5)
    with pytest.raises(ValueError):
        calculate_power(-220, 5)

def test_calculate_power_invalid_current():
    """Current < 0 ต้องเกิด ValueError"""
    with pytest.raises(ValueError):
        calculate_power(220, -1)


# ----------------- ทดสอบ classify_power -----------------

def test_classify_power_normal():
    """น้อยกว่า 500 W ต้องเป็น NORMAL"""
    assert classify_power(0) == "NORMAL"
    assert classify_power(499.9) == "NORMAL"

def test_classify_power_warning():
    """500 ถึง 1000 W ต้องเป็น WARNING (รวมขอบ 500 และ 1000)"""
    assert classify_power(500.0) == "WARNING"
    assert classify_power(750.0) == "WARNING"
    assert classify_power(1000.0) == "WARNING"

def test_classify_power_critical():
    """มากกว่า 1000 W ต้องเป็น CRITICAL"""
    assert classify_power(1000.1) == "CRITICAL"
    assert classify_power(2500.0) == "CRITICAL"

def test_classify_power_negative():
    """กำลังไฟฟ้าติดลบต้องเกิด ValueError"""
    with pytest.raises(ValueError):
        classify_power(-50)