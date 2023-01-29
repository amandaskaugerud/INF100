#oppgave 5a
def wavelength_to_color(nm):
    #sjekker wavelength mot de ulike verdiene for bølgelengdene
    if 380<=nm<=450:
        return "Violet"
    elif 450<=nm<=485:
        return "Blue"
    elif 485<=nm<=500:
        return "Cyan"
    elif 500<=nm<=565:
        return "Green"
    elif 565<=nm<=590:
        return "Yellow"
    elif 590<=nm<=625:
        return "Orange"
    elif 625<=nm<=750:
        return "Red"
    else:
        return None

#oppgave 5b
def frequency_to_color(THz):
    # regner om til hertz
    Hz = THz*(10**12)
    # regner om til bølgelengde 
    wavelength = (((3e8))/Hz)
    nm = wavelength * (10**9)
    return wavelength_to_color(nm)

#oppgave 5c
def frequency_or_wavelength_to_color():
    # ber om bruker input
    print("Enter a unit (nm or THz):")
    enhet = str(input())
    # sjekker hva verdien av inputen var
    if enhet=="nm":
        # ber om en bølgelengde verdi
        print("Enter a value in nm:")
        nm = int(input())
        print("")
        # sjekker at bølgelengden er innenfor spekteret
        if 380<=nm<=750:
            return print(wavelength_to_color(nm))
        else:
            print(f"There is no color with wavelength {nm} nm")
    # om enhet er THz gjøres det samme
    elif enhet == "THz":
        # ber om en THz verdi
        print("Enter a value in THz:")
        THz = int(input())
        print("")
        # sjekker at det er en gyldig verdi
        if 400<=THz<=790:
            # feilmelding for ingen THz frekvens som eksisterer
            return print(frequency_to_color(THz))
        else:
            print(f"There is no color with frequency {THz} THz") 
    else: 
        # om ingenting stemmer av input blir det en feilmelding
        print("")
        print(f"The unit must be either nm or THz, it can not be {enhet}")
frequency_or_wavelength_to_color()
