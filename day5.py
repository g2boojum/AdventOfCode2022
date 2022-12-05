# day5.py

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


def init_stacks(stacks, lines, nbrline):
    letter_positions = list(range(1, 1 + 4*(stacks-1), 4))
    for i in range(nbrlinenum-1, 0, -1):




def parse(lines):
    for i, line in enumerate(lines):
        if '1' in line:
            nbrline = line
            nbrlinenum = i
            break
    numstacks = [int(d) for d in nbrline.split()][-1]
    stacks = [[] for i in range[numstacks]]


def part1(lines):
    parse(lines)


if __name__ == '__main__':
    print('Part 1')
    part1(testlines)
    part1(data)
