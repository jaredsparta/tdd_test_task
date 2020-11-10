class Calc:
    # Returns T/F if the value is positive
    def is_positive(self, value):
        if value > 0:
            return True
        return False

    # Returns T/F if the num1 is divisible by num2
    def remainder(self, num1, num2):
        if num1 % num2 == 0:
            return True
        return False