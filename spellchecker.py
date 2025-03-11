import time

import multiDictionary as md
from multiDictionary import MultiDictionary


class SpellChecker:

    def __init__(self):
        self.multiDiz = MultiDictionary()

    def handleSentence(self, txtIn, language):
        return self.multiDiz.searchWord(txtIn,language)

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


