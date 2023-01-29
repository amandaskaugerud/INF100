# oppgave 7
# funksjon som sjekker om det er en lovlig trekant??
def is_legal_triangle(lengde1, lengde2,lengde3):
    # samler alle lengdene i en liste, lengder
    trekant = [lengde1,lengde2,lengde3]
    # løper gjennom listen for å sjekke typen til hver verdi i listen
    for verdi in trekant:
        if type(verdi) == str or type(verdi) == float:
            return False
        else:
            # sjekker at summen av to lengder er større enn den siste lengden
            if lengde1 < lengde2 + lengde3 and lengde2<lengde1+lengde3 and lengde3< lengde1+lengde2:
                return True
            else:
                return False
