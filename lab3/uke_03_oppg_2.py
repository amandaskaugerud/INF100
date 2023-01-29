# en funksjon som lager rader med gange rekker
# fikk hjelp av Petter Kjørrefjord Ramstad til å lage funksjonen
def multiplication_table(n):
    # en løkke som lager rad nummer
    for i in range(1,n+1):
        # skriver ut rad nummeret 
        print(f"{i}:",end=" ")
        # løkke som ganger hoppet n med antall rader og tall i radene
        for x in range(1,n+1):
            print(i*x,end=" ")
        # fikk hjelp av Dag 
        print("")




