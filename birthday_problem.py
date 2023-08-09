# In probability theory, the birthday problem asks for the probability that,
# in a set of n randomly chosen people, at least two will share a birthday.
# The birthday paradox refers to the counterintuitive fact that only
# 23 people are needed for that probability to exceed 50%.


import random


class BirthdayProblem(object):
    def prob_shared_birthday(self, n_babies, n_simulations=50000):
        shared_birthdays = 0
        for simulation in range(n_simulations):
            birthdays = []
            for baby in range(n_babies):
                birthdays.append(random.randint(1, 365))
            if len(birthdays) != len(set(birthdays)):
                shared_birthdays += 1
        # probability of finding a shared birthday with n_babies
        prob = (shared_birthdays * 100) / n_simulations
        return prob


if __name__ == "__main__":
    s = BirthdayProblem()
    n_babies = 23
    n_simulations = 50000
    print(s.prob_shared_birthday(n_babies, n_simulations))
