# day14.py

import matplotlib.pyplot as plt

testlines = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''.splitlines()

with open('day14.txt') as fp:
    data = fp.read().splitlines()


def parse(lines):
    rockpts = set()
    for line in lines:
        nodes = line.split('->')
        pairs = zip(nodes, nodes[1:])
        for p1,p2 in pairs:
            x1, y1 = (int(s) for s in p1.split(','))
            x2, y2 = (int(s) for s in p2.split(','))
            if x1 == x2:
                # vertical line
                for y in range(min(y1,y2), max(y1,y2)+1):
                    rockpts.add((x1, y))
            elif y1 == y2:
                # horizontal line
                for x in range(min(x1, x2), max(x1, x2)+1):
                    rockpts.add((x, y1))
            else:
                raise ValueError('Invalid rock pair: ', p1, p2)
    return rockpts


def plot_pts(pts, fname='rocks.svg'):
    fig, ax = plt.subplots()
    xlst = []; ylst = []
    for x,y in pts:
        xlst.append(x)
        ylst.append(y)
    ax.plot(xlst, ylst, 's')
    ax.invert_yaxis()
    fig.savefig(fname)


def bounds(pts):
    xlst = [p[0] for p in pts]
    ylst = [p[1] for p in pts]
    return min(xlst), max(xlst), min(ylst), max(ylst)


start = (500, 0)
def fall(pts, bottom):
    x,y = start
    has_escaped = False
    while y <= bottom:
        if (x, y+1) not in pts:
            y = y + 1
        elif (x-1, y+1) not in pts:
            x = x - 1
            y = y + 1
        elif (x+1, y+1) not in pts:
            x = x + 1
            y = y + 1
        else:
            # sand has come to rest here
            return has_escaped, (x,y)
    has_escaped = True
    return has_escaped, (x,y)


def part1(lines):
    rockpts = parse(lines)
    bottom = bounds(rockpts)[-1]
    numsand = 0
    while True:
        numsand += 1
        has_escaped, pos = fall(rockpts, bottom)
        if has_escaped:
            break
        rockpts.add(pos)
    return numsand - 1


if __name__ == '__main__':
    testrockpts = parse(testlines)
    plot_pts(testrockpts, 'testrocks.svg')
    print('Part 1')
    print('Test: ', part1(testlines))
    datarockpts = parse(data)
    plot_pts(datarockpts, 'datarocks.svg')
    print('Data: ', part1(data))


def fall2(pts, bottom):
    floor = bottom + 2
    x,y = start
    while y < floor-1:
        if (x, y+1) not in pts:
            y = y + 1
        elif (x-1, y+1) not in pts:
            x = x - 1
            y = y + 1
        elif (x+1, y+1) not in pts:
            x = x + 1
            y = y + 1
        else:
            # sand has come to rest here
            return (x,y)
    # sand is sitting on the floor
    return (x,y)


def part2(lines):
    rockpts = parse(lines)
    bottom = bounds(rockpts)[-1]
    numsand = 0
    while True:
        numsand += 1
        pos = fall2(rockpts, bottom)
        if pos == start:
            break
        rockpts.add(pos)
        if numsand > 1000000:
            raise ValueError('Too many interations!')
    return numsand 


if __name__ == '__main__':
    print('Part 2')
    print('Test: ', part2(testlines))
    print('Data: ', part2(data))
