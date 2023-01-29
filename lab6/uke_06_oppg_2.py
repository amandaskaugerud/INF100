# oppgave 2
def alternate_sign_sum(a):
    # en tom sum variabel som skal endre seg løpende
    sum = 0
    # løper gjennom løkken for å hente index til verdiene i lista
    for i in range(len(a)):
        # bruker å finne annenhver av indexene til å legge til
        if i%2 == 0:
            sum = sum + a[i]
        # eller trekke fra og legger til i sum variabelen
        else:
            sum = sum - a[i]
    # returnerer sum
    return sum
