def read_file(path):
    with open(path, "rt", encoding='utf-8') as f:
        return f.read()

def first_letter_last_word(path):
    letters = ""
    file_content = read_file(path)
    for line in file_content.splitlines():
        listed_line = list(line.split(" "))
        letters += listed_line[-1][0]
    return letters
