# day4.py

testlines = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()

with open('day4.txt') as fp:
    data = fp.read().splitlines()

def parse_line(line):
    lf, rt = line.split(',')
    lfmin, lfmax = lf.split('-')
    rtmin, rtmax = rt.split('-')
    return (int(lfmin), int(lfmax)), (int(rtmin), int(rtmax))

def is_wholly_contained(a, b):
    amin, amax = a
    bmin, bmax = b
    if amin < bmin:
        # a starts to the left of b
        if amax >= bmax:
            return True
    elif amin == bmin:
        # starts in the same place, so one of them _must_ contain the other
        return True
    else:
        # b starts to the left of a
        if bmax >= amax:
            return True
    return False

def part1(lines):
    num = 0
    for line in lines:
        a, b = parse_line(line)
        if is_wholly_contained(a, b):
            num += 1
    return num

if __name__ == '__main__':
    print('Part 1')
    print('test: ', part1(testlines))
    print('data: ', part1(data))

    
def is_overlapped(a, b):
    amin, amax = a
    bmin, bmax = b
    if amin == bmin:
        return True
    elif amin < bmin:
        # a starts to the left of b
        if amax >= bmin:
            return True
    else:
        # b starts to the left of a
        if bmax >= amin:
            return True
    return False

def part2(lines):
    num = 0
    for line in lines:
        a, b = parse_line(line)
        if is_overlapped(a, b):
            num += 1
    return num

if __name__ == '__main__':
    print('Part 2')
    print('test: ', part2(testlines))
    print('data: ', part2(data))

