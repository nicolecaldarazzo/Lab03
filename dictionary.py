class Dictionary:
    def __init__(self,parole=[]):
        self.parole=parole

    def loadDictionary(self,path):
        input_file = open(path, "r", encoding='utf-8')
        riga = input_file.readline()
        par=[]
        while riga != "":
            par.append(riga)
            riga = input_file.readline()
        input_file.close()
        self.parole=par
        return par

    def printAll(self):
        self.parole


    @property
    def dict(self):
        return self._dict