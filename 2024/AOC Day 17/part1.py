# https://adventofcode.com/2024/day/17

import re


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
        program = []


def get_combo_value(operand, registers):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return registers.get("A", 0)
    elif operand == 5:
        return registers.get("B", 0)
    elif operand == 6:
        return registers.get("C", 0)
    else:
        raise ValueError(f"Invalid combo operand: {operand}")


ip = 0
output = []

while ip < len(program):
    opcode = program[ip]
    if ip + 1 < len(program):
        operand = program[ip + 1]
    else:
        break

    jump_taken = False

    if opcode == 0:
        # adv: Divide register A by 2^(combo operand) and store the result in A.
        val = get_combo_value(operand, registers)
        denom = 2**val
        registers["A"] = registers.get("A", 0) // denom

    elif opcode == 1:
        # bxl: Bitwise XOR of register B with the literal operand; store result in B.
        registers["B"] = registers.get("B", 0) ^ operand

    elif opcode == 2:
        # bst: Set register B to (combo operand modulo 8).
        val = get_combo_value(operand, registers)
        registers["B"] = val % 8

    elif opcode == 3:
        # jnz: If register A is nonzero, jump to the literal operand address.
        # If A is 0, do nothing (i.e. simply add 2 later).
        if registers.get("A", 0) != 0:
            ip = operand
            jump_taken = True

    elif opcode == 4:
        # bxc: Set register B to (B XOR C); operand is read but ignored.
        registers["B"] = registers.get("B", 0) ^ registers.get("C", 0)

    elif opcode == 5:
        # out: Output (combo operand modulo 8).
        val = get_combo_value(operand, registers)
        output.append(str(val % 8))

    elif opcode == 6:
        # bdv: Divide register A by 2^(combo operand) and store the result in B.
        val = get_combo_value(operand, registers)
        denom = 2**val
        registers["B"] = registers.get("A", 0) // denom

    elif opcode == 7:
        # cdv: Divide register A by 2^(combo operand) and store the result in C.
        val = get_combo_value(operand, registers)
        denom = 2**val
        registers["C"] = registers.get("A", 0) // denom

    else:
        raise ValueError(f"Unknown opcode {opcode} at instruction pointer {ip}")

    if not jump_taken:
        ip += 2


result = ",".join(output)
print(f"{ result = }")
