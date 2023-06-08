# day15.py

import re
import numpy as np


testlines = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''.splitlines()

with open('day15.txt') as fp:
    data = fp.read().splitlines()


def parse(lines):
    closest = {}
    for line in lines:
        sx, sy, bx, by = tuple(map(int, re.findall(r"[-\d]+", line)))
        closest[(sx, sy)] = (bx, by)
    return closest


def r_taxi(a, b):
    ax, ay = a
    bx, by = b
    return np.abs(ax - bx) + np.abs(ay - by)


def calc_excluded(closest):
    excl = {}
    for sensor in closest:
        excl[sensor] = r_taxi(sensor, closest[sensor])
    return excl


def row_excluded(row, excl):
    rexcl = set()
    for sensor in excl:
        sx, sy = sensor
        d = excl[sensor]
        l = d - r_taxi(sensor, (sx, row))
        if l >= 0:
            rexcl.add(sx)
            for x in range(1, l+1):
                rexcl.add(sx+x)
                rexcl.add(sx-x)
    return rexcl


if __name__ == '__main__':
    c = parse(testlines)
    excl = calc_excluded(c)
    rowexcl = row_excluded(10, excl)
    print(len(rowexcl))

