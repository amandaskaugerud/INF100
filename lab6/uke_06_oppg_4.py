# oppgave 4
def smallest_absolute_difference(a):
    # sorterer listen på en ikke-destruktiv måte
    a = sorted(a)
    # lager en tom liste som tar inn alle differansene
    differanser = []
    # en tom iterasjons variabel for while-løkken
    i = 0
    # en while løkke som har indexene til verdiene i listen
    while i < len(a)-1:
        # finner differansen mellom verdiene
        differanse = abs(a[i]-a[i+1])
        # legger til differansen i differanse listen
        differanser = differanser + [differanse]
        i += 1
    # returnerer minste differanse fra listen
    return min(differanser)
