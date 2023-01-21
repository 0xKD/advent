def get_input():
    with open("input.txt") as f:
        yield from f.readlines()


def update_in_bracket(char, in_brackets):
    if char == "[" and not in_brackets:
        return True
    elif char == "]" and in_brackets:
        return False
    elif char == "[" and in_brackets or char == "]" and not in_brackets:
        raise ValueError("Invalid sequence")


def main():
    count = 0
    for line in get_input():
        in_brackets, abba, hypernet_abba = False, False, False
        for index, start in enumerate(line[:-3]):
            in_brackets_new = update_in_bracket(start, in_brackets)
            if in_brackets_new is not None:
                in_brackets = in_brackets_new
                continue

            # abba characters
            one, two, three, four = line[index : index + 4]
            if one == two:
                continue
            if one == four and two == three:
                if in_brackets:
                    hypernet_abba = True
                else:
                    abba = True
                continue

        if abba and not hypernet_abba:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
