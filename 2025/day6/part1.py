def main(f):
    with open(f, "r") as inp:
        *lines, operations = inp.readlines()

    ops = [_.strip() for _ in operations.split()]
    print(ops)
    answers = [1 if op == "*" else 0 for op in ops]
    for line in lines:
        values = line.split()
        # assert len(values) == len(answers) == len(ops)
        for col_idx, num in enumerate(values):
            if ops[col_idx] == "*":
                answers[col_idx] *= int(num)
            else:
                answers[col_idx] += int(num)
    print(sum(answers))


if __name__ == "__main__":
    main("input.txt")
