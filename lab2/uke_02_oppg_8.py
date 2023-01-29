
#  oppgave 8a
#  lager en funksjon point_in_rectangle som tar inn 6 argumenter (tre punkter)
def point_in_rectangle(x0,y0,x1,y1,x2,y2):
    # finner ut hvilke verdier som tilsvarer til hvilken side
    venstre = min(x0,x1)
    høyre = max(x0,x1)
    bunn = min(y0,y1)
    topp = max(y0,y1)
    # sjekker at det siste punktet er innenfor både venstre og høyre samt bunn og topp
    if høyre>=x2>=venstre and bunn<=y2<=topp:
        return True
    else:
        return False

# oppgave 8b
def rectangles_overlap(x0,y0,x1,y1,x2,y2,x3,y3):
    # finner verdiene for rektangel 1
    rec1_venstre = min(x0,x1)
    rec1_høyre = max(x0,x1)
    rec1_bunn = min(y0,y1)
    rec1_topp = max(y0,y1)
    # finner verdiene for rektangel 2
    rec2_venstre = min(x2,x3)
    rec2_høyre = max(x2,x3)
    rec2_bunn = min(y2,y3)
    rec2_topp = max(y2,y3)

    if rec1_høyre <= rec2_venstre and rec2_høyre<=rec1_venstre:
        return True
    elif rec1_topp >= rec2_bunn and rec2_topp >= rec1_bunn:
        return True
    else: 
        return False

# oppgave 8c
# henter funksjon distance fra uke_01_oppg_5 fra lab 1
# for å brukes i oppga 8c
def distance(x1,y1,x2,y2):
    avstand = ((abs(x1-x2)**2)+(abs(y1-y2)**2))**0.5 #regner ut etter formelen
    avstand_round = round(float(avstand),11) #runder av til 11 desimaler
    return avstand_round #printer til terminalen
# hovedfunksjonen i 8c
def circle_overlaps_rectangle(x0,y0,x1,y1,x2,y2,r2):
    venstre = min(x0,x1)
    høyre = max(x0,x1)
    bunn = min(y0,y1)
    topp = max(y0,y1)

    if point_in_rectangle(x0,y0,x1,y1,x2,y2):
        return True
    elif point_in_rectangle(x0,y0+r2,x1-r2,y1,x2,y2):
        return True
    elif venstre<=x2<=høyre:
        if y2 >= bunn-r2 and y2 <= topp+r2:
            return True
        else:
            return False
    elif bunn<=y2<=topp:
        if x2<= venstre-3 and x2 >= høyre+3:
            return True
        else: 
            return False
    elif distance(x0,y0,x2,y2)<=r2:
        return True
    elif distance(x1,y1,x2,y2)<=r2:
        return True
    elif distance(x0,y1,x2,y2)<=r2:
        return True
    elif distance(x1,y0,x2,y2)<=r2:
        return True
    else:
        return False

