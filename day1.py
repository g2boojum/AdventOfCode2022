# https://adventofcode.com/2022/day/1

import pathlib

testdata = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".splitlines()


def parse(lines):
    elves = []
    cals = []
    for line in lines:
        if line == '':
            elves.append(cals)
            cals = []
            continue
        cal = int(line)
        cals.append(cal)
    if cals:
        elves.append(cals)
    return elves


def max_cals(elves):
    return [sum(cals) for cals in elves]


if __name__ == "__main__":
    print("Part 1")
    tstelves = parse(testdata)
    tst_tot_cals = sorted(max_cals(tstelves), reverse=True)
    print(tst_tot_cals)
    print("Test max cals: ", tst_tot_cals[0])
    data = pathlib.Path('day1.txt').read_text().splitlines()
    elves = parse(data)
    tot_cals = sorted(max_cals(elves), reverse=True)
    print("Data max cals: ", tot_cals[0])
    print()
    print("Part 2")
    print("Test top 3: ", sum(tst_tot_cals[:3]))
    print("Data top 3: ", sum(tot_cals[:3]))
