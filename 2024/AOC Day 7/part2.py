'''
--- Part Two ---
The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.

The concatenation operator (||) combines the digits from its left and right inputs into a single number. For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.

Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:

156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
192: 17 8 14 can be made true using 17 || 8 + 14.
Adding up all six test values (the three that could be made before using only + and * plus the new three that can now be made by also using ||) produces the new total calibration result of 11387.

Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their total calibration result?
'''

from itertools import product

results = []
nums_list = []
total = 0

with open("input.txt","r") as file:
    for line in file:
        result , eqn = line.strip().split(":")
        results.append(int(result.strip()))
        nums_list.append(list(map(int, eqn.strip().split())))

def evaluate(nums, ops):
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == "*":
            result *= nums[i+1]
        elif ops[i] == "+":
            result += nums[i+1]
        elif ops[i] == "||":
            result = int( str(result) + str(nums[i+1]) )
    
    return result

for i in range(len(results)):
    operator_combinations = product( ["*", "+", "||"] , repeat = len(nums_list[i]) - 1 )
    for operators in operator_combinations:
        if results[i] == evaluate( nums_list[i] , operators ):
            total += results[i]
            break
    
print(f'{ total = }')