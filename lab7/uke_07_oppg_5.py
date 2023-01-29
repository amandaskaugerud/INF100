# hjelpefunksjon som teller antall underscores i listen
def find_underscores(liste,shift):
    # variabler som skal telle antall dansetrinn
    count_dancemoves = 0
    # løper gjennom listen med hensyn på kolonnen
    for col in range(len(liste[0])):
        count_underscore = 0
        for row in range(len(liste)):
            # sjekker om et tegn er underscore
            if liste[row][col] == "_":
                # teller antall underscore
                count_underscore += 1
            # om hele kolonnen består av kun underscore
            if count_underscore == shift:
                # legger til 1 i antall dansetrinn
                count_dancemoves += 1
    return (count_dancemoves + 1)

first_line = input()
rows,cols = first_line.split()
rows = int(rows)
cols = int(cols)
bilde_liste = []
for i in range(rows):
    bilde = input()
    bilde_liste.append(bilde)
print(find_underscores(bilde_liste,rows))
        