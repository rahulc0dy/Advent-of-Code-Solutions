import random

with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]
initial_assignments = {}
gates = []
for line in lines:
    if ":" in line and "->" not in line:
        parts = line.split(":")
        wire = parts[0].strip()
        val = int(parts[1].strip())
        initial_assignments[wire] = val
    elif "->" in line:
        lhs, out_wire = line.split("->")
        out_wire = out_wire.strip()
        tokens = lhs.strip().split()
        in1 = tokens[0]
        op = tokens[1]
        in2 = tokens[2]
        gates.append({"op": op, "in1": in1, "in2": in2, "out": out_wire})
wire_to_gates = {}
for i, gate in enumerate(gates):
    for w in [gate["in1"], gate["in2"]]:
        wire_to_gates.setdefault(w, []).append(i)
wire_produced_by = {}
for i, gate in enumerate(gates):
    wire_produced_by[gate["out"]] = i


def simulate(swaps, input_assignment):
    wires = {}
    for w, val in initial_assignments.items():
        if w.startswith("x") or w.startswith("y"):
            if w in input_assignment:
                wires[w] = input_assignment[w]
            else:
                wires[w] = val
        else:
            wires[w] = val
    computed = [False] * len(gates)
    changed = True
    while changed:
        changed = False
        for i, gate in enumerate(gates):
            if computed[i]:
                continue
            if gate["in1"] in wires and gate["in2"] in wires:
                a = wires[gate["in1"]]
                b = wires[gate["in2"]]
                if gate["op"] == "AND":
                    res = a & b
                elif gate["op"] == "OR":
                    res = a | b
                elif gate["op"] == "XOR":
                    res = a ^ b
                else:
                    raise ValueError("Unknown op: " + gate["op"])
                effective_out = gate["out"]
                if i in swaps:
                    partner = swaps[i]
                    effective_out = gates[partner]["out"]
                if effective_out not in wires or wires[effective_out] != res:
                    wires[effective_out] = res
                    changed = True
                computed[i] = True
        computed = [False] * len(gates)
    return wires


def get_number(prefix, wires):
    bits = []
    for w, val in wires.items():
        if w.startswith(prefix):
            idx = int(w[len(prefix) :])
            bits.append((idx, val))
    if not bits:
        return 0
    bits.sort(key=lambda x: x[0])
    return sum(val * (2**idx) for idx, val in bits)


def test_swaps(swaps, tests):
    for assign in tests:
        wires = simulate(swaps, assign)
        X = get_number("x", wires)
        Y = get_number("y", wires)
        Z = get_number("z", wires)
        if Z != X + Y:
            return False
    return True


def get_input_wires(prefix):
    return sorted(
        [w for w in initial_assignments if w.startswith(prefix)],
        key=lambda w: int(w[len(prefix) :]),
    )


x_wires = get_input_wires("x")
y_wires = get_input_wires("y")
test1 = {
    w: initial_assignments[w] for w in (x_wires + y_wires) if w in initial_assignments
}
tests = [test1]
for _ in range(10):
    assign = {}
    for w in x_wires:
        assign[w] = random.randint(0, 1)
    for w in y_wires:
        assign[w] = random.randint(0, 1)
    tests.append(assign)
candidate_gates = {
    i for i, gate in enumerate(gates) if gate["out"].lower().startswith("z")
}
candidate_list = list(candidate_gates)
print("Found", len(candidate_list), "candidate gates.")


def search_swaps(candidate_list, used, start, chosen):
    if len(chosen) == 4:
        swaps = {}
        for a, b in chosen:
            swaps[a] = b
            swaps[b] = a
        if test_swaps(swaps, tests):
            swap_wires = []
            for a, b in chosen:
                swap_wires.append(gates[a]["out"])
                swap_wires.append(gates[b]["out"])
            swap_wires = sorted(swap_wires)
            result = ",".join(swap_wires)
            print("Solution found:")
            print(result)
            return True
        return False
    for i in range(start, len(candidate_list)):
        a = candidate_list[i]
        if a in used:
            continue
        for j in range(i + 1, len(candidate_list)):
            b = candidate_list[j]
            if b in used:
                continue
            new_used = used | {a, b}
            new_chosen = chosen + [(a, b)]
            if search_swaps(candidate_list, new_used, i + 1, new_chosen):
                return True
    return False


if not search_swaps(candidate_list, set(), 0, []):
    print("No valid swap configuration found.")
