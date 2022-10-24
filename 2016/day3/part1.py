def get_input(file="input.txt"):
    with open(file, "r") as f:
        return [
            [int(_) for _ in sides.strip().split()]
            for sides in f.read().strip().split("\n")
        ]


def main():
    print(sum((a + b > c and a + c > b and c + b > a) for a, b, c in get_input()))


if __name__ == "__main__":
    main()
