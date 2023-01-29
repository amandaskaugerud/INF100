# Hvordan kjøre programmet :)
# begynn med å starte programmet ved å trykke på den tilsvarende "play" knappen
# deretter skriver dere inn filnavnet med alt inkuldert, typisk filnavn.csv eller liknende 
# videre så trykker dere enter_knappen, etter å ha skrevet inn filnavnet
# så er det bare å vente litt og deretter åpne samme fil med innskrevet filnavn


# åpner og leser filen
def lese_fil(path):
    # lager en tom liste som skal ta i mot data fra filen
    liste_med_data = []
    # åpner filen
    with open(path, "rt", encoding='utf-8') as f:
        # går igjennom filen og lagrer hver linje som en liste med hvert element splittet ved ,
        for line in f:
            liste_med_data.append(line.strip().split(","))
        return liste_med_data

# Lese og skrive til fil https://inf100.ii.uib.no/notat/strenger/#lese-og-skrive-til-fil; 28.11.2022
def write_file(path, contents):
    """ Writes the contents to the file with the given file path. If
    the file does not exist, it will be created. If the file does
    exist, its old content will be overwritten. """
    # åpner filen 
    with open(path, "wt", encoding='utf-8') as f:
        # går igjenom hver rad i data som er gitt
        for row in contents:
            # gjør listen om til en streng
            string_row = ",".join(row)
            # skriver strengen til filen med ny linje på hver ende
            f.write(string_row+"\n")

def sortere_data(path):
    # åpner filen
    data = lese_fil(path)
    # lager en 2d liste som skal ta inn endret informasjon
    new_data = []
    # legger til overskriftene i 2d listen
    new_data.append(["personnummer","medisin", "dato", "endring"])
    # går gjennom hver linje etter 0'te linje
    for line in data[1:]:
        # endrer slik at hver linje blir to nye
        # første legges til en linje med start for medisin
        new_line_start = line[0:3] + ["1"]
        new_data.append(new_line_start)
        # deretter legges til en linje med slutt for medisin
        new_line_end = line[:2] + [line[3]] + ["0"]
        new_data.append(new_line_end)
    # så sendes den nye 2d listen til write_file funksjonen
    return write_file(filnavn,new_data)

# ber brukeren skrive inn filnavnet som ønsker redigert
filnavn = input("Skriv inn filnavnet, navn.csv: ") 
# og kaller på funksjonen med gitt filnavn 
sortere_data(filnavn)
