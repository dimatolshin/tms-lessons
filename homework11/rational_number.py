import math

class Rational:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        self.__normalize()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.__numerator}/{self.__denominator}'

    def __mul__(self, other: 'Rational'):
        new = self.__numerator * other.__numerator
        new1 = self.__denominator * other.__denominator
        return Rational(new, new1)

    def __truediv__(self, other: 'Rational'):
        new = self.__numerator * other.__denominator
        new1 = self.__denominator * other.__numerator
        return Rational(new, new1)

    def __add__(self, other: 'Rational'):
        first = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        second = self.__denominator * other.__denominator
        return Rational(first, second)

    def __sub__(self, other: 'Rational'):
        new = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        new1 = self.__denominator * other.__denominator
        return Rational(new, new1)

    def __eq__(self, other: 'Rational'):
        return self.__numerator / self.__denominator == other.__numerator / other.__denominator

    def __ne__(self, other: 'Rational'):
        return self.__numerator / self.__denominator != other.__numerator / other.__denominator

    def __gt__(self, other: 'Rational'):
        return self.__numerator / self.__denominator > other.__numerator / other.__denominator

    def __lt__(self, other: 'Rational'):
        return self.__numerator / self.__denominator < other.__numerator / other.__denominator

    def __ge__(self, other: 'Rational'):
        return self.__numerator / self.__denominator >= other.__numerator / other.__denominator

    def __le__(self, other: 'Rational'):
        return self.__numerator / self.__denominator <= other.__numerator / other.__denominator



    def __normalize(self):
        if self.__denominator < 0 and self.__numerator < 0 or self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1

        user = math.gcd(self.__numerator, self.__denominator)
        if user > 1:
            self.__numerator = self.__numerator // user
            self.__denominator = self.__denominator // user

if __name__ == '__main__':
    user = Rational(1, 4)
    use = Rational(3, 2)
    use_1 = Rational(1, 8)
    use_2 = Rational(156, 100)
    print(user.numerator)
    print(user.denominator)
    print(user)
    assert Rational(1, 2) > Rational(1, 3)
    assert Rational(1, 5) < Rational(3, 4)
    assert Rational(1, 4) >= Rational(1, 100)
    assert Rational(1, 45) >= Rational(1, 45)
    assert Rational(1, 400) <= Rational(1, 100)
    assert Rational(1, 4) <= Rational(1, 4)
    assert Rational(9, 45) == Rational(1, 5)
    assert Rational(19, 56) != Rational(1, 45)
    assert Rational(1, 4) + Rational(1, 4) == Rational(1, 2)
    assert Rational(3, 2) - Rational(1, 2) == Rational(1, 1)
    assert Rational(4, 9) * Rational(6, 12) == Rational(2, 9)
    print(Rational(2, 4))
    print(Rational(-1, -2))
    print(Rational(3, -9))
    print(user * (use + use_1) + use_2)
