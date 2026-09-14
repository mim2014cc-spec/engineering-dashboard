def classify_humidity(percent: float) -> str:
    if not 0 <= percent <= 100:
        raise ValueError("ความชื้นต้องอยู่ระหว่าง 0 ถึง 100 %")
    if 40 <= percent <= 60:
        return "NORMAL"
    if 30 <= percent <= 70:
        return "WARNING"
    return "CRITICAL"