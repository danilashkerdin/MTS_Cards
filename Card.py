from enum import StrEnum, IntEnum


class Color(StrEnum):
    red = "red"
    yellow = "yellow"
    green = "green"
    blue = "blue"


class Action(StrEnum):
    reverse = "reverse"
    get_2_cards = "get_2_cards"
    skip = "skip"


class SpecialAction(StrEnum):
    get_4_cards = "get_4_cards"
    # change_color = "change_color"


class Digit(IntEnum):
    zero = 0  # карт с нулями в колоде уно - 4шт, а всех остальных цифр - по 8
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9


class Card:

    def render(self):
        pass


class ColoredCard(Card):

    color: Color
    value: Action | Digit | None


class SpecialCard(Card):
    # всегда меняет цвет
    actions: SpecialAction | None
