def read_file(path):
    with open(path,"rt",encoding="utf-8") as f:
        return f.read()

def define_word(dict, line):
    dict[line[1]] = line[2]
    return dict

def calc_line(dict, liste):
    for element in liste[1::2]:
            if element in dict:
                print(f"{element} known")
            else:
                print(f"{' '.join(liste)} uknown")
                return

my_dict = dict()
for line in read_file("lab9\input.txt").splitlines():
    line_list = []
    for word in line.split(" "):
        line_list += [word]
    if line_list[0] == "def":
       my_dict = define_word(my_dict,line_list)
    elif line_list[0] == "calc":
        calc_line(my_dict,line_list)

# def foo 3
# calc foo + bar =
# def bar 7
# def programming 10
# calc foo + bar = // foo + bar = unknown
# def is 4
# def fun 8
# calc programming - is + fun = // programming - is + fun = unknown
# def fun 1
# calc programming - is + fun =
# clear

# foo + bar = unknown
# foo + bar = programming
# programming - is + fun = unknown
# programming - is + fun = bar

