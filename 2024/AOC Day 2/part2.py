# https://adventofcode.com/2024/day/2#part2


def is_safe(report):
    if len(report) < 2:
        return True

    diff = report[1] - report[0]
    if diff == 0 or abs(diff) > 3:
        return False

    increasing = diff > 0

    for i in range(1, len(report)):
        d = report[i] - report[i - 1]
        if d == 0 or abs(d) > 3:
            return False
        if increasing and d < 0:
            return False
        if not increasing and d > 0:
            return False

    return True


def count_safe_reports(filename):
    safe_reports = 0

    with open(filename, "r") as file:
        for line in file:
            levels = list(map(int, line.strip().split()))

            if is_safe(levels):
                safe_reports += 1
            else:
                for i in range(len(levels)):
                    new_report = levels[:i] + levels[i + 1 :]
                    if is_safe(new_report):
                        safe_reports += 1
                        break

    return safe_reports


if __name__ == "__main__":
    result = count_safe_reports("input.txt")
    print(result)
