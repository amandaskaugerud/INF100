from math import sqrt

#definerer en funksjon distance som tar inn fire variabler
def distance(x1,y1,x2,y2):
    avstand = sqrt(abs(x1-x2)**2+abs(y1-y2)**2) #regner ut etter formelen
    avstand_round = round(float(avstand),11) #runder av til 11 desimaler
    return avstand_round #printer til terminalen
#ber om brukeren sine tall på koordinater og gjør de til float slik at round funk, fungerer
x1 = float(input("Koordinat x1: "))
y1 = float(input("Koordinat y1: "))
x2 = float(input("Koordinat x2: "))
y2 = float(input("Koordinat y2: "))
#kaller på funksjonen med koordinater gitt av bruker
print(distance(x1,y1,x2,y2))