# oppgave 1
# innhold: les fra fil, håndtere strenger, skriv til fil
# leser filen
def read_file(path):
    with open(path, "rt", encoding='utf-8') as f:
        return f.read()

# hoved metode som leser fra fil, og lager en ny
def filter_high_temperatures(path_input, path_output, threshold_temp):
    # lagrer den leste filen
    file_content = read_file(path_input)
    # lager en ny fil med gitt navn/path
    file_created = open(f"lab12/{path_output}", "wt", encoding='utf-8')
    # løper gjennom den leste filen linje for linje
    for line in file_content.splitlines():
        # splitter linjen på dag og temperatur
        day, temp = line.split(" ")
        # sjekker om temperaturen er lik eller større enn oppgitt grense
        if float(temp) >= float(threshold_temp):
            # legger til i den nye filen
            file_created.write(f"{day} {temp}\n")
    # lukker filen når alt er sjekker
    file_created.close()
filter_high_temperatures("lab12/temperatures.txt", "high_temps.txt", 23.5)
filter_high_temperatures("lab12/temperatures.txt", "lab12/high_temps.txt", 23.5)
