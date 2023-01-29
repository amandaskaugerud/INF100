# oppgave 6
# definerer en funksjon som sjekker om tallet er positivt og partall
def is_even_positive_int(x):
    # sjekker typen til x, større enn null og partall
    if type(x) is int and x>0 and x%2==0:
        return True
    else:
        return False
