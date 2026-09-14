def generate_alarms(
    temp_status: str,
    humid_status: str,
    power_status: str
) -> list[str]:
    """คืน list ข้อความเตือนตามลำดับ Temp -> Humid -> Power; ปกติทั้งหมดคืน []"""
    valid_statuses = {"NORMAL", "WARNING", "CRITICAL"}

    for status in (temp_status, humid_status, power_status):
        if status not in valid_statuses:
            raise ValueError(f"สถานะไม่ถูกต้อง: {status}")

    alarms = []

    # 1. ตรวจสอบ Temperature
    if temp_status == "WARNING":
        alarms.append("WARNING: Temperature requires attention")
    elif temp_status == "CRITICAL":
        alarms.append("CRITICAL: Temperature is unsafe")

    # 2. ตรวจสอบ Humidity
    if humid_status == "WARNING":
        alarms.append("WARNING: Humidity requires attention")
    elif humid_status == "CRITICAL":
        alarms.append("CRITICAL: Humidity is unsafe")

    # 3. ตรวจสอบ Power
    if power_status == "WARNING":
        alarms.append("WARNING: Power consumption is high")
    elif power_status == "CRITICAL":
        alarms.append("CRITICAL: Power consumption is unsafe")

    return alarms