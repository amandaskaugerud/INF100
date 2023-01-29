# oppgave 6
def add_numbers():
    # løpende sum variabel
    summen = 0
    # while løkke som kjører helt til break
    while True:
        # ber om input fra bruker
        heltall = input("Give me an integer (q to quit):\n")
        # try, except som sjekker at input er et heltall
        try:
            # sjekker at input ikke er q som avslutter alt
            if heltall == "q":
                # skriver ut summen
                print(f"The sum is {summen}.")
                break
            # inter inputen
            heltall = int(heltall)
            # og legger til i sum
            summen += heltall
        # men hvis linje 16 kræsjer kjøres dette
        except ValueError:
            print("That was not an integer. Please try again.")
add_numbers()