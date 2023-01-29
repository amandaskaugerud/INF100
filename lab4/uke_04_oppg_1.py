# oppgave 1 
# en funksjon som tar inn tre parametre
# den skal sette inn en str på en gitt indeksplass i en hovedstr
def insert_at(source_string, index, insertion_string):
    # gjør str om til liste
    source_string = list(source_string)
    # setter inn oppgitt str på gitt indeks plass
    source_string.insert(index,insertion_string)
    # gjør om til en str igjen
    source_string = ''.join(source_string)
    # returnerer hele hovedstr
    return source_string

