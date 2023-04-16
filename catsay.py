# New files must be put into the /Sys directory.
# The directory structure must not be changed.
# New Quotes can be inserted into the "quotes" list.
# However maximum allowable length is 100.

import random
import os

SPEECH_BUBBLE = True
# Flip boolean to 'False' to just print the ascii art,
# without speech bubble
output_string = ''
absolute_path = os.path.join(os.path.dirname(__file__)) + "/Says"

file_list = ["bat", "cards", "cat", "chonk_cat", "cloudgazer", "crab",
             "dapper_cat", "devil", "dolphin", "dragon", "egyptian", "fish",
             "flintstone", "four_bears", "gun", "hatter", "hummingbird",
             "kitty_cat", "mermaids", "octopus", "owl", "phoenix",
             "southpark", "squidward", "swans", "turtle", "tux", "tux_stare",
             "twin_cat", "whale"]

quotes = ["Let me sudo rm -rf", "Its FOSS!", "Arch Btw",
          "neofetch neofetch neofetch", "Windows LMAO", "life | grep meaning",
          "That was not supposed to happen", "cowsay hello world",
          "import gravity", "goodbye world", "Password is password",
          "y2k", "*lightskin stare*", "*laughs in linux*",
          "COWABUNGA IT IS", "This was made in Python!",
          "Just had a little kernal panic", "F**k the User", "...",
          "cd nuts", "Goodmorning Starshine, Earth says Hello!",
          "WARNING CAPS LOCK ENABLED", "Oppai!!!! ^_^", "Kimochi..UwU",
          "JavaScript Vs the World", "Nvidia, F**k you", "What in tarnation?!",
          "Never gonna give up, Never gonna let you down, Never gonna run around and hurt you...",
          "Здравствуйте, товарищ! ☭"]


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
    """Assemble a speech bubble ready for out (Long version)"""

    return f"""
    {'=' * 55}
  / {line1}\\
  \\ {line2}/
    {'=' * 55}
        \\
         \\

"""


# Randomly choose a quote and a ascii art file
chosen_file = random.choice(file_list)
chosen_quote = random.choice(quotes)

quote_length = len(chosen_quote)

if SPEECH_BUBBLE is True:

    # If Quote is short, assemble one-liner output string
    if quote_length <= 50:
        output_string = assemble_string_short(quote_length, chosen_quote)

    # Break quote to two lines
    elif quote_length <= 100:

        line_length = 0
        assembled_line_1 = ''
        assembled_line_2 = ''

        # Add max possible words to first line then move to next
        for i in chosen_quote.split():

            line_length += len(i)

            if line_length < 45:
                assembled_line_1 += i + ' '

            else:
                assembled_line_2 += i + ' '

        # Center and add padding to the created strings
        assembled_line_1 = assembled_line_1.center(55)
        assembled_line_2 = assembled_line_2.center(55)

        output_string = assemble_string_long(
            assembled_line_1, assembled_line_2)

    else:
        print('Error! Quote too long!, Max length = 100 chars')

# Get directory of /Says folder and attempt read the file
file_name = f"{absolute_path}/{chosen_file}.say"

with open(file_name, "r") as File:
    output_string += File.read()

# Output
print(output_string)
