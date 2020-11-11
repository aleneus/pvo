"""Strategy pattern example."""


class Activity:
    """
    Any activity, elementary, complex and very complex.
    """
    def __init__(self):
        self.workers = {}
        self.name = ""
        self.info = ""

    def set_worker(self, work, worker):
        self.workers[work] = worker

    def set_default_worker(self, work, activity):
        if work not in self.workers.keys():
            self.set_worker(work, activity)

    def __call__(self):
        raise NotImplementedError


class OutputDigit(Activity):
    pass


class DigitAsDigit(OutputDigit):
    def __init__(self, check_value=False):
        self.check_value = check_value

    def __call__(self, x):
        if self.check_value and ((x > 9) or (x < 0)):
            print('Wrong number')
            return
        print(x, end='')


class DigitAsText(OutputDigit):
    def __call__(self, x):
        if x == 0:
            word = 'zero'
        elif x == 1:
            word = 'one'
        elif x == 2:
            word = 'two'
        elif x == 3:
            word = 'three'
        elif x == 4:
            word = 'four'
        elif x == 5:
            word = 'five'
        elif x == 6:
            word = 'six'
        elif x == 7:
            word = 'seven'
        elif x == 8:
            word = 'eight'
        else:
            word = 'nine'
        print(word, end=' ')


class OutputNumber(Activity):
    def __init__(self):
        super().__init__()
        self.set_default_worker('output', DigitAsDigit())

    def __call__(self, n):
        digits = []
        while True:
            digits.append(n % 10)
            n = n // 10
            if n == 0:
                break
        for d in reversed(digits):
            self.workers['output'](d)
        print()


def main():
    out_num = OutputNumber()
    out_num.workers['output'] = DigitAsDigit()
    out_num(123)
    print()
    out_num.workers['output'] = DigitAsText()
    out_num(123)


if __name__ == "__main__":
    main()
