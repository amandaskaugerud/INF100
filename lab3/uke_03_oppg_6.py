# oppgave 6a
# funksjon som tar inn x som argument og returnerer verdien av funksjonen gitt x-verdien
def g(x):
    return 1/8*(x**2)-2*x+10

# oppgave 6b
# funksjon som regner integral av funksjonen gitt av to x-verdier
def approx_area_under_g(x_lo,x_hi):
    # tom variabel som skal fungerer som løpende sum variabel
    areal = 0
    # en for-løkke som teller variabel i, i rommet fra laveste x- og høyeste x-verdi 
    for x_i in range(x_lo,x_hi):
        # legger til verdien i sum variabelen
        areal += g(x_i)
    # returnerer areal variabelen
    return areal

# oppgave 6c
# en funksjon som finner tilnærmet areal under funksjonen
# den tar inn tre argumenter den høyeste og laveste x-verdien og antall stolper under funksjonen
def riemann_sum_g(x_lo, x_hi, n):
    # finner ut hva bredden av hver stolpe skal være
    bredde = float((x_hi-x_lo)/n)
    total = 0
    # en for-løkke som teller i innenfor antall stolper under funksjonen
    for i in range(0,n):
        # finner ut hva x verdien til i stolpen under funksjonen
        x_i = x_lo + (bredde*i)
        # legger så til arealet av stolpen under funksjonen til total arealet
        total += bredde * g(x_i)
    return total


# oppgave 6d
# en ny funksjon som gjør akkurat det samme som 6c bortsett fra at den tar inn hvilken som helst funksjon 
# og regner arealet under funksjonen og at brukeren selv bestemmer antall trapper under funksjonen
def riemann_sum(f,x_lo,x_hi,n):
    # finner ut hva bredden på hver trapp må være
    bredde = float((x_hi-x_lo)/n)
    total = 0
    # en for-løkke som teller i innefor antall trapper
    for i in range(0,n):
        # finner ut hva x-verdien til i trapp under funksjonen
        x_i = x_lo + (bredde * i)
        # legger til arealet av trappen i total summen av arealet under funksjon
        total += bredde * f(x_i)
    return total

