#oppgave 5a
#definerer en funksjon som regner volum
def volum_of_box(w,h,d):
    #gjør om verdiene til int
    width = int(w)
    height = int(h)
    depth = int(d)
    #multipliserer verdiene til variablene sammen
    volum = width*height*depth
    return volum

#bruker skriver inn verdier for høyde, bredde og dybde
#width =  input("Angi en bredde: ")
#height = input("Angi en høyde: ")
#depth =  input("Angi en dybde: ")
#kaller på funksjonen med gitte verdier
#print(volum_of_box(width,height,depth))
print(volum_of_box(2,3,5))

#oppgave 5b
from math import sqrt
#definerer en funksjon distance som tar inn fire parameter
def distance(x1,y1,x2,y2):
    avstand = sqrt(abs(x1-x2)**2+abs(y1-y2)**2) #regner ut etter formelen
    avstand_round = round(float(avstand),11) #runder av til 11 desimaler
    return avstand_round #printer til terminalen

#ber om brukeren sine tall på koordinater og gjør de til float slik at round funk, fungerer
#x1 = float(input("Koordinat x1: "))
#y1 = float(input("Koordinat y1: "))
#x2 = float(input("Koordinat x2: "))
#y2 = float(input("Koordinat y2: "))
#kaller på funksjonen med koordinater gitt av bruker
#print(distance(x1,y1,x2,y2))
print(distance(0,0,1,1))

#oppgave 5c
#definerer en funksjon circles_overlap som tar inn 6 variabler
def circles_overlap(x1,y1,r1,x2,y2,r2):
    #bruker samme fremgangsmetode som fra oppgave 5b
    avstand = distance(x1,y1,x2,y2) #regner ut etter formelen
    sum_radius= r1+r2
    #bruker if-setning til å sjekke avstanden mot radiusene
    if avstand <= sum_radius:
        return True #hvis mindre eller lik er svart true
    else:
        return False #hvis større er svaret nei
#input felt for brukeren til å skrive inne koordinater og radius
#x1 = int(input("Koordinat x1: "))
#y1 = int(input("Koordinat y1: "))
#r1 = int(input("Radius sirkel: "))
#x2 = int(input("Koordinat x2: "))
#y2 = int(input("Koordinat y2: "))
#r2 = int(input("Radius sirkel: "))
#kaller på funksjonen
#print(circles_overlap(x1,y1,r1,x2,y2,r2))
print(circles_overlap(0,0,3,5,0,2))