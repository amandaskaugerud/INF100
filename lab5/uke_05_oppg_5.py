# oppgave 5
def complement(seq):
    # en tom liste
    komplementstreng= []
    # bruker for-løkke til å løpe gjennom sekvensen
    for i in range(len(seq)):
        # sjekker så hva de ulike verdiene i sekvensen er 
        # legger deretter til tilsvarende verdi for komplement i tom liste variabel
        if seq[i] == "A":
            komplementstreng += "T"
        elif seq[i] == "C" :
            komplementstreng += "G"
        elif seq[i] == "T":
            komplementstreng += "A"
        else:
            komplementstreng += "C"
    # gjør listen om til en streng 
    komplementstreng = "".join(map(str,komplementstreng))
    # reverserer strengen
    # og printer til terminalen
    return komplementstreng[::-1]
