# The coin problem (or Frobenius problem) is a mathematical problem
# that asks for the largest monetary amount that cannot be obtained
# using only coins of specified denominations, for example, the
# largest amount that cannot be obtained using only coins of 3 and 5
# units is 7 units. The solution to this problem for a given set of coin
# denominations is called the Frobenius number of the set. The Frobenius
# number exists as long as the set of coin denominations has no common
# divisor greater than 1.


from euclidean_algorithm import EuclideanAlgorithm


class CoinProblem(object):
    def frobenius_number(self, a, b):
        euclidean_alg = EuclideanAlgorithm()
        gcd = euclidean_alg.gcd(a, b)
        if gcd != 1:
            return -1
        return a * b - a - b


if __name__ == "__main__":
    s = CoinProblem()
    a, b = 9, 20
    print(s.frobenius_number(a, b))
