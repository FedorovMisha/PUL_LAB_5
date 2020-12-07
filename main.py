class PolynomialOneVariable:
    coefficients = []

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def calculate_polynomial(self, x):
        n = len(self.coefficients) - 1
        result = self.coefficients[n]
        for i in range(n - 1, 0, -1):
            result = x * result + self.coefficients[i]

        return result

    def __str__(self):
        p_str = ''
        step = 0
        for i in self.coefficients:
            p_str = p_str + "+" + str(i) + "x^" + str(step)
            step += 1
        return p_str + "....."

    def __add__(self, other):
        items_count = max(len(self.coefficients), len(other.coefficients))
        result = []
        for i in range(0, items_count):
            a = 0
            b = 0
            if i < len(self.coefficients):
                a = self.coefficients[i]
            if i < len(other.coefficients):
                b = other.coefficients[i]
            result.append(a + b)
        return PolynomialOneVariable(result)

    def __sub__(self, other):
        items_count = max(len(self.coefficients), len(other.coefficients))
        result = []
        for i in range(0, items_count):
            a = 0
            b = 0
            if i < len(self.coefficients):
                a = self.coefficients[i]
            if i < len(other.coefficients):
                b = other.coefficients[i]
            result.append(a - b)
        return PolynomialOneVariable(result)

    def __mul__(self, other):
        items_count = len(self.coefficients) + len(other.coefficients) - 1
        result = [0 for i in range(0, items_count)]
        for i in range(0, len(self.coefficients)):
            for j in range(0, len(other.coefficients)):
                result[i + j] = self.coefficients[i] * other.coefficients[j]

        return PolynomialOneVariable(result)


class ComplexNumber:
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        result = str(self.a) + " + i" + str(self.b)
        return result

    def __mul__(self, other):
        part_1 = self.a * other.a - self.b * other.b
        part_2 = self.a * other.b + self.b * other.a
        return ComplexNumber(part_1, part_2)


p1 = PolynomialOneVariable([1, 2, 3, 5, 5])
p2 = PolynomialOneVariable([1, 2, 3, 4, 5])
print(p1)
print(p2)

res = p1  +  p2


print(res.calculate_polynomial(1))

z1 = ComplexNumber(3, 4)
z2 = ComplexNumber(5, -6)

res = z1 * z2
print(res)