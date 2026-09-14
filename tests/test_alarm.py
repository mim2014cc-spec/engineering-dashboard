import pytest
from services.alarm import generate_alarms

def test_all_normal():
    # กรณีทุกโมดูลปกติ ต้องได้ []
    assert generate_alarms("NORMAL", "NORMAL", "NORMAL") == []

def test_single_warning():
    # กรณีมี 1 โมดูลเป็น WARNING
    expected = ["WARNING: Temperature requires attention"]
    assert generate_alarms("WARNING", "NORMAL", "NORMAL") == expected

def test_mixed_warning_and_critical():
    # กรณีมี WARNING และ CRITICAL พร้อมกัน (ตรวจการเรียงลำดับ)
    expected = [
        "CRITICAL: Humidity is unsafe",
        "WARNING: Power consumption is high"
    ]
    assert generate_alarms("NORMAL", "CRITICAL", "WARNING") == expected

def test_all_critical():
    # กรณีทุกโมดูลเป็น CRITICAL
    expected = [
        "CRITICAL: Temperature is unsafe",
        "CRITICAL: Humidity is unsafe",
        "CRITICAL: Power consumption is unsafe"
    ]
    assert generate_alarms("CRITICAL", "CRITICAL", "CRITICAL") == expected

def test_invalid_input():
    # กรณีใส่ค่าที่ไม่ใช่ NORMAL, WARNING หรือ CRITICAL ต้องเกิด ValueError
    with pytest.raises(ValueError):
        generate_alarms("OK", "NORMAL", "NORMAL")
    with pytest.raises(ValueError):
        generate_alarms("NORMAL", "ERROR", "NORMAL")