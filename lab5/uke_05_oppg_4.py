# oppgave 4
def read_and_sort():
    # tom liste som tar inn input
    tall = []
    # starter med en input
    siffer = int(input())
    # lagrer den i tall listen
    tall = tall + [siffer]
    # kjører en while-løkke som vil be om input til inputen er 0
    while (siffer != 0):
        # ber om input
        siffer = int(input())
        # legger den til i tall listen
        tall = tall + [siffer]
    # bruker den innebygde funksjonen til å sortere verdiene i tall liten
    tall.sort()
    # løper gjennom listen for å luke ut 0
    for i in range(len(tall)):
        if tall[i] != 0:
            # printer alle verdiene i listen som ikke er 0
            print(tall[i])
read_and_sort()


def f(x):
    x += x
    return 2*x
 
def g(x):
    y = f(x)
    y+= f(x)
    return f(y)

x = 1
x = f(x)
x = g(x)
print(x)