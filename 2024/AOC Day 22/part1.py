# https://adventofcode.com/2024/day/22#part2

MOD = 16777216
ITERATIONS = 2000

with open("input.txt", "r") as file:
    initial_secrets = list(map(int, file.readlines()))


def next_secret(secret):
    # Step 1: Multiply by 64, mix (XOR) then prune modulo MOD
    secret = (secret ^ (secret * 64)) % MOD
    # Step 2: Floor divide by 32, mix then prune modulo MOD
    secret = (secret ^ (secret // 32)) % MOD
    # Step 3: Multiply by 2048, mix then prune modulo MOD
    secret = (secret ^ (secret * 2048)) % MOD
    return secret


total = 0

for secret in initial_secrets:
    for _ in range(ITERATIONS):
        secret = next_secret(secret)
    total += secret

print(f"{ total = }")
