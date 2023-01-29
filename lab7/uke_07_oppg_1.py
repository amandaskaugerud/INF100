from venv import create
from uib_inf100_graphics import *
# oppgave 1 
# en funksjon som lager et rutenett basert på farger
def draw_grid(canvas, x1,y1,x2,y2,color_grid):
    # definerer cols og rows som verdiene som skal brukes for å lage rutenettene
    # radene tilsvarer lengden av hele den nøstede listen
    rows = len(color_grid)
    # kolonnene tilsvarer lengden av hele den første indre listen
    cols = len(color_grid[0])
    # finner bredden til hver celle som er hele breddena v rutenettet delt på antall kolonner
    cell_width = abs(x2-x1)/cols
    # finner høyden til hver celle som er hele høyde forskjellen på rutenettet delt på antall rader
    cell_height = abs(y2-y1)/rows
    # løper gjennom antall rader først
    for row in range(0,rows):
        # slik at man får laget riktig antall mengde med kolonner
        for col in range(0,cols):
            # x1 koordinatet til en celle er start verdien for hele rutenettet pluss bredden for antall kolonner
            cell_x1 = x1 + cell_width * col
            # y1 koordinatet til en celle er start verdien for hele rutenettet pluss høyden for antall rader
            cell_y1 = y1 + cell_height * row
            # x2 koordinatet til en cell er x1 verdien pluss bredden 
            cell_x2 = cell_x1 + cell_width
            # y2 koordninatet til en cell er y1 verdien pluss høyden
            cell_y2 = cell_y1 + cell_height
            # lager rektanglene 
            canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2,fill=color_grid[row][col])

def redraw_all(app, canvas):
    # Et 3x3 rutenett med innebygde farger
    draw_grid(canvas, 50, 20, 130, 100, [
        ["red", "green", "blue"],
        ["yellow", "pink", "cyan"],
        ["black", "gray", "orange"],
    ])

    # Et sjakkbrett
    draw_grid(canvas, 150, 20, 350, 100, [
        ["white", "black"] * 4,
        ["black", "white"] * 4,
    ] * 4)

    # En 2D-liste med kun én rad
    draw_grid(canvas, 50, 120, 350, 180, [
        ['#00c', '#01c', '#02c', '#03c', '#04c', '#05c', '#06c', '#07c',
         '#08c', '#09c', '#0ac', '#0bc', '#0cc', '#0dc', '#0ec', '#0fc']
    ])

run_app(width=400, height=200)