def get_input(f):
    ranges = []
    ingredients = []
    with open(f, "r") as inp:
        for line in inp.readlines():
            if line == "\n":
                continue
            try:
                s, e = line.strip().split("-")
                ranges.append([int(s), int(e)])
            except ValueError:
                ingredients.append(int(line.strip()))

    return ranges, ingredients


def main(f):
    count = 0
    ranges, ingredients = get_input(f)
    for i in ingredients:
        for s, e in ranges:
            if s <= i <= e:
                count += 1
                break
    print(count)


if __name__ == "__main__":
    main("input.txt")
