"""
Skript vloží do textu html entitu pro nedělitelnou mezeru '&nbsp;'.

Zatím funguje pro slova o délce jednoho znaku. Do budoucna budou doplněny 
další případy, kde je potřeba použít nedělitelnou mezeru, viz:
https://cs.wikipedia.org/wiki/Nezlomitelná_mezera#Využití

Skript je psán pro český jazyk. Pokud je spuštěn přímo, vytvoří objekt třídy
'NbspText()', načte text ze schránky, přidá na patřičná místa html entitu pro
nezlomitelnou mezeru a zkopíruje upravený text do schránky.

Autor: Lukáš Karásek / lukas@lukaskarasek.cz
GitHub: https://github.com/ArseneLuko
"""

import pyperclip

class NbspText:
    def __init__(self, text: str = ''):
        self.ENTITY = '&nbsp;'
        self.original_text = text
        self.positions = self._get_one_letter_positions()
        self.modified_text = self._add_nonbreaking_spaces()

    def __repr__(self):
        return f"Text ke zpracování:\n\"{self.original_text}\""
    
    def _get_list_of_words(self):
        return self.original_text.split(' ')
    
    def _get_one_letter_positions(self):
        positions = tuple()
        list_of_words = self._get_list_of_words()
        for position, word in enumerate(list_of_words):
            if not (position == len(list_of_words) - 1):
                if len(word) == 1:
                    positions += (position, )
        
        return positions
    
    def _add_nonbreaking_spaces(self):
        list_of_words = self._get_list_of_words()
        if self.positions:
            for position in range(len(list_of_words) - 1):
                if position in self.positions:
                    list_of_words[position] += self.ENTITY
                else:
                    list_of_words[position] += ' '
        
        return ''.join(list_of_words)

    def copy_modified_to_clipboard(self):
        pyperclip.copy(self.modified_text)
        print("Upravaný text zkopírován do schránky")
                

if __name__ == "__main__":
    NbspText(pyperclip.paste()).copy_modified_to_clipboard()