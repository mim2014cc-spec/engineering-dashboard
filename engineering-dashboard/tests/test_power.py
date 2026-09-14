def calculate_power(voltage: float, current: float) -> float:
    if voltage <= 0 or current < 0:
        raise ValueError("แรงดันต้อง > 0 และกระแสต้อง >= 0")
    return round(voltage * current, 2)

def classify_power(power_watt: float) -> str:
    if power_watt < 500:
        return "NORMAL"
    elif power_watt <= 1000:
        return "WARNING"
    return "CRITICAL"