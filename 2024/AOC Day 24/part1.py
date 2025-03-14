# https://adventofcode.com/2024/day/24

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

wires = {}
gates = []
for line in lines:
    if ":" in line and "->" not in line:
        wire, value = line.split(":")
        wires[wire.strip()] = int(value.strip())
    elif "->" in line:
        parts = line.split("->")
        gate_info = parts[0].strip()
        out_wire = parts[1].strip()
        tokens = gate_info.split()
        if len(tokens) == 3:
            a, op, b = tokens
            gates.append((a, op, b, out_wire))
        else:
            raise ValueError("Unexpected gate format: " + line)
    else:
        pass

progress = True
while progress and gates:
    progress = False
    remaining_gates = []
    for a, op, b, out in gates:
        if a in wires and b in wires:
            a_val = wires[a]
            b_val = wires[b]
            if op == "AND":
                result = a_val & b_val
            elif op == "OR":
                result = a_val | b_val
            elif op == "XOR":
                result = a_val ^ b_val
            else:
                raise ValueError("Unknown operator: " + op)
            wires[out] = result
            progress = True
        else:
            remaining_gates.append((a, op, b, out))
    gates = remaining_gates

z_wires = {wire: value for wire, value in wires.items() if wire.startswith("z")}
if not z_wires:
    print("No wires starting with 'z' found.")


sorted_keys = sorted(z_wires.keys(), key=lambda k: int(k[1:]))

binary_str = "".join(str(z_wires[k]) for k in reversed(sorted_keys))
decimal_value = int(binary_str, 2)

print(f"{ decimal_value = }")
