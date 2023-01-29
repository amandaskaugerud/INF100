import csv

with open("lab12/Akvakulturregisteret.csv", "rt", encoding='iso-8859-1') as f:
    tabell = list(csv.reader(f, delimiter=";"))

fiskearter = dict()
for row in range(2,len(tabell)):
    if tabell[row][12] not in fiskearter:
        fiskearter[tabell[row][12]] = 1
    else:
        fiskearter[tabell[row][12]] += 1

for i in sorted(fiskearter.keys()):
    print(f"{i}: {fiskearter[i]}")