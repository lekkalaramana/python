import sys
from math import log
DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def convert(s):
    """Convert a string to an integer."""
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}",
              file = sys.stderr)
        return -1

def string_log(string)
    convert = convert(string)
    return log(convert)

# def convert(s):
#     """Convert a string to an integer."""
#     num = -1
#     try:
#         number = ''
#         for token in s:
#             number += DIGIT_MAP[token]
#         num = int(number)
#         print(f"Conversion succeeded! num = {num}")
#     except (KeyError, TypeError):
#         print("Conversion failed!")
#     return num


# convert('two zero two two'.split())
#
# convert('around one two three'.split())
#
# convert(435)


# we check the above code changes by importing convert from exceptional

# from exceptional import convert
# convert('one three four eight'.split())
