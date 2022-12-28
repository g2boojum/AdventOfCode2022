# day8.py

testlines = '''30373
25512
65332
33549
35390'''.splitlines()

def build_grid(lines):
    num_lines = len(lines)
    num_cols = len(lines[0])
    grid = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            pos = (i, j)
            dig = int(c)
            grid[pos] = dig
    return grid


if __name__ == '__main__':
    testgrid = build_grid(testlines)
    print(testgrid)

