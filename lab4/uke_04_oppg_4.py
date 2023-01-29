# oppgave 4a
# funksjon som sjekker lengden på en kode
def good_style(source_code):
    # en for-løkke som deler opp ved linje skift
    for line in source_code.splitlines():
        # tom teller variabel
        teller = 0
        # sjekker i inn i lengden av linjene
        for i in line:
            # legger til 1 for hvert tegn i linjen
            teller +=1 
            # om lengden er 80 eller mer, så er det dårlig 
            if teller >= 80:
                return False
    # om if-løkken sin betingelser knyttet mot lengden ikke gjøres
    # returnerer den True
    return True

# oppgave 4b
#  funksjon som skal lese gjennom filen og sjekke om den har bra stil
def good_style_from_file(filename):
    # åpner filen på filnavnet og kaller den for f
    with open(filename, "rt") as f:
        # definerer en variabel kode som er det samme som å lese filen
        kode = f.read()
        # returnerer returverdien fra funksjonen i 4a
        return good_style(kode)

