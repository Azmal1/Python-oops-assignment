# 6) Write a Python class to implement pow(x, n) 
class PowerCalculator:

    def pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.pow(x, -n)
        if n % 2 == 0:
            half_pow = self.pow(x, n // 2)
            return half_pow * half_pow
        else:
            return x * self.pow(x, n - 1)

if __name__ == "__main__":
    calculator = PowerCalculator()
    x = 0
    n = 1
    result = calculator.pow(x, n)
    print(f"{x} raised to the power of {n} is {result}")
