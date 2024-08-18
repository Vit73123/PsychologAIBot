from enum import Enum


class Colors(Enum):
    RESET = "\x1b[0m"  # reset; clears all colors and styles (to white on black)

    BOLD = "\x1b[1m"  # bold on (see below)
    ITALIC = "\x1b[3m"  # italics on
    UNDERLINE = "\x1b[4m"  # underline on
    INVERSE = "\x1b[7m"  # inverse on; reverses foreground & background colors
    STRIKETHROUGH = "\x1b[9m"  # strikethrough on

    BOLD_OFF = "\x1b[22m"  # bold off (see below)
    ITALIC_OFF = "\x1b[23m"  # italics off
    UNDERLINE_OFF = "\x1b[24m"  # underline off
    INVERSE_OFF = "\x1b[27m"  # inverse off
    STRIKETHROUGH_OFF = "\x1b[29m"  # strikethrough off

    FOREGROUND_DEFAULT = "\x1b[39m"  # set foreground color to default (white)
    BACKGROUND_DEFAULT = "\x1b[49m"  # set background color to default (black)

    FOREGROUND_LIGHT_WHITE = "\x1b[37m"  # set foreground color to white

    FOREGROUND_GRAY = "\x1b[37m"  # set foreground color to white
    FOREGROUND_DARK_GRAY = "\x1b[90m"  # set foreground color to black
    FOREGROUND_BLACK = "\x1b[30m"  # set foreground color to black

    FOREGROUND_RED = "\x1b[91m"  # set foreground color to red
    FOREGROUND_DARK_RED = "\x1b[31m"  # set foreground color to red

    FOREGROUND_GREEN = "\x1b[92m"  # set foreground color to green
    FOREGROUND_DARK_GREEN = "\x1b[32m"  # set foreground color to green

    FOREGROUND_YELLOW = "\x1b[93m"  # set foreground color to yellow
    FOREGROUND_DARK_YELLOW = "\x1b[33m"  # set foreground color to yellow

    FOREGROUND_BLUE = "\x1b[94m"  # set foreground color to blue
    FOREGROUND_DARK_BLUE = "\x1b[34m"  # set foreground color to blue

    FOREGROUND_PURPLE = "\x1b[95m"  # set foreground color to magenta (purple)
    FOREGROUND_DARK_PURPLE = "\x1b[35m"  # set foreground color to magenta (purple)

    FOREGROUND_CYAN = "\x1b[96m"  # set foreground color to cyan
    FOREGROUND_DARK_CYAN = "\x1b[36m"  # set foreground color to cyan

    BACKGROUND_GRAY = "\x1b[47m"  # set background color to white
    BACKGROUND_DARK_GRAY = "\x1b[100m"  # set background color to white
    BACKGROUND_BLACK = "\x1b[40m"  # set background color to black

    BACKGROUND_RED = "\x1b[101m"  # set background color to red
    BACKGROUND_DARK_RED = "\x1b[41m"  # set background color to red

    BACKGROUND_GREEN = "\x1b[102m"  # set background color to green
    BACKGROUND_DARK_GREEN = "\x1b[42m"  # set background color to green

    BACKGROUND_YELLOW = "\x1b[103m"  # set background color to yellow
    BACKGROUND_DARK_YELLOW = "\x1b[43m"  # set background color to yellow

    BACKGROUND_BLUE = "\x1b[104m"  # set background color to blue
    BACKGROUND_DARK_BLUE = "\x1b[44m"  # set background color to blue

    BACKGROUND_PURPLE = "\x1b[105m"  # set background color to magenta (purple)
    BACKGROUND_DARK_PURPLE = "\x1b[45m"  # set background color to magenta (purple)

    BACKGROUND_CYAN = "\x1b[46m"  # set background color to cyan
    BACKGROUND_DARK_CYAN = "\x1b[106m"  # set background color to cyan
