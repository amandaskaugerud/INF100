# Del A
def at_least_two(word,c):
    # tom telle variabel
    count = 0
    # gjør ordet om til en liste
    listed_word = list(word)
    # løper gjennom bokstav for bokstav
    for letter in word:
        # sjekker om noen av de er like
        if c == letter:
            count += 1
    # sjekker om telle variabelen er større eller lik 2
    if count >= 2:
        return True
    else: return False

# del B
def at_least_two_in_list(wordlist,c):
    # tom liste variabel
    list_word_letter = []
    # løper gjennom ord for ord
    for word in wordlist:
        # gjør ordet om til liste
        listed_word = list(word)
        # og bruker samme fremgangsmåte som i del A
        count = 0
        for letter in listed_word:
            if c == letter:
                count += 1
        if count >= 2:
            list_word_letter.append(word)
    # returnerer lengden av listen
    return len(list_word_letter)

# del C
# funksjon som leser filen
def read_file(path):
    with open(path,"rt",encoding="utf-8") as f:
        return f.read()
# hovedfunksjonen som sjekker om det er to av noe i filen
def at_least_two_in_file(path,c):
    # tom telle variabler for antall ord
    count_word = 0
    # leser gjennom filen
    file_content = read_file(path)
    # finner ord i teksten
    for word in file_content.splitlines():
        print(word)
        count_letter = 0
        # går gjennom bokstav og sammenlikner
        for letter in word:
            if c == letter:
                count_letter += 1
        # sjekker antall bokstaver
        if count_letter >= 2:
            count_word += 1
    # returnerer antall ord med riktig forekomst av bokstaven
    return count_word
print(at_least_two_in_file("lab10/wordlist.txt", "and"))