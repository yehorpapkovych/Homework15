class Fraction:

    def __init__(self, num1, num2):
        if num2 == 0:
            raise ValueError('Denominator cannot be zero.')
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f'{self.num1}/{self.num2}'

    def simplify(self):
        for i in range(2, self.num2 + 1):
            if self.num1 % i == 0 and self.num2 % i == 0:
                self.num1 = self.num1 / i
                self.num2 = self.num2 / i

    def __add__(self, other):
        new_num1 = self.num1 * other.num2 + self.num2 * other.num1
        new_num2 = self.num2 * other.num2
        result = Fraction(new_num1, new_num2)
        result.simplify()
        return result

    def __sub__(self, other):
        new_num1 = self.num1 * other.num2 - self.num2 * other.num1
        new_num2 = self.num2 * other.num2
        result = Fraction(new_num1, new_num2)
        result.simplify()
        return result

    def __mul__(self, other):
        new_num1 = self.num1 * other.num1
        new_num2 = self.num2 * other.num2
        result = Fraction(new_num1, new_num2)
        result.simplify()
        return result

    def __truediv__(self, other):
        if other.num2 == 0:
            raise ZeroDivisionError('Denominator cannot be zero.')
        new_num1 = self.num1 * other.num2
        new_num2 = self.num2 * other.num1
        result = Fraction(new_num1, new_num2)
        result.simplify()
        return result

    def __lt__(self, other):
        return (self.num1 * other.num2) < (other.num1 * self.num2)

    def __gt__(self, other):
        return (self.num1 * other.num2) > (other.num1 * self.num2)

    def __le__(self, other):
        return (self.num1 * other.num2) <= (other.num1 * self.num2)

    def __ge__(self, other):
        return (self.num1 * other.num2) >= (other.num1 * self.num2)


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x < y)
    print(x <= y)
    print(x > y)
    print(x >= y)