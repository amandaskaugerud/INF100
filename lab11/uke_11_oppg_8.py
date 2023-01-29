import csv
import matplotlib.pyplot as plt

tabell = []
with open("lab11\Statistikk_Tilsyn_ar.csv", "rt", encoding='iso-8859-1') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        tabell.append(row)

tabell.remove(tabell[0])
aar = []
antall_tilsyn = []
antall_med_tilsyn = []
for row in tabell:
    aar.append(int(row[0]))
    antall_tilsyn.append(int(row[1]))
    antall_med_tilsyn.append(int(row[2]))

# plotting the points 
plt.plot(aar, antall_tilsyn, label = 'antall tilsyn')
plt.plot(aar, antall_med_tilsyn, label = 'antall med tilsyn')
  
# function to show the plot
plt.legend(loc='best')
plt.show()