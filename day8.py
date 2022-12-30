# day8.py

import numpy as np

testlines = '''30373
25512
65332
33549
35390'''.splitlines()

with open('day8.txt') as fp:
    data = fp.read().splitlines()


def build_grid(lines):
    grid = np.array([[int(c) for c in line] for line in lines])
    return grid


def build_maxgrid_NS(grid):
    maxgrid = np.zeros(grid.shape)
    numrows, numcols = grid.shape
    for col in range(numcols):
        maxval = -1 # no trees before this one
        maxgrid[0, col] = maxval
        for row in range(1,numrows):
            curr = grid[row-1, col]
            if curr > maxval:
                maxval = curr
            maxgrid[row, col] = maxval
    return maxgrid


def build_maxgrid_SN(grid):
    maxgrid = np.zeros(grid.shape)
    numrows, numcols = grid.shape
    for col in range(numcols):
        maxval = -1 # no trees before this one
        maxgrid[numrows-1, col] = maxval
        for row in range(numrows-2, -1, -1):
            curr = grid[row+1, col]
            if curr > maxval:
                maxval = curr
            maxgrid[row, col] = maxval
    return maxgrid


def build_maxgrid_WE(grid):
    maxgrid = np.zeros(grid.shape)
    numrows, numcols = grid.shape
    for row in range(numrows):
        maxval = -1 # no trees before this one
        maxgrid[row, 0] = maxval
        for col in range(1, numcols):
            curr = grid[row, col-1]
            if curr > maxval:
                maxval = curr
            maxgrid[row, col] = maxval
    return maxgrid


def build_maxgrid_EW(grid):
    maxgrid = np.zeros(grid.shape)
    numrows, numcols = grid.shape
    for row in range(numrows):
        maxval = -1 # no trees before this one
        maxgrid[row, numcols-1] = maxval
        for col in range(numcols-2, -1, -1):
            curr = grid[row, col+1]
            if curr > maxval:
                maxval = curr
            maxgrid[row, col] = maxval
    return maxgrid


def part1(lines):
    grid = build_grid(lines)
    numrows, numcols = grid.shape
    maxgrid_NS = build_maxgrid_NS(grid)
    maxgrid_SN = build_maxgrid_SN(grid)
    maxgrid_WE = build_maxgrid_WE(grid)
    maxgrid_EW = build_maxgrid_EW(grid)
    numvisible = 0
    for row in range(numrows):
        for col in range(numcols):
            curr = grid[row, col]
            if (curr > maxgrid_NS[row, col] or
                curr > maxgrid_SN[row, col] or
                curr > maxgrid_WE[row, col] or
                curr > maxgrid_EW[row, col]):
                numvisible += 1
    return numvisible

if __name__ == '__main__':
    testvis = part1(testlines)
    print('Test number of visible trees: ', testvis)
    datavis = part1(data)
    print('Data number of visible trees: ', datavis)


def get_scenic_score(pos, grid):
    numrows, numcols = grid.shape
    row, col = pos
    curr = grid[row, col]
    # N of pos
    vis_N = 0
    for i in range(row-1, -1, -1):
        vis_N += 1
        if grid[i, col] >= curr:
            break
    # S of pos
    vis_S = 0
    for i in range(row+1, numrows):
        vis_S += 1
        if grid[i, col] >= curr:
            break
    # W of pos
    vis_W = 0
    for j in range(col-1, -1, -1):
        vis_W += 1
        if grid[row, j] >= curr:
            break
    # E of pos
    vis_E = 0
    for j in range(col+1, numcols):
        vis_E += 1
        if grid[row, j] >= curr:
            break
    return vis_N*vis_S*vis_W*vis_E


def part2(lines):
    grid = build_grid(lines)
    ss_grid = np.zeros(grid.shape)
    numrows, numcols = grid.shape
    for row in range(numrows):
        for col in range(numcols):
            ss_grid[row, col] = get_scenic_score((row, col), grid)
    return ss_grid.max()

if __name__ == '__main__':
    print('Part 2')
    print()
    print('Test lines: max scenic score = ', part2(testlines))
    print('Data lines: max scenic score = ', part2(data))
