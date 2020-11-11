from libadc1 import *
from libadc2 import *

class adapt_adc1(adc1):
    def set_channel(self, rate, gain):
        self.set(rate, gain)

    def get_hz_rate(self):
        return self.rate

class adapt_adc2(adc2):
    def set_channel(self, rate, gain):
        self.set_rate(rate/1000)
        self.set_gain(gain)

    def get_hz_rate(self):
        return self.rate*1000

class adc:
    def __init__(self, device):
        self.device = device

    def print_setting(self):
        print('Adc 1. Rate={0} Hz. Gain = {1}'.format(self.device.get_hz_rate(), self.device.gain))
    
a = adapt_adc1()
#a = adapt_adc2()
a.set_channel(20,2)

source = adc(a)
source.print_setting()

