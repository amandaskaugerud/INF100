# funksjon som deler opp i linje med lik differanse
def split_line(x_lo,x_hi,n):
    # finner lengde differansen
    lengde = float((x_hi-x_lo)/n)
    # en for-løkke som teller antall splittede linjestykker i antall linjestykker
    for i in range(n):
        # skriver først det aller første x-koordinatet 
        print(x_lo, end=" ")
        # legger til lengden 
        x_lo += lengde
        print(x_lo,"")