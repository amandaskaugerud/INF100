def mase_for_is():
    print("Kan jeg få en is?")
    svar = input()
    while True:
        if svar == "ja":
            print("Tusen takk!")
            break
        else:
            print("Vær så snill, si ja!")
            svar = input()
mase_for_is()
