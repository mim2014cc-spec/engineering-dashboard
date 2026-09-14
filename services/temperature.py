class TemperatureService:
    @staticmethod
    def check_status(temp_celsius):
        """ตรวจสอบสถานะของอุณหภูมิ"""
        if temp_celsius > 38.0:
            return "High Risk (Fever)"
        elif temp_celsius < 35.0:
            return "Low (Hypothermia)"
        return "Normal"

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """แปลงอุณหภูมิ C เป็น F"""
        return (celsius * 9/5) + 32