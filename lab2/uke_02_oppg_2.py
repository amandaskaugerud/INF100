# oppgave 2
# en funksjon som sjekker skuddår
def is_leap_year(year):
    # sjekker om året er delelig med 4
    if year%4==0:
        # sjekker de resterende kravene for skuddår
        if year%100==0 and year%400!=0:
            return False
        else: 
            return True
    else:
        return False
