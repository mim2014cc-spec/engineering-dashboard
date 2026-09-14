# services/power.py

def calculate_power(voltage: float, current: float) -> float:
    """คำนวณกำลังไฟฟ้า P = V * I โดย V > 0 และ I >= 0; หากผิดเงื่อนไขให้ raise ValueError"""
    if voltage <= 0:
        raise ValueError("แรงดันไฟฟ้า (Voltage) ต้องมากกว่า 0 V")
    if current < 0:
        raise ValueError("กระแสไฟฟ้า (Current) ต้องมากกว่าหรือเท่ากับ 0 A")
    
    return round(float(voltage * current), 2)


def classify_power(power_watt: float) -> str:
    """จำแนกสถานะกำลังไฟฟ้า:
    - < 500 W -> NORMAL
    - 500 ถึง 1000 W -> WARNING
    - > 1000 W -> CRITICAL
    """
    if power_watt < 0:
        raise ValueError("กำลังไฟฟ้าต้องไม่ติดลบ")
        
    if power_watt < 500.0:
        return "NORMAL"
    elif power_watt <= 1000.0:
        return "WARNING"
    else:
        return "CRITICAL"