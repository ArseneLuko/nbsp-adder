"""
Skript vloží do textu html entitu pro nedělitelnou mezeru '&nbsp;'.

Zatím funguje pro slova o délce jednoho znaku. Do budoucna budou doplněny 
další případy, kde je potřeba použít nedělitelnou mezeru, viz:
https://cs.wikipedia.org/wiki/Nezlomitelná_mezera#Využití

Skript je psán pro český jazyk.
Autor: Lukáš Karásek / lukas@lukaskarasek.cz
GitHub: https://github.com/ArseneLuko
"""

import pyperclip

def add_nbsp(text: list) -> str:
    for position, word in enumerate(text):
        if not (position == len(text) - 1):
            if len(word) == 1:
                text[position] += '&nbsp;'
            else:
                text[position] += ' '

    return ''.join(text)


def one_letter_positions(text):
    positions = tuple()
    for position, word in enumerate(text):
        if len(word) == 1:
            positions += (position, )

    return positions


def main():
    text = """Ve schránce nebyl vložen text."""
    text = pyperclip.paste().split(' ')
    # positions = one_letter_positions(text)
    text = add_nbsp(text)
    pyperclip.copy(text)

if __name__ == "__main__":
    main()