from math import sqrt

#definerer en funksjon circles_overlap som tar inn 6 variabler
def circles_overlap(x1,y1,r1,x2,y2,r2):
    #bruker samme fremgangsmetode som fra oppgave 5b
    avstand = int(sqrt(abs(x1-x2)**2+abs(y1-y2)**2)) #regner ut etter formelen
    radiuser = r1+r2
    #bruker if-setning til å sjekke avstanden mot radiusene
    if avstand <= radiuser:
        return True #hvis mindre eller lik er svart true
    else:
        return False #hvis større er svaret nei
#input felt for brukeren til å skrive inne koordinater og radius
x1 = int(input("Koordinat x1: "))
y1 = int(input("Koordinat y1: "))
r1 = int(input("Radius til sirkel 1: "))
x2 = int(input("Koordinat x2: "))
y2 = int(input("Koordinat y2: "))
r2 = int(input("radius sirkel 2: "))
#kaller på funksjonen
print(circles_overlap(x1,y1,r1,x2,y2,r2))