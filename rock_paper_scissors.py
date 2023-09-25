# If 1 person has to be chosen out of a group of three 3 people (a, b, c)
# using rock paper scissors, is winner(winner(a,b),c) a random and fair
# way to decide this?

import random


class RpsTournment(object):
    def game(self):
        result = random.randint(0, 1)  # a x b
        if result == 0:  # a wins
            result = random.randint(0, 1)  # b x c
            if result == 0:
                return "c"
            elif result == 1:
                return "b"
        elif result == 1:  # b wins
            result = random.randint(0, 1)  # a x c
            if result == 0:
                return "c"
            elif result == 1:
                return "a"


if __name__ == "__main__":
    sim = 10000
    loser_count = {"a": 0, "b": 0, "c": 0}
    for i in range(sim):
        t = RpsTournment()
        loser = t.game()
        loser_count[loser] += 1
    print(loser_count)
