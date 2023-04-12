# Catsay

## Description

__Catsay__ was heavily inspired by, and is a clone of __Cowsay by Tony Monroe__. Cowsay works mighty fine as it is. I made a small script so cowsay spits out random quotes whenever the terminal is opened.
However, its' ASCII art is way too big for my terminal. And so Catsay was born. Catsay is a rushed project, which I created while still learning Python. 

## Restrictions

Unlike Cowsay, Catsay will not accept arguments or quotes from the user. It is purely designed in a way that it spits out random quotes and ASCII art whenever the terminal is open. While much of the art being quite small to not take up much space. Quotes and Art needs to be preloaded into the script.  

## Customizing

`Says` folder contains all the ascii art used in the script. New Art can be added to this folder, name the extension `say` as in `cow.say` and include the file name `cow` part into the `file_list` list within the script.

Quotes can be embedded to the script itself, add custom quotes into the `quotes` list. Quotes need to be no more than 100 characters in length.

## Usage

Script and the `Says` folder must be in the same directory. Edit bashrc and include the following line to run the script as bash starts.

```
python3 path/to/the/script/from/home/Catsay.py
```

You can also pipe the output to `lolcat`.

## Notice

All ASCII art included in the script were created by numerous artists. They are not mine nor they belong to Catsay. They were included purely for fun and educational purposes. No copyright intended.
