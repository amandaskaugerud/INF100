# del A
def can_be_made_of_letters(word,letters):
    # gjør om word til en liste
    word = list(word)
    # lager en tom liste som skal lagre tidligere tegn
    previous_char = []
    # løper gjennom listen word for å finne ulike verdiene i listen
    for char in word:
        # teller antall forekomster av et gitt tegn 
        x = letters.count(char)
        # sjekker om forekomsten er null, og kræsjer
        if x == 0:
            return False
        # sjekker at antall forekomster av et tegn er mindre enn tidligere lagrede tegn
        if x <= previous_char.count(char):
            return False
        previous_char += [char]
    return True




# del B
def possible_words(wordlist, letters):
    # lager en tom liste som skal ta vare på de mulige ordene som kan lages
    mulig_ord = []
    # en for løkke som løper gjennom lengden av listen for å finne indekser til verdiene i listen
    for i in range(len(wordlist)):
        # sjekker om det faktisk går an å lage ordet i ordlisten ved hjelp av funk fra del A
        # kaller på funksjonen med da hvert enkelt ord som argument per iterasjon og bokstavsamlingen
        if can_be_made_of_letters(wordlist[i], letters):
            # om det går an lagres ordet fra ordlisten i den nye listen
            mulig_ord = mulig_ord +[wordlist[i]]
    # helt til slutt returnerer funksjonen de mulige ordene
    return mulig_ord


# del C
def read_file(path):
    with open(path, "rt") as f:
        return f.read()

def possible_words_from_file(path, letters):
    # en tom liste som lagrer mulige ord
    mulige_ord = []
    # åpner og leser txt filen 
    file_content = read_file(path)
    # leser linje for linje eller i dette tilfellet ord for ord
    for linje in file_content.split():
        # sjekker om ordet/linjen kan lages av bokstavsamlingen
        if can_be_made_of_letters(linje,letters) == True:
            # om mulig lagres det i listen over mulige ord
            mulige_ord = mulige_ord + [linje]
    # returnerer tilslutt listen med mulige ord
    return mulige_ord
