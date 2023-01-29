import csv
import matplotlib.pyplot as plt

# Lese inn filen
with open("lab12/Akvakulturregisteret.csv", "rt", encoding='iso-8859-1') as f:
    tabell = list(csv.reader(f, delimiter=";"))

# Dele opp tabellen i kolonnenavn (overskifter) og data
headers = tabell[1]
data = tabell[2:]

# Konverter alle tallverdier fra streng til float
for row in data:
    for i in range(len(row)):
        try:
            row[i] = float(row[i])
        except ValueError:
            pass

# Lage oppslagsverk kolonnenavn -> kolonnenummer (i)
colname_to_i = {}
for i in range(len(headers)):
    colname_i = headers[i]
    colname_to_i[colname_i] = i
# print(colname_to_i)
# Filtrer data slik at vi kun har rader hvor gitt kolonne matcher verdi
def filter_data(data, col_num, must_match_value):
    filtered_data = []
    for row in data:
        cell_value = row[col_num]
        if must_match_value in cell_value:
            filtered_data.append(row)
    return filtered_data

def filter_data_NOT(data, col_num, must_match_value):
    filtered_data = []
    for row in data:
        cell_value = row[col_num]
        if must_match_value not in cell_value:
            filtered_data.append(row)
    return filtered_data

# Filtrerer data: finner punkter hvor vannmiljø er ferskvann og saltvann
laks_data = filter_data(data, colname_to_i["ART"], "Laks")
ørret_data = filter_data(data, colname_to_i["ART"], "ørret")
fisk_data = filter_data_NOT(data, colname_to_i["PRODUKSJONSFORM"],"MATFISK" )


# Hent ut en gitt kolonne
def get_col(data, col_num):
    col = []
    for row in data:
        col.append(row[col_num])
    return col

# Plot laks
laks_xs = get_col(laks_data, colname_to_i["Ø_GEOWGS84"])
laks_ys = get_col(laks_data, colname_to_i["N_GEOWGS84"])
plt.scatter(x=laks_xs, y=laks_ys, color="green",s=10, label="laks")

# Plot ørret 
ørret_xs = get_col(ørret_data, colname_to_i["Ø_GEOWGS84"])
ørret_ys = get_col(ørret_data, colname_to_i["N_GEOWGS84"])
plt.scatter(x=ørret_xs, y=ørret_ys, color="orange", alpha=0.2,s=10, label="ørret")

# Plot alle andre dyr
fisk_xs = get_col(fisk_data, colname_to_i["Ø_GEOWGS84"])
fisk_ys = get_col(fisk_data, colname_to_i["N_GEOWGS84"])
plt.scatter(x=fisk_xs, y=fisk_ys, color="blue", alpha= 0.1, s=10, label="annet")

plt.xlabel("Lengdegrad")
plt.ylabel("Breddegrad")

plt.legend()
plt.show()
