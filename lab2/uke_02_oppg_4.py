# oppgave 4
# funksjon som finner det første lengste ordet av tre
def find_first_longest_word(ord1,ord2,ord3):
    # finner lengden av argumentene til funksjonen
    len_ord1 = len(ord1)
    len_ord2 = len(ord2)
    len_ord3 = len(ord3)
    # finner ut hvem som er størst
    maks = max(len_ord1,len_ord2, len_ord3)
    # bruker if-setning til å finne ut av hvilken verdi som tilsvarer maks
    # og printer ut tilsvarende ord til terminalen
    if len_ord1 == maks:
        print(ord1)
    elif len_ord2 == maks:
        print(ord2)
    elif len_ord3 == maks:
        print(ord3)
