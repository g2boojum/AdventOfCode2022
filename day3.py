# day3.py

testlines = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()

with open('day3.txt') as fp:
    data = fp.read().splitlines()

def get_sacks(line):
    line = line.strip()
    sacksz = len(line)//2
    return line[:sacksz],line[sacksz:]

def sack_overlap(lhs, rhs):
    overlap = set(lhs) & set(rhs)
    return overlap.pop()

def get_priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 27

if __name__ == '__main__':
    print('Part 1')
    print('Test: ', sum(get_priority(sack_overlap(*get_sacks(line))) for line in testlines))
    print('Data: ', sum(get_priority(sack_overlap(*get_sacks(line))) for line in data))

# Part 2

def get_groups(lines):
    curr, rest = lines[:3], lines[3:]
    yield curr 
    while rest:
        curr, rest = rest[:3], rest[3:]
        yield curr

def get_badge(group):
    overlap = set(group[0]) & set(group[1]) & set(group[2])
    return overlap.pop()

if __name__ == '__main__':
    print('Part 2')
    print('Test: ', sum(get_priority(get_badge(group)) for group in get_groups(testlines)))
    print('Data: ', sum(get_priority(get_badge(group)) for group in get_groups(data)))




