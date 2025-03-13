# https://adventofcode.com/2024/day/22#part2

MOD = 16777216


def next_secret(secret):
    # Step 1: Multiply by 64, then mix (XOR) and prune modulo MOD
    secret = (secret ^ (secret * 64)) % MOD
    # Step 2: Divide by 32 (integer division), mix then prune
    secret = (secret ^ (secret // 32)) % MOD
    # Step 3: Multiply by 2048, mix then prune
    secret = (secret ^ (secret * 2048)) % MOD
    return secret


def simulate_buyer(initial, iterations=2000):
    prices = [initial % 10]
    s = initial
    for _ in range(iterations):
        s = next_secret(s)
        prices.append(s % 10)
    changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
    return prices, changes


global_sales = {}

with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

for line in lines:
    initial_secret = int(line)
    prices, changes = simulate_buyer(initial_secret, iterations=2000)
    buyer_first_occurrence = {}
    for i in range(len(changes) - 3):
        pattern = (changes[i], changes[i + 1], changes[i + 2], changes[i + 3])
        if pattern not in buyer_first_occurrence:
            buyer_first_occurrence[pattern] = prices[i + 4]
    for pattern, sale_price in buyer_first_occurrence.items():
        global_sales[pattern] = global_sales.get(pattern, 0) + sale_price

best_total = max(global_sales.values(), default=0)
print(best_total)
