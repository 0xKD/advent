def get_input():
    with open("input.txt") as f:
        yield from f.readlines()


def turn_on_pixels(state, size):
    width, height = [int(_) for _ in size.split("x")]
    for row in range(height):
        for col in range(width):
            state[row][col] = "#"


def rotate_pixels(state, delta, row=None, column=None):
    # naming/args could be better
    if row is not None:
        _, val = row.split("=")
        val = int(val)
        line = state[val]
        state[val] = line[-delta:] + line[:-delta]
    elif column is not None:
        _, val = column.split("=")
        val = int(val)
        line = [row[val] for row in state]
        modified = line[-delta:] + line[:-delta]
        for index, modified_val in enumerate(modified):
            state[index][val] = modified_val
    else:
        raise ValueError("wut")


def main(width=50, height=6):
    state = [["."] * width for _ in range(height)]
    for line in get_input():
        instruction, *params = line.split()
        if instruction == "rect":
            coordinates, *_ = params
            turn_on_pixels(state, coordinates)
        elif instruction == "rotate":
            row_or_col, position, _, delta = params
            rotate_pixels(state, int(delta), **{row_or_col: position})
        else:
            raise ValueError(f"Unknown instruction {instruction}")

    lit = sum(1 if pixel == "#" else 0 for pixel in "".join("".join(_) for _ in state))
    # Part 1
    print(lit)
    print("-" * width)
    # Part 2
    print("\n".join("".join(_) for _ in state))


if __name__ == "__main__":
    main()
