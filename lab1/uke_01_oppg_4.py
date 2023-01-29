#ber om diktet sine rader
print("Første raden:")
rad1 = input()
print("Andre raden:")
rad2 = input()
print("Tredje raden:")
rad3 = input()

#lagerer lengden av radene i variabler
lengde1= len(rad1)
lengde2= len(rad2)
lengde3= len(rad3)

#lager mellomrom
print(" ")

#skriver ut diktet
def dikt(rad1, rad2, rad3):
    maks = max(int(lengde1), int(lengde2), int(lengde3))
    print("@"*(maks+4))
    x = maks - lengde1
    print("@ "+(" "*x)+rad1+" @")
    x = maks - lengde2
    print("@ "+(" "*x)+rad2+" @")
    x = maks - lengde3
    print("@ "+(" "*x)+rad3+" @")
    print("@"*(maks+4))
dikt(rad1,rad2,rad3)

