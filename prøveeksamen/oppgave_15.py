import csv
#  del A
def sortere_fylker_og_kommuner():
    fylker = {}
    kommuner = {}
    alle_kommuner = []
    with open('prøveeksamen/NO_ADM12.csv', 'rt', encoding='utf-8') as f:
        data = csv.reader(f, delimiter=";")
        for line in data:
            if line[5] == "ADM1":
                fylker[line[7]] = line[2]
            elif line[5] == "ADM2":
                kommuner.setdefault(line[7],[])
                kommuner[line[7]].append((int(line[9]),line[2], float(line[3]), float(line[4])))
                alle_kommuner.append((int(line[9]),line[2]))
    return fylker, kommuner, alle_kommuner
fylker, kommuner, alle_kommuner = sortere_fylker_og_kommuner()

# del B
def fem_minste_kommuner(kommuner):
    sortert_kommuner = sorted(kommuner)
    print("De fem minste kommunene")
    for befolkning, navn,_,_ in sortert_kommuner[:5]:
        print(f"{navn:15} {befolkning}")
    print()

def fem_største_kommuner(kommuner):
    sortert_kommuner = sorted(kommuner)
    print("De fem største kommunene")
    for befolkning, kommune_navn,_,_ in sortert_kommuner[-5:]:
        print(f"{kommune_navn:15} {befolkning}")
    print()

def nordligste_kommune(kommuner):
    sortert_kommuner = sorted(kommuner)
    bredde = sortert_kommuner[0][2]
    lengde = sortert_kommuner[0][-1]
    navn = sortert_kommuner[0][1]
    print("Nordligste kommunen")
    for i in range(len(sortert_kommuner)):
            if sortert_kommuner[i][2] > bredde:
                bredde = sortert_kommuner[i][2]
                lengde = sortert_kommuner[i][-1]
                navn = sortert_kommuner[i][1]
    print(f"{navn:15} {bredde:5} N {lengde} Ø")
    print()

def sorligste_kommune(kommuner):
    sortert_kommuner = sorted(kommuner)
    bredde = sortert_kommuner[0][2]
    lengde = sortert_kommuner[0][-1]
    navn = sortert_kommuner[0][1]
    print("Sørligste kommunen")
    for i in range(len(sortert_kommuner)):
        if sortert_kommuner[i][2] < bredde:
            bredde = sortert_kommuner[i][2]
            lengde = sortert_kommuner[i][-1]
            navn = sortert_kommuner[i][1]
    print(f"{navn:15} {bredde:5} N {lengde} Ø")
    print()

def print_county(name):
    print(name)
    for key in fylker:
        if fylker[key] == name:
            kommuner_i_fylket = kommuner[key]
            fem_minste_kommuner(kommuner_i_fylket)
            fem_største_kommuner(kommuner_i_fylket)
            nordligste_kommune(kommuner_i_fylket)
            sorligste_kommune(kommuner_i_fylket)

# del C
while True:
    request = input("Search word (q to quit)? ")
    if request == "q":
        break
    
    name = None
    for adm1code, fylke in fylker.items():
        if request.lower() in fylke.lower():
            name = fylke
    
    if name == None:
        print("Not found. Try again")
        continue
    
    print_county(name)

