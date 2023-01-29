from uib_inf100_graphics import *

def app_started(app):
    # oppretter variabler som skal brukes for å lage stigen
    # ber at bruker skriver antall steg i stigen
    app.step = int(input("Amount of ladder steps: "))
    # bredden på stigen//avstanden mellom de vertikale stigebeina
    app.ladder_width = 100
    # bestemmer x- og y-koordinatene til stigebeina 
    app.x1 = app.width//2 - 40
    app.y1 = 20
    app.x2 = app.x1 + app.ladder_width
    app.y2 = 380
    # bestemmer avstanden mellom hvert steg gitt av antall steg i stigen
    app.height = (abs(app.y1-app.y2)-20)//app.step

# funksjon som tegner stigesteg basert på steg nummeret
def draw_step_on_ladder(app, canvas, step_number):
    # y-koordinatet begynner på samme y som beina også legges til avstanden mellom stigestegene basert på stigesteget
    y_coor = app.y1 + (app.height*step_number) + app.height
    # tegner stigesteget
    canvas.create_line(app.x1, y_coor, app.x2, y_coor, width = 3, fill="red")

def redraw_all(app, canvas):
    # tegner først de to vertikale bena for stigen
    canvas.create_line(app.x1, app.y1, app.x1, app.y2, width = 5, fill="red")
    canvas.create_line(app.x2, app.y1, app.x2, app.y2, width = 5, fill = "red")
    # også tegnes alle stige stegene ved hjelp av hjelppfunksjon draw_step_on_ladder som blir kalt på x antall stigesteg
    for i in range(0,app.step+1):
        draw_step_on_ladder(app,canvas,i)

run_app(width=300, height=400, title="Ladder")
