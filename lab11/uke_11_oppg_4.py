# oppgave 4
# del A
def simplified_pig_latin(word):
    # gjør om ordet til lowercase
    word = word.lower()
    # sjekker om den første bokstaven er en vokal
    if word[0] in "aeiouy":
        # legger til ay på slutten
        pig_latin_word = word + "hay"
    else:
    # legger til den første bokstaven til slutten med ay
        pig_latin_word = word[1:] + word[0] + "ay"
    return pig_latin_word

# del B
def sentence_to_simplified_pig_latin(sentence):
    # gjør ordene i setningen om til lowercase
    sentence = sentence.lower()
    # tom variabel som tar inn slutt setningen
    pig_latin_sentence = ""
    # løepr gjennom ord i setningen
    for word in sentence.split(" "):
        # kaller på funksjon fra del A
        pig_latin_word = simplified_pig_latin(word)
        # legger til ordet i setningsvaribelen
        pig_latin_sentence += pig_latin_word + " "
    # returnerer setningen med strippet for mellomrom før og etter strengen
    return pig_latin_sentence.strip()
