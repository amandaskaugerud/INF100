# en funksjon som fungerer som en dum bot
def dummy_chatbot():
    while True:
        # skriver først en print til brukeren
        print("Hi! Do you want to talk to me?")
        answer = input("")
        # sjekker svaret til brukeren 
        if answer == "no":
            # svaret er nei, så da skriver den en beskjed og avslutter while-løkken
            print("All right, bye!")
            break
        else:
            # om svaret ikke er nei, så skriver den en hyggelig beskjed til brukeren
            print("That's cool!")
dummy_chatbot()

