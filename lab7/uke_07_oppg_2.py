# oppgave 2
# del A
def remove_row(grid,row):
    # fjerner row i grid på en desktruktiv måte
    grid.remove(grid[row])

# del B
import copy
def row_removed(grid,row):
    # lager en dyp kopi av listen slik at jeg kan mutere den
    grid_copy = copy.deepcopy(grid)
    # muterer listen slik at jeg får fjernet ønsket rad
    grid_copy = grid_copy[:row] + grid_copy[row+1:]
    return grid_copy

# del C
def remove_col(grid, col):
    # finner alle radene i rutenett 
    for rows in grid:
        # fjerner kolonnen i radene
        rows.remove(rows[col])

# del D
def col_removed(grid,col):
    # lager en dyp kopi som kan muteres
    grid_copy = copy.deepcopy(grid)
    # en tom liste som skal ta inn de nye radene
    resultat = []
    # løper gjennom alle radene
    for rows in grid_copy:
        # fjerner ønsket kolonner
        a = [rows[:col] + rows[col+1:]]
        resultat += a
    return resultat

