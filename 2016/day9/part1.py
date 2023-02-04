def decompressed_length(inp: str, recurse=False) -> int:
    decompressed, to_skip = 0, 0
    sequence = None

    for index, char in enumerate(inp):
        if to_skip:
            to_skip -= 1
            continue

        if sequence is not None:
            if char == ")":
                length, repetitions = [int(_) for _ in sequence.split("x")]
                to_skip = length
                sequence = None  # reset
                multi = (
                    decompressed_length(
                        inp[index + 1 : index + 1 + length], recurse=recurse
                    )
                    if recurse
                    else length
                )
                decompressed += multi * repetitions
            else:
                sequence += char
        elif char == "(":
            sequence = ""
            continue
        else:
            decompressed += 1
    return decompressed


def main():
    with open("input.txt") as f:
        input_str = f.read()
        # Part 1
        print(decompressed_length(input_str))
        # Part 2
        print(decompressed_length(input_str, recurse=True))


if __name__ == "__main__":
    main()
