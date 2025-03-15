import sys, itertools


def parse_input(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f if l.strip()]
    init = {}
    gates = []
    for l in lines:
        if "->" in l:
            left, out = l.split(" -> ")
            parts = left.split()
            gates.append((parts[0], parts[1], parts[2], out))
        else:
            w, v = l.split(": ")
            init[w] = int(v)
    return init, gates


def simulate(gates, init):
    wires = dict(init)
    pending = set(range(len(gates)))
    while pending:
        prog = False
        for i in list(pending):
            a, op, b, out = gates[i]
            if a in wires and b in wires:
                if op == "AND":
                    wires[out] = wires[a] & wires[b]
                elif op == "OR":
                    wires[out] = wires[a] | wires[b]
                elif op == "XOR":
                    wires[out] = wires[a] ^ wires[b]
                pending.remove(i)
                prog = True
        if not prog:
            break
    return wires


def get_number(prefix, wires):
    lst = []
    for k, v in wires.items():
        if k.startswith(prefix):
            lst.append((int(k[1:]), v))
    if not lst:
        return 0
    lst.sort(key=lambda x: x[0])
    bits = "".join(str(v) for _, v in lst[::-1])
    return int(bits, 2)


init, orig_gates = parse_input("input.txt")
wires_orig = simulate(orig_gates, init)
expected = get_number("x", init) + get_number("y", init)
out_to_gate = {}
for i, g in enumerate(orig_gates):
    out_to_gate[g[3]] = i
cand = set()
stack = []
wires_sim = simulate(orig_gates, init)
for w in wires_sim:
    if w.startswith("z") and w in out_to_gate:
        stack.append(out_to_gate[w])
while stack:
    i = stack.pop()
    if i in cand:
        continue
    cand.add(i)
    a, op, b, out = orig_gates[i]
    if a in out_to_gate:
        stack.append(out_to_gate[a])
    if b in out_to_gate:
        stack.append(out_to_gate[b])
cand = sorted(list(cand))


def apply_swaps(pairs, gates):
    new = list(gates)
    for i, j in pairs:
        out_i = new[i][3]
        out_j = new[j][3]
        new[i] = (new[i][0], new[i][1], new[i][2], out_j)
        new[j] = (new[j][0], new[j][1], new[j][2], out_i)
    return new


found = False


def backtrack(start, used, pairs):
    global found
    if found:
        return
    if len(pairs) == 4:
        new_g = apply_swaps(pairs, orig_gates)
        wires = simulate(new_g, init)
        if get_number("z", wires) == expected:
            sw = []
            for i, j in pairs:
                sw.append(orig_gates[i][3])
                sw.append(orig_gates[j][3])
            sw = sorted(sw)
            print(",".join(sw))
            found = True
            sys.exit(0)
        return
    for i in range(start, len(cand)):
        if cand[i] in used:
            continue
        for j in range(i + 1, len(cand)):
            if cand[j] in used:
                continue
            new_used = used | {cand[i], cand[j]}
            backtrack(i + 1, new_used, pairs + [(cand[i], cand[j])])


backtrack(0, set(), [])
if not found:
    print("No solution found")
