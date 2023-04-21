# Catsay

## Description

**Catsay** was heavily inspired by, and is a clone of **Cowsay by Tony Monroe**. Cowsay works mighty fine as it is. Cowsay can be included in bashrc. So it runs whenever bash starts.
However, its' ASCII can be too big for a small terminal window. Catsay was written with small ASCII arts to mitigate this issue. Catsay is a rushed project, expect bad, imperfect code.

## Usage

Like Cowsay, Catsay can accept arguments or quotes from the user. `-f` can be used to specify an ASCII file in the `Says` folder.
`-f` flag is always the first argument used. After that, text to be displayed can be entered.

Example below:

```
$ python catsay.py -f cat hello world
```

Catsay can also be made to work whenever bash is opened. Edit your `bashrc` file and add the program, so it runs when bash starts.

```
python3 path/to/the/script/from/home/Catsay.py
```

## Customizing

Location of the `Says` folder and `Quotes.txt` file must not be changed.

`Says` folder contains all the ASCII art used in the script.
New art can be added to this folder. Open a `text` file and copy the ASCII art into the file. Then rename the extension to `say` as in `cow.say`.

Texts, or `Quotes` to be displaed by the program can be added to the `Quotes.txt` file. Every new quote must be added to a new line.

You can also pipe the output to `lolcat`.

## Dependencies

1. `Python`

## Notice

All ASCII art included in the script were created by numerous artists. They are not mine nor they belong to Catsay. They were included purely for fun and educational purposes. No copyright intended.
