def sort_by_sign(a):
    # tom liste som tar inn alt sortert
    sortert = []
    # tomme lister til de ulike kravene av verdiene i oppgaven
    negativ = []
    null = []
    positive = []
    # løper gjennom løkken for å finne indeks til de ulike 
    # verdiene i listene
    for i in range(len(a)):
        # henter ut alle de negative verdiene
        if a[i] < 0:
            # lagrer de i negativ listen
            negativ += [a[i]]
        # henter ut alle null verdier 
        elif a[i] == 0:
            # lagrer de i null listen
            null += [a[i]]
        # henter ut at de positive verdiene
        elif a[i] > 0:
            # lagrer de i positiv listen
            positive += [a[i]]
    # legger til de ulike listene med extend 
    # slik at jeg får de som enkelt verdier og ikke liste i liste
    sortert.extend(negativ)
    sortert.extend(null)
    sortert.extend(positive)
    return sortert
