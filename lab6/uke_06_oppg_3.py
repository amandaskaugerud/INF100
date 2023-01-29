# oppgave 3
def median(a):
    # sorterer listen på en ikke-destruktiv måte
    b = sorted(a)
    # sjekker om lista er ujevnt eller jevnt antall verdier
    # hvis den er et jevnt antall
    if len(b)%2 == 0:
        # finner de to midterste verdiene i lista
        midt1 = len(b)//2 - 1
        midt2 = len(b)//2
        # returnerer gjennomsnittet av de to midterste verdiene
        return (b[midt1]+b[midt2])/2
    else:
        # finner midterste verdi i en uvjevn liste
        midt_index = (len(b)-1)//2
        # returnerer den midterste verdien
        return b[midt_index]
