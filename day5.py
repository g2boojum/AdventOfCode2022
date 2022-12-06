# day5.py

import re

testlines = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines()

with open('day5.txt') as fp:
    data = fp.read().splitlines()


def init_stacks(lines, numlineidx):
    numline = lines[numlineidx]
    numstacks = [int(d) for d in numline.split()][-1]
    stacks = [[] for _ in range(numstacks)]
    letter_positions = list(range(1, 1 + 4*(numstacks-1) + 1, 4))
    for line in reversed(lines[:numlineidx]):
        for stacknum, pos in enumerate(letter_positions):
            if pos >= len(line):
                continue
            c = line[pos]
            if c != ' ':
                stacks[stacknum].append(c)
    return stacks


def parse(lines):
    for i, line in enumerate(lines):
        if '1' in line:
            nbrlineidx = i
            break
    stacks = init_stacks(lines, nbrlineidx)
    moves = []
    for line in lines[nbrlineidx + 2:]:
        moves.append(tuple(map(int, re.findall(r'\d+', line))))
    return stacks, moves


def part1(lines):
    stacks, moves = parse(lines)
    for move in moves:
        num = move[0]
        fromidx = move[1] - 1
        toidx = move[2] - 1
        for _ in range(num):
            stacks[toidx].append(stacks[fromidx].pop())
    top_crates = [stack.pop() for stack in stacks]
    return top_crates


if __name__ == '__main__':
    print('Part 1')
    top_crates = part1(testlines)
    print('Test: ', ''.join(top_crates))
    top_crates = part1(data)
    print('Data: ', ''.join(top_crates))


def part2(lines):
    stacks, moves = parse(lines)
    for move in moves:
        num = move[0]
        fromidx = move[1] - 1
        toidx = move[2] - 1
        stacks[toidx].extend(stacks[fromidx][-num:])
        stacks[fromidx] = stacks[fromidx][:-num]
    top_crates = ''.join([stack.pop() for stack in stacks])
    return top_crates

if __name__ == '__main__':
    print('Part 2')
    top_crates = part2(testlines)
    print('Test: ', top_crates)
    top_crates = part2(data)
    print('Data: ', top_crates)
