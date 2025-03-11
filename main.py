import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        errori = sc.handleSentence(txtIn,"italian")
        for errore in errori:
            print(errore)
        continue

    elif int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        errori=sc.handleSentence(txtIn,"english")
        for errore in errori:
            print(errore)
        continue

    elif int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        errori=sc.handleSentence(txtIn,"spanish")
        for errore in errori:
            print(errore)
        continue

    elif int(txtIn) == 4:
        break


