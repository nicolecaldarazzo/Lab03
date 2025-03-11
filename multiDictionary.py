import dictionary as d
import richWord as rw
from dictionary import Dictionary
dr = d.Dictionary()
class MultiDictionary:

    def __init__(self):
        self.dizionario = Dictionary()

    def printDic(self, language):
        diz = []
        if (language == "italian"):
            diz = dr.loadDictionary("./resources/Italian.txt")
        elif (language == "english"):
            diz = dr.loadDictionary("./resources/English.txt")
        elif (language == "spanish"):
            diz = dr.loadDictionary("./resources/Spanish.txt")
        return diz

    def searchWord(self, words, language):
        #chiamo il loadDictionary in base al linguaggio passato
        # cerco le parole nel dizionario chiamato
        if(language=="italian"):
            self.dizionario=dr.loadDictionary("./resources/Italian.txt")
        elif(language=="english"):
            self.dizionario=dr.loadDictionary("./resources/English.txt")
        elif(language=="spanish"):
            self.dizionario=dr.loadDictionary("./resources/Spanish.txt")
        newtext = self.replaceChars(words)
        parole = newtext.split(" ")
        errori=[]
        corrette=[]
        # se la parola è nel diz, allora ho true altrimenti false: quando è false aggiungo le parole alla lista da returnare
        for parola in parole:
            rww = rw.RichWord(parola)
            if self.dizionario.__contains__(parola):
                #rww.corretta(True)
                corrette.append(parola)
            else:
                #rww.corretta(False)
                errori.append(parola)
        return errori

    def replaceChars(self,text):
        chars = "\\'*_{}[]()>#+-.!$^;,-"
        for c in chars:
            text = text.replace(c, "")
            return text


