# definerer en funksjon som skal skrive ut sju gangen
def multiples_of_seven_up_to(n):
    # sjekker om tallet er er delelig med 7
    if n%7==0:
        # finner ut hvor mange ledd n tilsvarer til
        antall = int(n/7)
        # en for-løkke som teller og skriver ut 7 gangen tilsvarende til antall ledd av n
        for i in range(1,antall):
            print(i*7)
    return antall

# def multiplesOfSeven(n):
#     i = 7
#     while (i<=n):
#         print(i)
#         i+=7
