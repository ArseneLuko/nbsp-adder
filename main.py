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
    for positon, word in enumerate(text):
        if len(word) == 1:
            text[positon] += '&nbsp;'
            next_word = text.pop(positon + 1)
            text[positon] += next_word
    
    return ' '.join(text)

def main():
    text = """Ve schránce nebyl vložen text."""
    text = pyperclip.paste().split(' ')
    text = add_nbsp(text)
    pyperclip.copy(text)

if __name__ == "__main__":
    main()