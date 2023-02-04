def get_input():
    with open("input.txt") as f:
        yield from f.read()


def main():
    decompressed, to_skip = 0, 0
    sequence = None

    for char in get_input():
        if to_skip:
            to_skip -= 1
            continue

        if sequence is not None:
            if char == ")":
                length, repetitions = [int(_) for _ in sequence.split("x")]
                to_skip = length
                sequence = None  # reset
                decompressed += length * repetitions
            else:
                sequence += char
        elif char == "(":
            sequence = ""
            continue
        else:
            decompressed += 1
    print(decompressed)


if __name__ == "__main__":
    main()
