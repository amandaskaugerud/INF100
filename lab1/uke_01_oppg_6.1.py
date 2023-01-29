import random

#definerte funksjonen joker
def joker(x1,x2,x3,x4,x5):
    #en for-løkke som kjører gjennom listen tall
    for i in range(0,len(tall)):
        #sjekker om noen av siffrene i listen tall er mindre eller lik 4
        if tall[i] <= 4:
            print("opp")
        else:
            print("ned")

#velger tilfeldig hele tall fra 0-9
x1 = random.randint(0,9) 
x2 = random.randint(0,9) 
x3 = random.randint(0,9) 
x4 = random.randint(0,9) 
x5 = random.randint(0,9) 
#samler det i en liste
tall = [x1,x2,x3,x4,x5]
#kaller funksjonen
joker(x1,x2,x3,x4,x5)