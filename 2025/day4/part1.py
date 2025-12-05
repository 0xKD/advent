# go over each position in the grid, and then "taint" the neighbours (+1 to their "dirty" flag)
# if this is the last time any of them can be touched and they are dirty<4 and having a roll,
# increment final counter with + 1
# last-time-access - if i,j (current pos) is greater than cell_i+1,cell_j+1 (for any cell)
# cells at the right edge will reach this sooner (no i+1 for them, so can run on cell_i, cell_j+1)


def get_input(f):
    with open(f, "r") as inp:
        return [_.strip() for _ in inp.read().splitlines()]


def get_positions_to_mark(i, j):
    neighbours = [
        (i - 1, j - 1),
        (i, j - 1),
        (i + 1, j - 1),
        (i - 1, j),
        # (i, j),
        (i + 1, j),
        (i - 1, j + 1),
        (i, j + 1),
        (i + 1, j + 1),
    ]
    # avoid negative indexing
    return [(i, j) for i, j in neighbours if (i >= 0 and j >= 0)]


def main(f):
    grid = get_input(f)
    rows, cols = len(grid), len(grid[0])
    marked = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == ".":
                pass
            elif grid[i][j] == "@":
                for pos in get_positions_to_mark(i, j):
                    try:
                        marked[pos[0]][pos[1]] += 1
                    except IndexError:
                        pass

    accessible = 0
    # Can avoid this iteration by checking/incrementing counter
    # during the last time each neighbour is marked
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "@" and marked[i][j] < 4:
                accessible += 1
    print(accessible)


if __name__ == "__main__":
    main("input.txt")
