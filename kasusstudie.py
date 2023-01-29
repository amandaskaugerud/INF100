from uib_inf100_graphics import *
import random

def app_started(app):
    app.margin = 25
    app.population = 200
    app.radius = 0.01
    app.maxspeed = 0.01
    app.people = [generate_person() for _ in range(app.population)]
    app.people[0]["status"] = "sick"

def generate_person():
    return {
        "x": random.random(),
        "y": random.random(),
        "dy": random.random() - 0.5,
        "dx": random.random() - 0.5,
        "status":"healthy"
    }

def timer_fired(app):
    move_people(app)

def move_people(app):
    for person in app.people:
        person["x"] +=  person["dx"] * app.maxspeed
        person["y"] +=  person["dy"] * app.maxspeed

def infect_people(app):
    for person in app.people:
        if person["status"] == "sick":
            for peer in app.people:
                if within_striking_distance(person,peer):
                    peer["status"] = "sick"

def within_striking_distance(app, p1, p2):
    distance = (p1["x"]-p2["x"])**2 + (p1["y"]-p2["y"])**2

def redraw_all(app,canvas):
    draw_people(app,canvas,app.margin,app.margin,app.width-app.margin, app.height-app.margin)

def draw_people(app, canvas, x1,y1,x2,y2):
    canvas.create_rectangle(x1,y1,x2,y2)
    width = x2-x1
    heigth = y2-y1
    for person in app.people:
        cx = person["x"]
        cy = person["y"]
        x_left = (cx-app.margin) * width + x1
        x_rigth = x_left+2* app.radius * width
        y_top = (cy-app.margin)* heigth + y1
        y_bottom = y_top + 2 * app.radius * heigth
        get_color(person["status"])
        canvas.create_oval(x_left,y_top,x_rigth,y_bottom, fill="green", width=0)

def get_color(status):
    if status == "healthy":
        return "green"
    elif status == "sick":
        return "orange"
    elif status =="immune":
        return "magenta"

run_app(width = 500, heigth = 500)
