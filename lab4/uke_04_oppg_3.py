# en funksjon som finner hvilken plass en gitt karakter har
def find_nth_occurence(search_string,character,n):
    # tom telle variabel
    amount_character = 0
    # en for-løkke som løper gjennom lengden av strengen for å bruke i som index
    for i in range(len(search_string)):
        # sjekker om i index av strengen er lik ønsket karakter
        if character == search_string[i]:
            # legger til en på hvor ofte jeg finner karakteren
            amount_character+=1
            # hvis da mengden er lik antall forekomster n
            # så returnerer den indeksen
            if amount_character == n:
                return i
    # om det ikke skulle være noe forekomst i det hele tatt
    # returnere -1
    return -1

