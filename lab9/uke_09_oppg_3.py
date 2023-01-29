def rotate(grid):
    # tom resultat rutenett
    resultat = []
    # løper gjennom kolonnene
    for col in range(len(grid[0])):
        # lager en tom kolonne liste som skal ta inn kolonne-verdiene
        col_liste = []
        # løper gjennom rad slik at det blir samme kolonne i ulike rad
        for row in range(len(grid)):
            # legger til verdien i kolonnelisten
            col_liste.append(grid[row][col])
        # legger så til kolonnelisten i resultat rutenettet
        resultat.append(col_liste)
    return resultat
