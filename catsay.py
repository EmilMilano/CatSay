# New ASCII art text files must be put into the /Says directory.
# With extension renamed to 'say' as in 'cat.say'
# The directory structure must not be changed.
# Insert new quotes to Quotes.txt file, within a new line.

import random
import os
import sys

CONSOLE_INPUT = False if len(sys.argv) == 1 else True
SPEECH_BUBBLE = True
# Flip boolean to 'False' to just print the ascii art,
# without the speech bubble

absolute_path = os.path.join(os.path.dirname(__file__))
file_list = [i for i in os.listdir(
    absolute_path + '/Says') if i.endswith('.say')]

with open(absolute_path + '/Quotes.txt', 'r') as File:
    quotes = File.readlines()

if CONSOLE_INPUT is True:
    chosen_quote = ''

    if sys.argv[1] == '-f':
        chosen_file = f'{sys.argv[2]}.say'

        if len(sys.argv) >= 4:
            for i in range(3, len(sys.argv)):
                chosen_quote += f'{sys.argv[i]} '

        else:
            chosen_quote = (random.choice(quotes)).strip('\n')

    else:
        chosen_file = random.choice(file_list)

        for i in range(1, len(sys.argv)):
            chosen_quote += f'{sys.argv[i]} '

else:
    chosen_file = random.choice(file_list)
    chosen_quote = (random.choice(quotes)).strip('\n')


def assemble_string_short(length: int, quote: str) -> str:
    """Assemble a speech bubble ready for output"""

    return f"""
   {'-' * length}
 < {quote} >
   {'-' * length}
        \\
         \\

"""


def assemble_string_long(line1: str, line2: str) -> str:
    """Assemble a speech bubble ready for output (Long version)"""

    return f"""
    {'=' * 55}
  / {line1}\\
  \\ {line2}/
    {'=' * 55}
        \\
         \\

"""


def assemble_string_huge(string: str) -> str:
    """Assemble a speech bubble ready for output (uncapped)"""

    string_array = [i for i in string.split()]
    output_array = []
    output_string = ("_" * 57).center(60, ' ')
    assemble_line = ''

    for i in string_array:
        if len(assemble_line) < 45:
            assemble_line += i + ' '

        else:
            output_array.append(assemble_line)
            assemble_line = ''

    for i in range(len(output_array)):
        if i == 0:
            output_array[0] = (
                '\n' + '/ ' + output_array[0].center(55, ' ') + ' \\')

        elif output_array[i] == output_array[-1]:
            output_array[i] = (
                '\n' + '\\ ' + output_array[i].center(55, ' ') + ' /')

        else:
            output_array[i] = (
                '\n' + '| ' + output_array[i].center(55, ' ') + ' |')

    for i in output_array:
        output_string += i

    output_string += '\n' + ('-' * 57).center(60, ' ')
    output_string += """
            \\
             \\

"""

    return output_string


# Randomly choose a quote and a ascii art file
quote_length = len(chosen_quote)
if SPEECH_BUBBLE is True:
    output_string = ''
    # If Quote is short, assemble one-liner output string
    if quote_length <= 50:
        output_string = assemble_string_short(quote_length, chosen_quote)

    # Break quote to two lines
    elif quote_length <= 100:

        assembled_line_1 = ''
        assembled_line_2 = ''

        # Add max possible words to first line then move to next
        for i in chosen_quote.split():

            if len(assembled_line_1) < 45:
                assembled_line_1 += i + ' '

            else:
                assembled_line_2 += i + ' '

        # Center and add padding to the created strings
        assembled_line_1 = assembled_line_1.center(55)
        assembled_line_2 = assembled_line_2.center(55)

        output_string = assemble_string_long(
            assembled_line_1, assembled_line_2)

    else:
        output_string = assemble_string_huge(chosen_quote)

# Get directory of /Says folder and attempt read the file
file_name = f"{absolute_path}/Says/{chosen_file}"

with open(file_name, "r") as File:
    output_string += File.read()

# Output
print(output_string)
