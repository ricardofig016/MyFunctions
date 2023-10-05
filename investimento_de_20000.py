# Suponha que lhe é proposto um investimento de 20 000 € numa
# pequena empresa. A partir de um estudo à viabilidade da
# empresa estimou-se que: com probabilidade de 10% o
# investimento quadriplicará no primeiro ano, com probabilidade de
# 40% a empresa falhará levando à perda total do investimento, e
# com 50% de probabilidade a empresa sobreviverá, mas com uma
# perda de um quarto do investimento. Com base nestas estimativas
# que decisão deve tomar?


import random


class Investimento(object):
    def invest(self, invest_amount):
        seed = random.randint(1, 10)
        if seed <= 1:
            return invest_amount * 4
        elif seed <= 5:
            return invest_amount * 0
        elif seed <= 10:
            return invest_amount * (3 / 4)


if __name__ == "__main__":
    sim = 10000000
    amount = 20000
    sum_of_results = 0
    for i in range(sim):
        inv = Investimento()
        sum_of_results += inv.invest(amount)
    average = sum_of_results / sim
    print(average)
