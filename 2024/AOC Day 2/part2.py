'''
--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
'''

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
                    new_report = levels[:i] + levels[i + 1:]
                    if is_safe(new_report):
                        safe_reports += 1
                        break

    return safe_reports


if __name__ == "__main__":
    result = count_safe_reports("input.txt")
    print(result)
