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

# Filtrer data slik at vi kun har rader hvor gitt kolonne matcher verdi
def filter_data(data, col_num, threshold_low, threshold_high):
    filtered_data = []
    for row in data:
        if row[colname_to_i["LOK_ENHET"]] == "TN":
            cell_value = row[col_num].replace(",",".")
            cell_value = float(cell_value)
            if  threshold_low <= cell_value < threshold_high-1:
                filtered_data.append(row)
    return filtered_data

# Filtrerer data: finner punkter hvor vannmiljø er ferskvann og saltvann
førstekvartal_data = filter_data(data, colname_to_i["LOK_KAP"], 0,2000)
andrekvartal_data = filter_data(data, colname_to_i["LOK_KAP"],2000,4000)
tredjekvartal_data = filter_data(data, colname_to_i["LOK_KAP"],4000,6000)
fjerdekvartal_data = filter_data(data, colname_to_i["LOK_KAP"],6000,10000)


# Hent ut en gitt kolonne
def get_col(data, col_num):
    col = []
    for row in data:
        col.append(row[col_num])
    return col

# Plot 0-2000
førstekvartal_xs = get_col(førstekvartal_data, colname_to_i["Ø_GEOWGS84"])
førstekvartal_ys = get_col(førstekvartal_data, colname_to_i["N_GEOWGS84"])
plt.scatter(x=førstekvartal_xs, y=førstekvartal_ys, color="green",s=3, label="0-2000 TN")

# Plot 2000 - 4000
andrekvartal_xs = get_col(andrekvartal_data, colname_to_i["Ø_GEOWGS84"])
andrekvartal_ys = get_col(andrekvartal_data, colname_to_i["N_GEOWGS84"])
plt.scatter(x=andrekvartal_xs, y=andrekvartal_ys, color="orange", alpha=0.2,s=6, label="2000-4000 TN")

# Plot 4000-6000
tredjekvartal_xs = get_col(tredjekvartal_data, colname_to_i["Ø_GEOWGS84"])
tredjekvartal_ys = get_col(tredjekvartal_data, colname_to_i["N_GEOWGS84"])
plt.scatter(x=tredjekvartal_xs, y=tredjekvartal_ys, color="blue", alpha= 0.1, s=9, label="4000-6000 TN")

# Plot 6000 -->
fjerdekvartal_xs = get_col(fjerdekvartal_data, colname_to_i["Ø_GEOWGS84"])
fjerdekvartal_ys = get_col(fjerdekvartal_data, colname_to_i["N_GEOWGS84"])
plt.scatter(x=fjerdekvartal_xs, y=fjerdekvartal_ys, color="red", alpha= 0.1, s=12, label="6000--> TN")

plt.xlabel("Lengdegrad")
plt.ylabel("Breddegrad")

plt.legend()
plt.show()
