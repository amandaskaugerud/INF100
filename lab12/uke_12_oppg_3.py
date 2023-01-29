def spise_sammen():
    # et oppslagsverk som meny
    meny = {
        0: "Meny",
        1: "Stekt uer med blomkålpuré",
        2: "Piggvarfilet med ertepuré",
        3: "Boknatorsk med kremstuede",
        4: "Steinbit, sjøkreps og snøkrabbe",
        5: "Norske oster med marmelade"
    }
    # går gjennom oppslagsverket
    for key, value in meny.items():
        # for den første nøkkelen skriver bare ut verdien
        if key == 0: 
            print(value)
        # for de andre skrives både nøkkel og verdi ut
        else:
            print(f"{key}. {value}.")
    # ber brukeren velge
    valg = int(input("\nHvilket nummmer vil du bestille? "))
    # sjekker om valget er i blant nøkklene til oppslagsverket
    if int(valg) in meny.keys():
        # skriver ut valget
        print(f"{meny[int(valg)]} kommer straks!")
    else:
        # skriver en feilmelding
        print("Dette er ikke et gyldig valg!")
spise_sammen()
