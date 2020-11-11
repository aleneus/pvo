from libadc1 import ADC1
from libadc2 import ADC2


class AdapterADC1(ADC1):
    def set_channel(self, rate, gain):
        self.set(rate, gain)

    def get_hz_rate(self):
        return self.rate


class AdapterADC2(ADC2):
    def set_channel(self, rate, gain):
        self.set_rate(rate/1000)
        self.set_gain(gain)

    def get_hz_rate(self):
        return self.rate*1000


class ADC:
    def __init__(self, device):
        self.device = device

    def print_setting(self):
        print('ADC 1. Rate={0} Hz. Gain = {1}'.
              format(self.device.get_hz_rate(), self.device.gain))


if __name__ == "__main__":
    a = AdapterADC1()
    a.set_channel(20, 2)

    source = ADC(a)
    source.print_setting()
