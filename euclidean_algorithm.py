# In mathematics, the Euclidean algorithm, or Euclid's algorithm, is an
# efficient method for computing the greatest common divisor (GCD) of two
# integers, the largest number that divides them both without a remainder.


class EuclideanAlgorithm(object):
    def gcd(self, a, b):
        if a < b:
            temp = a
            a = b
            b = temp
        while b:
            a, b = b, a % b
        return abs(a)


if __name__ == "__main__":
    s = EuclideanAlgorithm()
    a, b = 48, 60
    print(s.gcd(a, b))
