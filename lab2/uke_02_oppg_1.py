def find_longest_words(ord0,ord1,ord2):
    # finner lengden av ordene
    len_ord0 = len(ord0)
    len_ord1 = len(ord1)
    len_ord2 = len(ord2)
    # samler de i en lsite
    ord = [ord0, ord1, ord2]
    # finner den lengste ordet
    maks = max(len_ord0,len_ord1,len_ord2)
    # samler lengdene i en liste
    lengde = [len_ord0,len_ord1,len_ord2]
    # løper gjennom lengde-listen 
    for i in range(0,len(lengde)):
        # sjekker om det er noen av lengdene som tilsvarer maks lengde
        if lengde[i]==maks:
            # printer ut, dersom
            print (ord[i])

