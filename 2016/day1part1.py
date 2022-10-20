from collections import namedtuple
from typing import List, Tuple

_INSTRUCTIONS = """
R2, L5, L4, L5, R4, R1, L4, R5, R3, R1, L1, L1, R4, L4, L1, R4, L4, R4, L3,
R5, R4, R1, R3, L1, L1, R1, L2, R5, L4, L3, R1, L2, L2, R192, L3, R5, R48,
R5, L2, R76, R4, R2, R1, L1, L5, L1, R185, L5, L1, R5, L4, R1, R3, L4, L3,
R1, L5, R4, L4, R4, R5, L3, L1, L2, L4, L3, L4, R2, R2, L3, L5, R2, R5, L1,
R1, L3, L5, L3, R4, L4, R3, L1, R5, L3, R2, R4, R2, L1, R3, L1, L3, L5, R4,
R5, R2, R2, L5, L3, L1, L1, L5, L2, L3, R3, R3, L3, L4, L5, R2, L1, R1, R3,
R4, L2, R1, L1, R3, R3, L4, L2, R5, R5, L1, R4, L5, L5, R1, L5, R4, R2, L1,
L4, R1, L1, L1, L5, R3, R4, L2, R1, R2, R1, R1, R3, L5, R1, R4
"""

INSTRUCTIONS = [
    [direction.strip(), int("".join(distance))]
    for direction, *distance in [_.strip() for _ in _INSTRUCTIONS.strip().split(",")]
]


def find_distance(x1, y1, x2, y2, distance=0):
    # probably a simpler way to go about this too
    if x1 == x2 and y1 == y2:
        return distance
    elif x1 == x2:
        return find_distance(x1, y1, x2, y1, distance + abs(y2 - y1))
    else:
        return find_distance(x1, y1, x1, y2, distance + abs(x2 - x1))


Instruction = namedtuple("Instruction", ["direction", "distance"])

COMPASS = ["N", "E", "S", "W"]
COMPASS_MOVE = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_new_facing(facing, direction):  # this can be made O(1)
    delta = 1 if direction == "R" else -1
    return COMPASS[(COMPASS.index(facing) + delta) % len(COMPASS)]


def find_destination(
    instructions: List[Instruction], pos=(0, 0), facing="N"
) -> Tuple[int, int]:
    if not instructions:
        return pos

    inst, *rest = instructions
    x, y = pos
    # can combine below three ops
    new_facing = get_new_facing(facing, inst.direction)
    delta_x, delta_y = COMPASS_MOVE[COMPASS.index(new_facing)]
    new_x, new_y = x + (delta_x * inst.distance), y + (delta_y * inst.distance)
    return find_destination(rest, pos=(new_x, new_y), facing=new_facing)


if __name__ == "__main__":
    dest = find_destination([Instruction(*_) for _ in INSTRUCTIONS])
    print(find_distance(0, 0, *dest))
