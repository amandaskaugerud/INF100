# del A av oppg 4
def shopping_list_to_dict(shopping_list_as_string):
    # lager et tomt oppslagsverk
    shopping_dict = dict()
    # løper gjennom str linje for linje
    for line in shopping_list_as_string.splitlines():
        # splitter linjen på antall og varen
        quantity,commodity = line.split()
        # legger til i oppslagsverket med varen som nøkkel
        shopping_dict[commodity] = int(quantity)
    return shopping_dict

# del B
def shopping_list_file_to_dict(path):
    # åpner og leser filen
    with open(path,"rt",encoding="utf-8") as f:
        # returnerer kallet fra funksjonen i del A
        return shopping_list_to_dict(f.read())
