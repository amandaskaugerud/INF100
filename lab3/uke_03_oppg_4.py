# oppgave 4a
# en funksjon som sjekker tverrsummen
def cross_sum(n):
    # tom variabel som blir løpende sum variabel
    tverrsum = 0
    # while-løkke som kjører så lenge argumentet til funksjonen er større enn null
    while n>0:
        # isolerer hvert siffer fra argumentet
        isolert = n%10
        # legger til det isolerte i tverrsummen
        tverrsum+=isolert
        # fjerner det siste sifferet i argumentet
        n = n//10
    # returnerer tverrsummen når n <=0
    return tverrsum

# oppgave 4b
# en funksjon som sjekker at kryss summen av det nth-leddet blir x
def nth_number_with_cross_sum_x(n,x):
    # definerer to tomme variabler som skal løpende endres
    nth = 0
    i = 0
    # fikk hjelp av Halvard Håvardsrud
    while nth < n:
        i += 1
        # sjekke om tverrsummen er lik gitt tverrsum
        if cross_sum(i) == x:
            nth += 1
    return i


