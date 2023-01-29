import tkinter
from uib_inf100_graphics import *

def draw_stripes_from_left_edge(app, canvas, colors):
    # setter noen faste verdier som skal forbli slik som de er gjennom hele funksjonen
    y1 = 0
    y2 = app.height
    # bruker en indeksert løkke og løper gjennom colors-listen og henter indeks til elementene i lista
    for i,c in enumerate(colors):
        # endrer x-verdiene som er parametere i create-rectangel
        # slik at bredden på hvert rektangel er 10
        x1 = i*10
        x2 = 10 + i*10
        # lager rektangelene
        canvas.create_rectangle(x1,y1,x2,y2,fill=colors[i],outline=colors[i])

def draw_stripes_from_point(canvas, x, y, width, height, colors):
    # setter noen faste verdier som ikke kommer til å endre seg
    y2 = y + height
    y1 = y
    # løkke som løper gjennom colors listen og finner index
    for i in range(len(colors)):
        # endrer x-verdiene for hvert rektangel av en farge i listen
        # slik at bredden blir lik for hver gang
        x2 = x + width + (i*width)
        x1 = x + i * width
        # tegner rektanglene
        canvas.create_rectangle(x1,y1,x2,y2, outline=colors[i], fill=colors[i])
        


def draw_vertical_stripes_between(canvas, x1, y1, x2, y2, colors):
    # finner hva høyden og bredden er for hvert rektangel
    hoyde = max(y1,y2) - min(y1,y2)
    bredde = (x2-x1)/len(colors)
    y2 = y1 + hoyde
    # bruker løkke for å løpe gjennom listen med farger og henter index
    for i in range(len(colors)):
        # endrer tilsvarende x- og y-verdier for hvert rektangel med farge
        # slik at de blir like for hver iterasjon
        x = x1 + i*bredde
        x2 = x1 + bredde + bredde * i
        # lager rektangelen
        canvas.create_rectangle(x,y1,x2,y2, outline=colors[i], fill=colors[i])

# def redraw_all(app, canvas):
#     draw_stripes_from_left_edge(app, canvas, ["green", "yellow", "#0cc"]*4)
#     draw_stripes_from_point(canvas, 50, 50, 50, 100, ["#f00", "#f50", "#f80"])
#     draw_vertical_stripes_between(canvas=canvas, x1=250, y1=10, x2=350, y2=80,
#     colors=["red", "#a00", "#500", "black",])
# run_app(width=400, height=200)

# def redraw_all(app, canvas):
#     draw_stripes_from_left_edge(app, canvas, ["blue","navy"]*5)
#     draw_stripes_from_point(canvas, 30, 90, 50, 100, ["#0f0", "#0fc", "#0ff", "#0cf"])
#     draw_vertical_stripes_between(canvas=canvas, x1=160, y1=10, x2=350, y2=80,colors=["black", "red", "yellow"])

#     margin = 2
#     width = 30 + margin
#     height = 20 + margin
#     x_left = 270
#     y_top = 100
#     for row in range(3):
#         for col in range(4):
#             draw_vertical_stripes_between(canvas=canvas,
#                 x1=(x_left + width*row),
#                 y1=(y_top + height*col),
#                 x2=(x_left + width*(row+1) - margin),
#                 y2=(y_top + height*(col+1) - margin),
#                 colors=["#0f0", "#0a0", "#050", "black",])
# run_app(width=400, height=200)