from collections import defaultdict, deque
from dataclasses import dataclass
import re


@dataclass
class BotData:
    values: set
    low_type: str = None
    low_id: int = None
    high_type: str = None
    high_id: int = None


VALUE_RE = re.compile(r"value (?P<val>\d+) goes to bot (?P<bot>\d+)")
BOT_RE = re.compile(
    r"bot (?P<bot>\d+) "
    r"gives low to (?P<low_type>\w+) (?P<low_id>\d+) "
    r"and high to (?P<high_type>\w+) (?P<high_id>\d+)"
)


def get_input():
    with open("input.txt") as f:
        yield from f.readlines()


def main():
    botmap = defaultdict(lambda: BotData(set()))
    output = defaultdict(list)
    queued = deque()

    def add_microchip_to_bot(bot_id, value):
        # Also enqueue if both values available
        values = botmap[bot_id].values
        values.add(int(value))
        if len(values) == 2:
            queued.append(bot_id)

    for line in get_input():
        if line.startswith("value"):
            val, bot_id = VALUE_RE.match(line).groups()
            add_microchip_to_bot(bot_id, val)
        elif line.startswith("bot"):
            data = BOT_RE.match(line).groupdict()
            bot_id = data.pop("bot")
            botmap[bot_id] = BotData(botmap[bot_id].values, **data)
        else:
            raise ValueError(f"Unknown instruction: {line}")

    while queued:
        bot = botmap[(bot_id := queued.popleft())]
        value_min, value_max = sorted(bot.values)
        instructions = (
            # (destination, identifier, microchip)
            (bot.low_type, bot.low_id, value_min),
            (bot.high_type, bot.high_id, value_max),
        )
        for (typ, id_, val) in instructions:
            if typ == "output":
                output[id_].append(val)
            elif typ == "bot":
                add_microchip_to_bot(id_, val)

        if bot.values == {17, 61}:
            # Part 1
            print(bot_id)

    # Part 2
    print(output["0"][0] * output["1"][0] * output["2"][0])


if __name__ == "__main__":
    main()
