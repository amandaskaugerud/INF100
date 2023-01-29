def mix(s1,s2):
    # en tom resultat variabel som blir skrevet ut til slutt
    resultat = ""
    # finner det lengste ordet
    lengst = max(len(s1), len(s2))
    # sjekker om det er noen tomme str
    if s1 == "":
        # hvis det er det bare returnere det andre ordet 
        return s2
    elif s2 == "":
        return s1
    else:
        # en for løkke som løper gjennom det lengste ordet slik at alle symbolene blir med
        for i in range(0,lengst):
            # hvis indeksen er i lengden av str 1
            if i in range(len(s1)):
                    resultat += s1[i]
            # gjør det samme for str 2, sjekker om indeksen er i lengden av str
            if i in range(len(s2)):
                    resultat += s2[i]
        # returnerer tilslutt resultatet
        return resultat
