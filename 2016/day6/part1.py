from collections import Counter


def get_input(file="input.txt"):
    with open(file, "r") as f:
        yield from f.readlines()


def main():
    lines = get_input()
    first = next(lines)
    collected = [Counter(_) for _ in first]
    for line in lines:
        for index, char in enumerate(line):
            collected[index].update(char)
    print("".join(_.most_common(1)[0][0] for _ in collected))


if __name__ == "__main__":
    main()
