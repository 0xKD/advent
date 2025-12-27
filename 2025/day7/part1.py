"""
Rules (i/j mixed up...)
---
manifold(i,j) + space(i,j+1) => [beam(i,j+1)]
beam(i,j) + splitter(i,j+1) => [beam(i-1, j+2), beam(i+1, j+2)]
beam(i,j) + space(i,j+1) => [beam(i,j+1)]
"""

BEAM = "|"
MANIFOLD = "S"
SPACE = "."
SPLITTER = "^"


def get_input(f):
    with open(f, "r") as inp:
        return [list(_.strip()) for _ in inp.readlines()]


def main(f):
    field = get_input(f)
    size = len(field)
    splits = 0
    for j, line in enumerate(field):
        if j == size - 1:
            break
        for i, char in enumerate(line):
            # print(f">>>{i=},{j=}: {field[i][j]}")
            # could do switch
            if char == SPACE:
                continue
            elif char == MANIFOLD:
                field[j + 1][i] = BEAM
            elif char == BEAM and field[j + 1][i] == SPLITTER:
                field[j + 2][i - 1] = BEAM
                field[j + 2][i + 1] = BEAM
                splits += 1
            elif char == BEAM and field[j + 1][i] == SPACE:
                field[j + 1][i] = BEAM
    print(splits)


if __name__ == "__main__":
    main("input.txt")
