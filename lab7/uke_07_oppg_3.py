def all_rows_and_cols_equal_sum(grid):
    # samler radene
    row_lst = []
    # løper gjennom radene i rutenettet
    for row in range(len(grid)):
        # legger samme verdiene av alle elementene i raden
        row_lst.append(sum(grid[row]))
    # samler kolonnene
    # tom liste som skal lagre summen av kolonnene
    col_lst = []
    # tar utgangspunkt i kolonne verdien
    for col in range(len(grid[0])):
        # (en variabel som lagrer summen av ulike kolonner)
        sum_col = 0
        # og finner den kolonne verdien i rad
        for row in range(len(grid)):
            # regner ut summen av kolonnen
            sum_col += grid[row][col]
        # legger til summen i listen
        col_lst.append(sum_col)
    # Ragnhild Klette og jeg tenkte ut denne måten å sjekke listen på
    # sjekker om hele listen er lik
    # for hvis den største og minste verdien er lik så er hele listen lik
    # hvis ikke så er det hvertfall et tilfelle der verdiene ikke er like
    if max(col_lst) == min(col_lst) and max(row_lst) == min(row_lst):
        return True
    else:
        return False
