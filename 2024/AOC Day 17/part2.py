# https://adventofcode.com/2024/day/17#part2
#!/usr/bin/env python3
import re
import sys


def simulate(program, initA, max_steps=10**6, check_interval=100):
    A = initA
    B = 0
    C = 0
    ip = 0
    outputs = []
    expected_length = len(program)
    steps = 0
    seen_states = {}
    p = program
    lp = len(p)

    while ip < lp and steps < max_steps:
        steps += 1
        # Only do cycle detection every check_interval steps to reduce overhead.
        if steps % check_interval == 0:
            state = (ip, A, B, C, len(outputs))
            if state in seen_states:
                return None
            seen_states[state] = True

        # Ensure there is an operand available.
        if ip + 1 >= lp:
            break
        opcode = p[ip]
        operand = p[ip + 1]

        if opcode == 0:
            # adv: A = A // (2 ** (combo operand))
            # Inline combo operand evaluation.
            if operand < 4:
                exp = operand
            elif operand == 4:
                exp = A
            elif operand == 5:
                exp = B
            elif operand == 6:
                exp = C
            A //= 2**exp
            ip += 2

        elif opcode == 1:
            # bxl: B = B XOR literal operand.
            B ^= operand
            ip += 2

        elif opcode == 2:
            # bst: B = (combo operand modulo 8).
            if operand < 4:
                val = operand
            elif operand == 4:
                val = A
            elif operand == 5:
                val = B
            elif operand == 6:
                val = C
            B = val % 8
            ip += 2

        elif opcode == 3:
            # jnz: if A != 0, jump to literal operand.
            if A != 0:
                ip = operand
            else:
                ip += 2

        elif opcode == 4:
            # bxc: B = B XOR C (operand ignored).
            B ^= C
            ip += 2

        elif opcode == 5:
            # out: output (combo operand modulo 8).
            if operand < 4:
                val = operand
            elif operand == 4:
                val = A
            elif operand == 5:
                val = B
            elif operand == 6:
                val = C
            out_val = val % 8
            outputs.append(out_val)
            # If output length exceeds the program length, candidate fails.
            if len(outputs) > expected_length:
                return None
            # Check the output so far matches the program's prefix.
            if outputs != p[: len(outputs)]:
                return None
            ip += 2

        elif opcode == 6:
            # bdv: B = A // (2 ** (combo operand)).
            if operand < 4:
                exp = operand
            elif operand == 4:
                exp = A
            elif operand == 5:
                exp = B
            elif operand == 6:
                exp = C
            B = A // (2**exp)
            ip += 2

        elif opcode == 7:
            # cdv: C = A // (2 ** (combo operand)).
            if operand < 4:
                exp = operand
            elif operand == 4:
                exp = A
            elif operand == 5:
                exp = B
            elif operand == 6:
                exp = C
            C = A // (2**exp)
            ip += 2

        else:
            raise ValueError("Unknown opcode: {}".format(opcode))

    # If the program halted and the outputs match exactly, return the outputs.
    if ip >= lp and outputs == p:
        return outputs
    return None


with open("input.txt", "r") as file:
    data = file.read().strip()
registers = {}
for line in data.splitlines():
    m = re.match(r"Register (\w+):\s*(-?\d+)", line)
    if m:
        registers[m.group(1)] = int(m.group(2))
program_match = re.search(r"Program:\s*([\d,]+)", data)
if program_match:
    program = list(map(int, program_match.group(1).split(",")))
else:
    print("No program found")
    sys.exit(1)

candidate = 1
while True:
    result = simulate(program, candidate)
    if result is not None:
        print("Lowest positive initial A =", candidate)
        break
    candidate += 1
