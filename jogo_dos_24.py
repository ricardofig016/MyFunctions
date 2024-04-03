import random

from itertools import permutations, product
from icecream import ic

OPERATIONS = ["+", "-", "*", "/"]


def solve(nums):
    num_perms = permutations(nums)
    for num_perm in num_perms:
        for ops_set in product(OPERATIONS, repeat=len(nums) - 1):
            result = num_perm[0]
            for i in range(len(ops_set)):
                next_num = num_perm[i + 1]
                if ops_set[i] == "+":
                    result += next_num
                elif ops_set[i] == "-":
                    result -= next_num
                elif ops_set[i] == "*":
                    result *= next_num
                elif ops_set[i] == "/" and next_num != 0:
                    result /= next_num
            if result == 24:
                return [num_perm, ops_set]
    return [(), ()]


if __name__ == "__main__":
    nums = [
        random.randint(1, 20),
        random.randint(1, 20),
        random.randint(1, 20),
        random.randint(1, 20),
    ]
    [num_perm, ops] = solve(nums)
    if ops:
        str = "24 = " + "(" * (len(ops) - 1) + f"{num_perm[0]}"
        for i in range(len(ops)):
            str += f" {ops[i]} {num_perm[i+1]})"
        print(str[:-1])
    else:
        print(f"no possible solutions for {nums}")
