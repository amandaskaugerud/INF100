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
#x1 = input("Skriv et siffer") 
#x2 = input("Skriv et siffer") 
#x3 = input("Skriv et siffer") 
#x4 = input("Skriv et siffer") 
#x5 = input("Skriv et siffer") 

x1 = 3
x2 = 4
x3 = 5
x4 = 6 
x5 = 1
#samler det i en liste
tall = [x1,x2,x3,x4,x5]
#kaller funksjonen
joker(3,4,5,6,1)