# a = "Hello"
# b = 1.3
# c = 7
# d = True

# print(type(a+"b"))
# print(type(b*c))
# print(type(f"{c}"))
# print(type([d]))
# print(type(len(a)))
# print(type(c*a))
# print(type(c==10.3))
# print(type(a+a))

# xs = {
#     "a":5,
#     "d": "hello",
#     "z": 3.1415,
#     5: 7
# }

# print(xs["a"]==5)
# print("hello" in xs.values())
# print(list(xs.keys()))
# print(xs[5] == 7)

# while True:
#     text = input("Text:")
#     if text == "":
#         print("Bye")
#         break
#     print(f"Your text had {len(text)} characters.")

# print(5 in range(0,10,3))
# print(False or True)
# print(15//2 > 7)
# print(not(not True))
# print(5 < 7 and 4 > 5)
# print(list(range(7))[-1] == 7)
# print(3 < 7 < 9)
# print([x**2 for x in range(3)] == [0,1,4])
# print(5 in range(6))

# filename = "foo.txt"
# with open(filename) as f:
#     for line in f:
#         line = line.strip()
#         line = line[::-1]
#         print(line)

# xs = [1,3,7,2,4,5]
# i = 0
# while i < len(xs):
#     x = xs[i]
#     if x > 5:
#         print(x)
#     i += 1

# text = "oppvaskmaskin"
# if "a" in text:
#     print("A")
# else:
#     print("B")
# if "k" in text:
#     print("C")
# if "m" in text:
#     print("D")

# xs = ["a","b","c","d"]
# print(xs[2]=="c")
# print("abc" == "".join(xs[0:3]))
# print(xs[::-1])
# print("d" > xs[-2])

# def all_same(input):
#     x = input[0]
#     for e in input[1:]:
#         print(e)
#         if x != e:
#             return False
#     return True
# print(all_same([1,2,3,1]))
# print(all_same([2,2,2,2,2]))

# def both_below_100(a,b):
#     return a<100 and b<100

# def min(input):
#     a = input[0]
#     for i in input[1:]:
#         if i < a:
#             a = i
#     return a

# oppg 13
# funksjon som lager ny fil
# def write_new_file(data, filename):
#     with open(filename, "w") as f: 
#         f.writelines(data)

# # funksjon som åpner en fil med en gitt sti
# def read_fil(path):
#     with open(path, "r") as f:
#         # returnerer filen som liste
#         return f.readlines()

# def change_name(list_of_names):
#     # looper gjennom listen med navn
#     for old_name in list_of_names:
#         # lagerer listet og lest fil
#         old_file = read_fil(old_name)
#         # henter ut sted og dato fra filen
#         place = old_file[0].strip()
#         date = old_file[1].strip()
#         # lagrer det nye navnet
#         new_name = date + "_" + place + ".txt"
#         # kaller på funksjonen som lager ny fil, med det nye filnavnet og samme data som fra gammel fil
#         write_new_file(old_file,new_name)

# old_names = ["qwghlm.txt","qwerty.txt"]
# change_name(old_names)
# import random
# choices = ["scissor", "rock", "paper"]
# oppg 14
# def rock_paper_scissor():
#     round = 1
#     you = 0
#     data_point = 0
#     data_choice = str()
#     while True:
#         print(f"Let's play round {round}")
#         while True:
#             player = input("Your choice (Rock/Paper/Scissors)? ").lower()
#             try:
#                 if player not in choices:
#                     raise Exception
#                 else:
#                     break
#             except:
#                 print(f"I don't understand {player}. Try again")
#         data_choice = choices[random.randint(0,2)]
#         print(f"My choice was {data_choice}.", end=" ")
#         if data_choice == player:
#             print("Tie")
#         elif player == "rock":
#             if data_choice == "scissor":
#                 print("You win")
#                 you += 1
#             else:
#                 print("I win")
#                 data_point += 1
#             print(f"Score: me {data_point} , you {you}")
#         elif player == "scissor":
#             if data_choice == "paper":
#                 print("You win")
#                 you += 1
#             else:
#                 print("I win")
#                 data_point += 1
#             print(f"Score: me {data_point} , you {you}")
#         elif player == "paper":
#             if data_choice == "rock":
#                 print("You win")
#                 you += 1
#             else:
#                 print("I win")
#                 data_point += 1
#             print(f"Score: me {data_point} , you {you}")
#         round += 1
#         cont = input("Continue (y/n)? ")
#         if cont == "n":
#             break
# rock_paper_scissor()

# oppg 15
# import math
# import matplotlib.pyplot as plt

# tidssekvens = [tall/100 for tall in range(0,505, 5)]
# angles = [30,45,60]
# start = 20
# g = 9.81
# def calc_x(tid, theta):
#     xs = list()
#     for t in tid:
#         xs.append(float(t * start * math.cos(theta)))
#     return xs

# def calc_y(tid, theta):
#     ys = list()
#     for t in tid:
#         ys.append(float(start * t * math.sin(theta) - (1/2 * g * t**2)))
#     return ys

# def make_trajectory(tid, angles):
#     for angle in angles:
#         rad = math.pi/180 * angle
#         xs = calc_x(tid, rad)
#         ys = calc_y(tid,rad)
#         bane_xs = []
#         bane_ys = []
#         for i in range(len(ys)):
#             if ys[i] > 0:
#                 bane_xs.append(xs[i])
#                 bane_ys.append(ys[i])
#         plt.plot(bane_xs,bane_ys, ".")

#     plt.legend(angles)
#     plt.title('Trajectories. v0 = 20 m/s')  # Tittel 
#     plt.xlabel('distance / m')              # x-aksetittel
#     plt.ylabel('height / m')                # y-aksetittel
#     plt.show()  
# make_trajectory(tidssekvens,angles)

        
