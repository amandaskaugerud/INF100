import matplotlib.pyplot as plt
import csv

# steg 1 lese filen
with open("lab11\Akvakulturregisteret.csv", "rt", encoding='iso-8859-1') as f:
    tabell = list(csv.reader(f, delimiter=';'))

# steg 2: lage 2D liste + headers
headers = tabell[1]
colname_to_i = {}
# funksjon som tar inn en string og gir plassen til den stringen i listen
for i in range(len(headers)):
    colname = headers[i]
    colname_to_i[colname] = i
data = tabell[2:]

# steg filtrere tabell slik at vi kun har ferskvann og saltvann

def filter_data(data, must_match_value,col):
    filtered_data = []
    for row in data:
    # hvis row er ferskvann, legg til i fresh_water_data
        water_environment = row[col]
        if water_environment == must_match_value:
            filtered_data.append(row)
    return filtered_data

fresh_water_data = filter_data(data, "FERSKVANN", colname_to_i["VANNMILJØ"])
salt_water_data = filter_data(data, "SALTVANN", colname_to_i["VANNMILJØ"])

# steg 3: finne x'er og y'er for posisjonene
xs_salt = list()
ys_salt = list()
for row in salt_water_data:
    # finn rad med x-koordinat, legg til i xs
    i = colname_to_i["N_GEOWGS84"]
    x = float(row[i])
    xs_salt.append(x)
    # finne kolonnen med y-koordinat, legg til i ys
    i = colname_to_i["Ø_GEOWGS84"]
    y = float(row[i])
    ys_salt.append(y)
plt.scatter(x = ys_salt, y = xs_salt, s=10, alpha=0.2, label="saltvann")

xs_fresh = list()
ys_fresh = list()
for row in fresh_water_data:
    # finn rad med x-koordinat, legg til i xs
    i = colname_to_i["N_GEOWGS84"]
    x = float(row[i])
    xs_fresh.append(x)
    # finne kolonnen med y-koordinat, legg til i ys
    i = colname_to_i["Ø_GEOWGS84"]
    y = float(row[i])
    ys_fresh.append(y)

plt.scatter(x = ys_fresh, y = xs_fresh, alpha=0.2, s=10 ,label="ferskvann")
plt.legend()
plt.show()