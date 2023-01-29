from uib_inf100_graphics import *

def app_started(app):
    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    # slange kroppen
    app.snake_height = 50
    app.snake_width = 25
    # slangehodet
    app.snake_head_x = None
    app.snake_head_y = None
    app.snake_head_r = 10
    # start posisjonen
    app.snake_x0 = 25
    app.snake_y0 = app.height//2
    app.snake_x1 = app.snake_x0 + app.snake_width
    app.snake_y1 = app.snake_y0 + app.snake_height//2

def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
    canvas.create_line(app.snake_x0,app.snake_y0,app.snake_x0,app.snake_y1,width = 3,fill="green")

    canvas.create_line(app.snake_x0, app.snake_y1, app.snake_x1, app.snake_y1, width= 3, fill="green")

    canvas.create_line(app.snake_x1, app.snake_y1, app.snake_x1, app.snake_y1 - app.snake_height, width = 3, fill="green")

    canvas.create_line(app.snake_x1, app.snake_y1-app.snake_height, app.snake_x1 + app.snake_width, app.snake_y1-app.snake_height, fill="green", width = 3)

    canvas.create_line(app.snake_x1 + app.snake_width, app.snake_y1-app.snake_height,app.snake_x1, app.snake_y1-app.snake_height, fill="green", width = 3)

run_app(width=400, height=200, title="Snake Pattern")
