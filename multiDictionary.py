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

    def searchWordLinear(self, words, language):
        if (language == "italian"):
            self.dizionario = dr.loadDictionary("./resources/Italian.txt")
        elif (language == "english"):
            self.dizionario = dr.loadDictionary("./resources/English.txt")
        elif (language == "spanish"):
            self.dizionario = dr.loadDictionary("./resources/Spanish.txt")
        newtext = self.replaceChars(words)
        parole = newtext.split(" ")
        errori = []
        corrette = []
        # se la parola è nel diz, allora ho true altrimenti false: quando è false aggiungo le parole alla lista da returnare
        for parola in parole:
            rww = rw.RichWord(parola)
            if self.dizionario.__contains__(parola + "\n"):
                # rww.corretta(True)
                corrette.append(parola)
            else:
                # rww.corretta(False)
                errori.append(parola)
        return errori

    def searchWordDichotomic(self, words, language):
        if (language == "italian"):
            self.dizionario = dr.loadDictionary("./resources/Italian.txt")
        elif (language == "english"):
            self.dizionario = dr.loadDictionary("./resources/English.txt")
        elif (language == "spanish"):
            self.dizionario = dr.loadDictionary("./resources/Spanish.txt")
        newtext = self.replaceChars(words)
        parole = newtext.split(" ")
        errori = []
        centro=int(len(self.dizionario)/2)
        for parola in parole:
            trovato = 0
            if(parola==self.dizionario[centro]):
                trovato=1
            elif(parola>self.dizionario[centro]):
                c=centro+1
                while(trovato==0 or c<len(self.dizionario)):
                    if(parola==self.dizionario[c]):
                        trovato=1
                    c=c+1
            elif (parola < self.dizionario[centro]):
                c = 0
                while (trovato == 0 or c<centro):
                    if (parola == self.dizionario[c]):
                        trovato = 1
                    c = c + 1
            if(trovato==0):
                errori.append(parola)
        return errori

    def replaceChars(self,text):
        chars = "\\'*_{}[]()>#+-.!$^;,-"
        for c in chars:
            text = text.replace(c, "")
            return text


