import csv
def read_csv_file(path, **kwargs):
    with open(path, "rt", encoding='iso-8859-1' ) as f:
        return list(csv.reader(f, **kwargs))

def sum_of_column(path, col):
    summen = 0
    csv_file = read_csv_file(path)
        # går gjennom linje/rad i filen
    for row in csv_file:
        if len(row)-1>= col:
            if row[col].strip() != "":
                if row[col][0] in "0123456789":
                    summen += int(row[col])
    return float(summen)
print(sum_of_column("lab12/airport-codes.csv",3))

print("Tester sum_first_col... ", end="")
assert(42.0 == sum_of_column("lab12/foo.csv", 0))
assert(95.0 == sum_of_column("lab12/foo.csv", 1))
assert(0.0 == sum_of_column("lab12/foo.csv", 2))
assert(76363.0 == sum_of_column("lab12/Statistikk_Tilsyn_ar.csv", 1))
assert(46007.0 == sum_of_column("lab12/Statistikk_Tilsyn_ar.csv", 2))
assert(5024518.0 == sum_of_column("lab12/airport-codes.csv", 3))
print("OK")
