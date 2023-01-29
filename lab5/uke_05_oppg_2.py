from textwrap import fill
import tkinter
from venv import create
from uib_inf100_graphics import *

def redraw_all(app, canvas):
    # lager horisont 
    canvas.create_rectangle(0,0,400,200, fill="#87CEEB")
    canvas.create_rectangle(0,181,400,200, fill="green", outline="green")
    # lager hust
    canvas.create_rectangle(130,180,250,100, outline="black", fill="pink" )
    # lager taket
    canvas.create_polygon(130, 100, 190, 40, 250, 100, fill='brown', width = 2, outline='black')
    # lager vinduene
    canvas.create_oval(135, 105, 155, 135,fill='white', outline='black', width=1)
    canvas.create_oval(165, 105, 185, 135,fill='white', outline='black', width=1)
    canvas.create_oval(195, 105, 215, 135,fill='white', outline='black', width=1)
    canvas.create_oval(225, 105, 245, 135,fill='white', outline='black', width=1)
    # lager kryss i vinduene
    canvas.create_line(135,120,155,120, fill="black")
    canvas.create_line(145,105,145,136, fill="black")
    canvas.create_line(165,120,185,120, fill="black")
    canvas.create_line(175,105,175,136, fill="black")
    canvas.create_line(195,120,215,120, fill="black")
    canvas.create_line(205,105,205,136, fill="black")
    canvas.create_line(225,120,245,120, fill="black")
    canvas.create_line(235,105,235,136, fill="black")
    # lager døren
    canvas.create_rectangle(150,150,175,178, outline="black", fill="#b25001")
    canvas.create_line(162,150,162,178)
    canvas.create_oval(157,163,160,165,outline="#fac139", fill="#fac139")
    canvas.create_oval(164,163,167,165,outline="#fac139", fill="#fac139")
    # lager vindu ved siden av døren
    canvas.create_rectangle(195,150,245,160, outline="black", fill="white")
    canvas.create_rectangle(195,165,245,175, outline="black", fill="white")
    # lager kryss i vinduene
    canvas.create_line(195,155,245,155)
    canvas.create_line(220,150,220,160)
    canvas.create_line(195,170,245,170)
    canvas.create_line(220,165,220,175)
    # lager pipe på huset
    canvas.create_polygon(151,80,151,50,157,50,157,75, fill="black")
    # lager sol
    canvas.create_oval(20,20,50,50,fill="#FFD700")
run_app(width=400, height=200)