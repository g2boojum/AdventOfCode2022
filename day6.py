# day 6

import collections

testlines = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb',
             'bvwbjplbgvbhsrlpgdmjqwftvncz',
             'nppdvjthqldpwncqszvftbrmjlhg',
             'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
             'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']
testpos = (7, 5, 6, 10, 11)

with open('day6.txt') as fp:
    data = fp.read()

def find_start_of_packet(line, bufsize):
    d = collections.deque(maxlen=bufsize)
    for i, c in enumerate(line):
        d.append(c)
        if bufsize == len(set(d)):
            return i, d


def part1(line):
    bufsize = 4 
    i, d = find_start_of_packet(line, bufsize)
    return i

if __name__ == '__main__':
    print('Part 1')
    for i, line in enumerate(testlines):
        assert testpos[i] == part1(line) + 1
    print('All test lines passed')
    print('Data: ', part1(data) + 1)

testpos = (19, 23, 23, 29, 26)

def part2(line):
    bufsize = 14
    i, d = find_start_of_packet(line, bufsize)
    return i


if __name__ == '__main__':
    print('Part 2')
    for i, line in enumerate(testlines):
        assert testpos[i] == part2(line) + 1
    print('All test lines passed')
    print('Data: ', part2(data) + 1)




