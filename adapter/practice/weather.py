from abc import ABC, abstractmethod

class WeatherAPI:
    def get_temperature_kelvin(self)->float:
        return 10.0


class DualTemperatureService(ABC):
    @abstractmethod
    def get_temperature_celsius(self)->float:
        pass
    
    def get_temperature_fahrenheit(self)->float:
        pass

        
class TemperatureAdapter(DualTemperatureService):
    def __init__(self, weather_api:WeatherAPI):
        self.weather_api = weather_api
        
    def get_temperature_celsius(self):
        temp_in_kelvin = self.weather_api.get_temperature_kelvin()
        temp_in_celsius = temp_in_kelvin - 273.15
        return temp_in_celsius
    
    def get_temperature_fahrenheit(self):
        temp_in_kelvin = self.weather_api.get_temperature_kelvin()
        temp_in_fahrenheit = (temp_in_kelvin - 273.15) * 9/5 + 32
        return temp_in_fahrenheit
    
temp_adapter = TemperatureAdapter(WeatherAPI())
print(temp_adapter.get_temperature_celsius())
print(temp_adapter.get_temperature_fahrenheit())