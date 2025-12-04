# noqa:brute

def get_ranges(f):
    with open(f, "r") as inp:
        return [r.strip().split("-") for r in inp.read().split(",")]


def main(f):
    invalid = 0
    ranges = get_ranges(f)
    for s, e in ranges:
        s = int(s)
        e = int(e)
        for _ in range(s, e + 1):
            sr = str(_)
            size = len(sr)
            if size % 2 != 0:
                continue
            if sr[size // 2 :] == sr[: size // 2]:
                invalid += _
    print(invalid)


if __name__ == "__main__":
    main(f="input.txt")
