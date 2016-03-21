
class Temperature(object):
    '''
    Wrapper for temperature in Fahrenheit scale

    Input values should be given in Celsius and converted using formula:
    Celsius * 1.8 + 32

    >>> t = Temperature(30)
    >>> t.temperature
    86.0
    >>> t.temperature = 35
    >>> t.temperature
    95.0
    '''
    def __init__(self, celsius):
        self.temp = celsius

    def get_temp(self):
        return (self.temp * 1.8 + 32)

    def set_temp(self, value):
        self.temp = value

    temperature = property(get_temp, set_temp)

tmp = Temperature(30)
print tmp.temperature

tmp.temperature = 100
print tmp.temperature
    

