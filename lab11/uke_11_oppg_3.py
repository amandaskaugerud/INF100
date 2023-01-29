# oppgave 3 
# del A
def sub_course_positions(path):
    # åpner og lese filen
    with open(path, "rt", encoding='utf-8') as f:
        file_read = f.read()
    # lager et tomt oppslagsverk 
    d = {"forward": 0,"depth": 0}
    # løper gjennom hver linje i tekstfilen
    for line in file_read.splitlines():
        # splitter linjen på retning og verdi
        direction, value = line.split(" ")
        # sjekker hva direction er 
        if direction == "forward":
            d["forward"] += int(value)
        elif direction == "up": 
            d["depth"] -= int(value)
        elif direction == "down":
            d["depth"] += int(value)
    return d

# del B
def sub_course(path):
    # kaller på funksjonen fra del A
    dict_result = sub_course_positions(path)
    # regner sammen verdiene
    summen = dict_result["forward"] * dict_result["depth"]
    return summen

