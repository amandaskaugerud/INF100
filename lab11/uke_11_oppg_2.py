# oppgave 2
def add_markers(filename):
    # en tom variabel som skal ta inn linjene med tekst
    tekst = ""
    # åpner og leser filen
    with open(filename, "rt", encoding='utf-8') as f:
        file_read = f.read()
    # går gjennom linje for linje av tekstfilen
    for line in file_read.splitlines():
        # sjekker at linjen ikke er tom
        if line != "":
            # legger til >>> og <<< og linjeskift til linjen
            line = ">>>" + line + "<<<" + "\n"
            # legger til linjen i tekst variabelen
            tekst += line
    return tekst
