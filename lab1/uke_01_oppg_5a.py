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
width =  input("Angi en bredde: ")
height = input("Angi en høyde: ")
depth =  input("Angi en dybde: ")
#kaller på funksjonen med gitte verdier
print(volum_of_box(width,height,depth))
