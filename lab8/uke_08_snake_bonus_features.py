import random
from uib_inf100_graphics import *

# hjelpefunksjon som angir fargene på brettet
def get_color(value):
    if value == 0:
        return "lightgray"
    elif value < 0:
        return "red"
    else:
        return "green"


# tegner et rute nett fra steg 1
# tok utgangspunkt fra oppg.1 i uke 7
def draw_board(canvas, x1,y1,x2,y2,board,debug_mode):
    rows = len(board)
    cols = len(board[0])
    cell_width = abs(x2-x1)/cols
    cell_height = abs(y2-y1)/rows
    for row in range(0,rows):
        for col in range(0,cols):
            color = get_color(board[row][col])
            cell_x1 = x1 + cell_width * col
            cell_y1 = y1 + cell_height * row
            cell_x2 = cell_x1 + cell_width
            cell_y2 = cell_y1 + cell_height
            # lager rutenettet
            canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2,fill=color, outline="black")
            # sjekker om debug mode er på
            if debug_mode == True:
                canvas.create_text((cell_x1+cell_x2)/2, (cell_y1+cell_y2)/2, text=f"{row},{col}\n{board[row][col]}", anchor='center')

def app_started(app):
    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    app.board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0,-1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    app.debug_mode = True
    app.head_pos = (3,4)
    size = input("How long do you want the snake to be? ")
    app.snake_size = int(size)
    direction = input("Choose a direction for the snake: ") 
    app.direction = direction.lower()
    app.state = "active"
    timer = input("How fast do you want the snake to move? Give answer in miliseconds: ")
    app.timer_delay = int(timer)

def get_next_head_position(head_row,head_col,direction):
    if direction == "north":
        head_row -= 1
    if direction == "south":
        head_row += 1
    if direction == "east":
        head_col += 1
    if direction == "west":
        head_col -= 1
    return (head_row, head_col)

def subtract_one_from_all_positives(grid):
    for col in range(len(grid[0])):
        for row in range(len(grid)):
            if grid[row][col] > 0:
                grid[row][col] -= 1

def add_apple_at_random_location(grid):
    possible_places = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                possible_places.append((row,col))
    possible_place = random.choice(possible_places)
    grid[possible_place[0]][possible_place[1]] = -1

def is_legal_move(row,col,board):
    if ((row in range(len(board))) and (col in range(len(board[0]))) and (board[row][col] <= 0)):
        return True
    else:
        return False

def move_snake(app):
    app.head_pos = get_next_head_position(app.head_pos[0], app.head_pos[1], app.direction)
    if is_legal_move(app.head_pos[0], app.head_pos[1],app.board) == True:
        if app.board[app.head_pos[0]][app.head_pos[1]] == -1:
            app.snake_size += 1
            add_apple_at_random_location(app.board)
        else:
            subtract_one_from_all_positives(app.board)
        app.board[app.head_pos[0]][app.head_pos[1]] = app.snake_size
        return app.head_pos
    else:
        app.state = "gameover"
        return 

def timer_fired(app):
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    if app.debug_mode == False and app.state == "active":
        move_snake(app) 

def key_pressed(app, event):
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    if app.state == "active":
        if event.key == "d":
            app.debug_mode = not app.debug_mode
        if event.key == "Space":
            move_snake(app)
        if event.key == "Up":
            app.direction = "north"
        if event.key == "Down":
            app.direction = "south"
        if event.key == "Left":
            app.direction = "west"
        if event.key == "Right":
            app.direction = "east"
    elif app.state == "gameover":
        if event.key == "d":
            app.debug_mode = not app.debug_mode
        if event.key == "r":
            app.state = "active"
            app_started(app)
      
def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.

    if app.state == "active":
        if app.debug_mode:
            canvas.create_text(app.width-(app.width/2), 10, text=f'app.head_pos={app.head_pos} app.snake_size={app.snake_size} app.direction={app.direction} status={app.state}',anchor='center')
        draw_board(canvas, 25, 25, app.width-25, app.height-25, app.board, app.debug_mode)
    elif app.state == "gameover": 
        if app.debug_mode:
            canvas.create_text(app.width-(app.width/2), 10, text=f'app.head_pos={app.head_pos} app.snake_size={app.snake_size} app.direction={app.direction} status={app.state}',anchor='center') 
        canvas.create_text(app.width/2,app.height/2,text="Game over", font ="Arial, 60",fill= "red")
        canvas.create_text(app.width/2,app.height - 20, text =" Press 'r' to play again.", fill="red")   
        
run_app(width=500, height=400, title="Snake")



