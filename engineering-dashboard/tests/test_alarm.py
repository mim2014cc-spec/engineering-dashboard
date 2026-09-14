def generate_alarms(temp_status: str, humid_status: str, power_status: str) -> list[str]:
    valid = {"NORMAL", "WARNING", "CRITICAL"}
    for s in [temp_status, humid_status, power_status]:
        if s not in valid:
            raise ValueError(f"สถานะไม่ถูกต้อง: {s}")

    alarms = []
    # 1. Temperature
    if temp_status == "WARNING":
        alarms.append("WARNING: Temperature requires attention")
    elif temp_status == "CRITICAL":
        alarms.append("CRITICAL: Temperature is unsafe")

    # 2. Humidity
    if humid_status == "WARNING":
        alarms.append("WARNING: Humidity requires attention")
    elif humid_status == "CRITICAL":
        alarms.append("CRITICAL: Humidity is unsafe")

    # 3. Power
    if power_status == "WARNING":
        alarms.append("WARNING: Power consumption is high")
    elif power_status == "CRITICAL":
        alarms.append("CRITICAL: Power consumption is unsafe")

    return alarms