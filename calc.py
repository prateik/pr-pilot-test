import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(a)

    def log(self, a, base=10):
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive values")
        return math.log(a, base)

    def sin(self, angle):
        return math.sin(math.radians(angle))

    def cos(self, angle):
        return math.cos(math.radians(angle))

    def tan(self, angle):
        return math.tan(math.radians(angle))


if __name__ == "__main__":
    calc = Calculator()
    print("Addition: 5 + 3 =", calc.add(5, 3))
    print("Subtraction: 5 - 3 =", calc.subtract(5, 3))
    print("Multiplication: 5 * 3 =", calc.multiply(5, 3))
    print("Division: 5 / 3 =", calc.divide(5, 3))
    print("Power: 5 ^ 3 =", calc.power(5, 3))
    print("Square Root: sqrt(25) =", calc.sqrt(25))
    print("Logarithm: log(100) =", calc.log(100))
    print("Sine: sin(30) =", calc.sin(30))
    print("Cosine: cos(60) =", calc.cos(60))
    print("Tangent: tan(45) =", calc.tan(45))
