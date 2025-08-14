"""
Skript vloží html entitu pro nedělitelnou mezeru '&nbsp;' na potřebná místa,
zatím funguje pro slova o délce jednoho znaku. Do budoucna budou doplněny 
další případy, kde je pottřeba použít nedělitelnou mezeru, viz:
https://cs.wikipedia.org/wiki/Nezlomitelná_mezera#Využití
Skript je psán primárně pro český jazyk.
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
    text = """zapomněl si označit text a vložit jej do schránky. A tak jsem neměl s čím pracovat, tvůj script"""
    text = pyperclip.paste().split(' ')
    text = add_nbsp(text)
    pyperclip.copy(text)

if __name__ == "__main__":
    main()