from uib_inf100_graphics import *

def app_started(app):
    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    app.r = 128
    app.g = 128
    app.b = 128
    app.color = str()
    app.message = str()
    app.state = False

def key_pressed(app, event):
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    app.state = True
    if event.key == "Up":
        if 0 < app.r <= 255:
            if 0 < app.r < 10:
                app.r -= 1
            else:
                app.r -= 10
    elif event.key == "Down":
        if 0 <= app.r < 255:
            if 240 < app.r < 255:
                app.r += 1
            else:
                app.r += 10
    elif event.key == "a":
        if 0 <= app.b < 255:
            if 240 < app.b < 255:
                app.b += 1
            else:
                app.b += 10
    elif event.key == "z":
        if 0 < app.b <= 255:
            if 0 < app.b < 10:
                app.b -= 1
            else:
                app.b -= 10
    elif event.key == "Right":
        if 0 < app.g < 255:
            if 240 < app.g < 255:
                app.g += 1
            else:
                app.g += 10
    elif event.key == "Left":
        if 0 < app.g <= 255:
            if 0 < app.g < 10:
                app.g -= 1
            else:
                app.g -= 10
    app.color = rgb_hexstring(app.r, app.g, app.b)
    app.message = f"Trykket '{event.key}', fargen er r={app.r} g={app.g} b={app.b}"

def rgb_hexstring(r, g, b):
    """ Given the integer RGB values (0-255) for a color, return its 
    hexadecimal RGB string repersentation."""
    return f"#{r:02x}{g:02x}{b:02x}"

def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.
    if app.state:
        canvas.create_text(10,50,text=app.message, anchor='nw', fill="black",font="Times 11")
        canvas.create_oval(160,80,240,160,fill=app.color, outline=app.color)
    else:
        canvas.create_text(10, 50, text=f'Trykk på piltastene og a,z for å endre farge r={app.r} b={app.g} g={app.b}', anchor='nw',fill='black', font='Times 11')
        canvas.create_oval(160,80,240,160,fill='#808080', outline="#808080")

run_app(width=400, height=200, title="Farge sirkel")
