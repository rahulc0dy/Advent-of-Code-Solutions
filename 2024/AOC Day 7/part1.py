# https://adventofcode.com/2024/day/7

from itertools import product

results = []
nums_list = []
total = 0

with open("input.txt", "r") as file:
    for line in file:
        result, eqn = line.strip().split(":")
        results.append(int(result.strip()))
        nums_list.append(list(map(int, eqn.strip().split())))


def evaluate(nums, ops):
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == "*":
            result *= nums[i + 1]
        elif ops[i] == "+":
            result += nums[i + 1]

    return result


for i in range(len(results)):
    operator_combinations = product(["*", "+"], repeat=len(nums_list[i]) - 1)
    for operators in operator_combinations:
        if results[i] == evaluate(nums_list[i], operators):
            total += results[i]
            break

print(f"{ total = }")
