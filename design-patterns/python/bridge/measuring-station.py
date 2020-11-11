class adc:
    def start_record(some_args):
        pass


class adc1(adc):
    def start_record(some_args):
        print('very complex implementation')


class adc2(adc):
    def start_record(some_args):
        print('very very complex implementation!')


class measuring_station:
    def start_record(some_args):
        pass

    def another_functions(some_args):
        pass


class ecg_measuring_station:
    def __init__(self, adc):
        self.adc = adc

    def start_record(self, some_args):
        self.adc.start_record(some_args)

ecg1 = ecg_measuring_station(adc1)
ecg1.start_record(None)

ecg2 = ecg_measuring_station(adc2)
ecg2.start_record(None)
