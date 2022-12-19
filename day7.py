# day7.py

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
    rt = {'name':'/', 'parent':None, 'files':[], 'dirs':{}}
    cwd = rt
    for line in lines:
        if '..' in line:
            cwd = cwd['parent']
        elif 'cd' in line:
            dirname = line.split()[-1]
            cwd = cwd['dirs'][dirname]
        elif 'ls' in line:
            continue
        elif 'dir' in line:
            dirname = line.split()[-1]
            cwd['dirs'][dirname] = {'name':dirname, 'parent':cwd, 'files':[],
                                    'dirs': {}}
        else:
            # must be a file
            size, name = line.split()
            cwd['files'].append((int(size), name))
    return rt

if __name__ == '__main__':
    tree = build_tree(testlines)
    print(tree)


