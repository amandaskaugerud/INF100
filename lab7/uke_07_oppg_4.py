def find_words_in_character_grid(char_grid,words):
    resultat = []
    # sjekker om ordene finnes i rad eller fra venstre til høyre
    for word in words:
        # en tom str variabel som skal ta inn radene gjort til strenger
        row_str = ""
        for row in char_grid:
            # gjør om radene til strenger
            row_str = "".join(row)
            # sjekker om et ord i ordlisten tilsvarer raden
            if word in row_str:
                resultat.append(word)
        # sjekker om ordene finnes i kolonnen
        for col in range(len(char_grid[0])):
            # tom variabel som skal være kolonnene gjort til strenger
            col_str = ""
            for row in range(len(char_grid)):
                # legger til hver bokstav i str variabelen
                col_str += char_grid[row][col]
            # sjekker om ord fra ordlisten tilsvarer til kolonnen
            if word in col_str:
                resultat.append(word)
    return sorted(resultat)
