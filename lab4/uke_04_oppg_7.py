# oppgave 7a
from uke_04_oppg_3 import find_nth_occurence
def get_impact(line):
    # bruker funk fra oppg 3 til å finne indeksen til andre og tredje semikolon
    andre_forekomst = find_nth_occurence(line,";",2)
    tredje_forekomst = find_nth_occurence(line, ";",3)
    # beskjærer strengen basert på indeksen og slik at jeg ikke får med semikolon
    impact = line[andre_forekomst+1:tredje_forekomst]
    # # gjør beskjæringen om til en flyttall
    impact = float(impact)
    # returnerer så beskjæringen
    return impact

# oppgave 7b
def filter_earthquakes(earthquake_csv_string,treshold):
    overskrift_lengde = int(earthquake_csv_string.find("\n"))
    nye_earthquake_csv_string = earthquake_csv_string[overskrift_lengde+1:]
    svar = earthquake_csv_string[0:overskrift_lengde+1]
    for linje in nye_earthquake_csv_string.splitlines():
        if get_impact(linje) > treshold:
            svar += linje + "\n"
    return svar

# oppgave 7c
def read_file(path):
    with open(path, "rt", encoding='utf-8') as f:
        return f.read()

def write_file(path, contents):
    with open(path, "wt", encoding='utf-8') as f:
        f.write(contents)

def filter_earth_quakes_file(source_filename, target_filename, treshold):
    file_content = read_file(source_filename)
    new_content = filter_earthquakes(file_content,treshold)
    write_file(target_filename, new_content)

print("Tester filter_earthquakes_file... ", end="")
filter_earth_quakes_file("lab4\earthquakes_simple.csv",
"lab4/earthquakes_above_7.csv", 7.0)

expected_value = """\
id;location;impact;time 
us100068jg;Northern Mariana Islands;7.7;2016-07-29 17:18:26 
us10006d5h;New Caledonia;7.2;2016-08-11 21:26:35 
us10006exl;South Georgia Island region;7.4;2016-08-19 03:32:22
"""
assert(expected_value == read_file("lab4\earthquakes_above_7.csv")) #den gir feil fordi det er et eller annet som går galt i sammenlikningen mellom """ og ikke sånn streng, tror jeg
print("OK")

# denne fungerer i redo_lab_4.py

# Manuell test: Finn earthquakes_above_7.csv, åpne og se at innholdet stemmer
