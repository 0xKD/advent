def get_rotations(f="input.txt"):
    with open(f, "r") as inp:
        lines = [(line[:1], int(line[1:])) for line in inp.readlines()]
    return [(-1 if direction == "L" else 1) * val for direction, val in lines]


def main(start=50, max_val=99):
    count = 0
    val = start
    for delta in get_rotations():
        val = val + delta
        if val < 0 or val > max_val:
            val = val % 100
        if val == 0:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
