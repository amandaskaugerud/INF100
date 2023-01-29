# en funksjon som sjekker like tilfeller av tegn i strengene
def get_common_symbols(s1,s2):
    # tom variabel som lagrer resultat
    resultat = ""
    # en for-løkke som løper gjennom streng 1 slik at jeg kan bruke indeks i 
    for i in range(len(s1)):
        # sjekker om indeks i av streng 1 befinner seg i streng 2
        if s1[i] in s2:
            # sjekker deretter igjen, om det tegnet allerede finnes i resultat variablen
            if s1[i] in resultat:
                # begynner på nytt dersom den er allerede
                continue
            else:
                # legger til tegnet om det ikke allerede er der
                resultat += s1[i]
    # returnerer deretter resultat variabelen
    return resultat
