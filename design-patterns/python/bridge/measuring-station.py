class ADC:
    def start_record(self):
        pass


class ADC1(ADC):
    def start_record(self):
        print('very complex implementation')


class ADC2(ADC):
    def start_record(self):
        print('very very complex implementation!')


class measuring_station:
    def start_record(self):
        pass

    def another_functions(self):
        pass


class ecg_measuring_station:
    def __init__(self, adc):
        self.adc = adc

    def start_record(self, some_args):
        self.adc.start_record(some_args)


if __name__ == "__main__":
    ecg1 = ecg_measuring_station(ADC1)
    ecg1.start_record(None)

    ecg2 = ecg_measuring_station(ADC2)
    ecg2.start_record(None)
