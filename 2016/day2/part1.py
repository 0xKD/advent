DELTA = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
GRID = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def get_code(sequence: str, num):
    for s in sequence:
        delta_x, delta_y = DELTA[s]
        new_x, new_y = ((num - 1) % 3) + delta_x, ((num - 1) // 3) + delta_y
        if 0 <= new_x <= 2 and 0 <= new_y <= 2:
            num = GRID[new_y][new_x]
    return num


def main(instructions, start=5):
    for line in instructions:
        start = get_code(line, num=start)
        print(start, end="")


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        main(f.read().strip().split("\n"))
