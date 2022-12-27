# day7.py

import pprint

testlines = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''.splitlines()

with open('day7.txt') as fp:
    data = fp.read().splitlines()


def build_tree(lines):
    cwd = {}
    rt = {'name': '/', 'parent': None, 'files': [], 'dirs': {}}
    for line in lines:
        if '$ cd /' in line:
            cwd = rt
        elif '$ cd ..' in line:
            cwd = cwd['parent']
        elif '$ cd' in line:
            dirname = line.split()[-1]
            cwd = cwd['dirs'][dirname]
        elif '$ ls' in line:
            continue
        elif 'dir' == line[:3]:
            dirname = line.split()[-1]
            cwd['dirs'][dirname] = {'name': dirname, 'parent': cwd,
                                    'files': [],
                                    'dirs': {}}
        else:
            # must be a file
            size, name = line.split()
            cwd['files'].append((int(size), name))
    return rt


def add_size(cwd):
    total = 0
    for size, _ in cwd['files']:
        total += size
    for dirname in cwd['dirs']:
        d = cwd['dirs'][dirname]
        if 'total' not in d:
            add_size(d)
        total += d['total']
    cwd['total'] = total


def walk_tree(cwd, lim):
    for dirname in cwd['dirs']:
        d = cwd['dirs'][dirname]
        for size in walk_tree(d, lim):
            yield size
    if cwd['total'] <= lim:
        yield cwd['total']


if __name__ == '__main__':
    tree = build_tree(testlines)
    add_size(tree)
    print('Test size = ', tree['total'])
    print('Test part 1 = ', sum(walk_tree(tree, 100000)))
    datatree = build_tree(data)
    add_size(datatree)
    print('Data size = ', datatree['total'])
    print('Data part 1 = ', sum(walk_tree(datatree, 100000)))


def walk_tree_sizes(cwd):
    for dirname in cwd['dirs']:
        d = cwd['dirs'][dirname]
        for size in walk_tree_sizes(d):
            yield size
    yield cwd['total']


def part2(lines):
    tree = build_tree(lines)
    add_size(tree)
    used = tree['total']
    fs_size = 70000000
    required = 30000000
    unused = fs_size - used
    additional = required - unused
    dirsizes = sorted(walk_tree_sizes(tree))
    for sz in dirsizes:
        if sz > additional:
            minsz = sz
            break
    return sz


if __name__ == '__main__':
    print('Test smallest dir size to be deleted: ', part2(testlines))
    print('Data smallest dir size to be deleted: ', part2(data))
