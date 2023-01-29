# funksjon som sjekker gjennomsnitt
def mean(a):
    # tom sum variabel
    sum_of_siffer = 0
    # løper gjennom listen med tall
    for siffer in a:
        # legger til tallet i sum 
        sum_of_siffer += siffer
    # returnerer gjennomsnittet
    return (sum_of_siffer/len(a))

# funksjon som sjekker medianen
def median(a):
    # sorterer listen på en ikke-destruktiv måte
    b = sorted(a)
    # sjekker om lista er ujevnt eller jevnt antall verdier
    # hvis den er et jevnt antall
    if len(b)%2 == 0:
        # finner de to midterste verdiene i lista
        midt1 = len(b)//2 - 1
        midt2 = len(b)//2
        # returnerer gjennomsnittet av de to midterste verdiene
        return (b[midt1]+b[midt2])/2
    else:
        # finner midterste verdi i en uvjevn liste
        midt_index = (len(b)-1)//2
        # returnerer den midterste verdien
        return b[midt_index]

# funksjon som sjekker typetallet
def mode(a):
    # lager et oppslagsverk
    occurence_dict = dict()
    # løper gjennom tall i listen
    for siffer in a:
        # endrer typen til siffer
        siffer = float(siffer)
        # sjekker at tallet ikke ligger i oppslagverket
        if siffer not in occurence_dict:
            # legger til at den er sett 1 gang
            occurence_dict[siffer] = 1
        else:
            # legger til at den er sett en gang til
            occurence_dict[siffer] += 1
    # finner den største verdien i oppslagsverket
    max_value = max(occurence_dict.values())
    # løper gjennom oppslagsverket
    for key, value in occurence_dict.items():
        # sjekker om en verdi er lik den største verdiene
        if value == max_value:
            # returnerer nøkkelen til den verdien
            return key

# en funksjons som bruker alle de andre laget
def cmd_main(numbers):
    # gjør om input til en liste med flyt-tall
    list_of_numbers = []
    for x in numbers:
        x = float(x)
        list_of_numbers.append(x)
    # bruker de andre metodene til å regne ut statistiske verdier
    gjennomsnittet = mean(list_of_numbers)
    medianen = median(list_of_numbers)
    typetallet = mode(list_of_numbers)
    # returnerer en svar setning
    return (f"\nGjennomsnitt: {gjennomsnittet}\nMedianen:     {medianen}\nTypetall:     {typetallet}")

if __name__ == "__main__":
    number_input = input("Regn ut statistiske gjennomsnitt for en liste.\nOppgi tallene du vil regne ut gjennomsnitt for, separert av mellomrom:\n").split()
    print(cmd_main(number_input))
