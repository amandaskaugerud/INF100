# oppgave 1a
def remove_threes(a):
    while (3 in a):
        # fjerner deretter 3 fra listen
        a.remove(3)
    return a

# oppgave 1b
def every_fourth(a):
    # tom resultat variabel
    resultat = []
    # løper gjennom listen for å finne indeks til verdier i listen
    for i in range(0,len(a)):
        # sjekker om indeksen til verdien er 4 
        if i % 4 ==0:
            # legger så til den verdien med indeks 4
            resultat += [a[i]]
        # returnerer resultat
    return resultat

# oppgave 1c
def halve_values(a):
    # løper gjennom løkken for å finne indeks
    for i in range(0,len(a)):
        # en ny variabel som er halvparten av den orginale verdien
        a_i = a[i]/2
        # legger til den nye verdien av den gamle i listen
        a[i] = a_i
    # returnerer a
    return a

# oppgave 1d
def unique_values(a):
    # tom variabel som skal lagre svaret
    resultat = []
    # løper gjennom listen og finner indeks
    for i in range(0,len(a)):
        # sjekker først om verdien allerede ligger i lista for resultat
        if a[i] in resultat:
            # om den gjør det, så hopper den ut og begynner på nytt
            continue
        else:
            # hvis ikke, legges den til i lista
            resultat += [a[i]]
    # returnerer lista
    return resultat

# oppgave 1e
def add_list(a,b):
    # løper gjennom listen med en indeksert løkke
    for i,c in enumerate(a):
        # bruker løkken og indeksen til å legge sammen samme indeks verdier fra a og b i en ny variabel
        a_b = a[i] + b[i]
        # tilordner den nye variabelen sin verdi til indeksen av funnet verdi
        a[i] = a_b
    print(f"a = {a}")
    print(f"b = {b}")
