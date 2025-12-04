def get_batteries(f):
    with open(f, "r") as f:
        return [_.strip() for _ in f.readlines()]


def main(f):
    total = 0
    batteries = get_batteries(f)
    for row in batteries:
        # index of largest non-last digit, and the other (largest)
        largest_non_last, the_other = 0, 1
        for idx, val in enumerate(row):
            if idx + 1 == len(row):
                continue
            if int(val) > int(row[largest_non_last]):
                largest_non_last = idx
                the_other = idx + 1
            if int(row[idx + 1]) > int(row[the_other]):
                the_other = idx + 1
        voltage = int(row[largest_non_last] + row[the_other])
        total += voltage
        # print(f">>>{row=}: {voltage=}, {total=}")
    print(total)


if __name__ == "__main__":
    main(f="input.txt")
