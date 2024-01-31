import re

def validate_phone_re(number):
    pattern=r'^(02|042|09172)?[5-9]\d{4,6}$'
    return bool(re.search(pattern,number))

# s* - 0 или повече
# s+ - едно или повече
# s? - нула или едно
# s{m,n} - между m и n
#s{,n} - най-много n пъти s{m,} - най-малко m пъти

# Non-greedy search - put ? after the quantor
# If we try '[hH]o+' on Hooooooooooohoho without ? - (Hooooooooooo)hoho, with ? (Ho)oooooooooohoho
# . is one random symbol
# ^ - start of string
# $ - end of string
# | is or for the whole string that is on the left/right of it da(y|n)ce if we want to escape it like that
# [symbols] - matches exactly one of the symbols in the brackets
# ^ before a class is means everything but the class
# \d - digit \D - non-digit
# \s - whitespace symbol(\t\r\n\f\v) \S - non-whitespace symbol
# \w - letter or digit \W - non-leter and non-digit symbol
# \b - zero symbols, but border of word
# \1 - from the first group, \2 - from the second group, ...


# re methods
# re.search() - if string contains text from pattern -> re.Match object
# re.match() - if string starts with text from pattern -> re.Match object
# re.findall() - returns list of all matches in the string
# re.finditer() - the top one but returns iterator

re.search(r'(?:\w+) \d','The 4 Horsemen of the Apocalypse').group()