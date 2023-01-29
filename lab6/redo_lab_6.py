# from uib_inf100_graphics import *

# oppg 1
# def draw_stripes_from_left_edge(app, canvas, colors):
    # y1 = app.height
    # for i,c in enumerate(colors):
    #     x0 = 10*i
    #     x1 = 10 + (10*i)
    #     canvas.create_rectangle(x0,0,x1,y1,fill=c, outline=c)


# def draw_vertical_stripes_between(canvas, x1, y1, x2, y2, colors):
    # width = abs(x2-x1)/len(colors)
    # height = abs(y2-y1)
    # draw_stripes_from_point(canvas,x1,y1,width,height,colors)

# oppg 2
# def alternate_sign_sum(a:list) -> int:
    # the_sum = int()
    # for i in range(len(a)):
    #     if i%2==0:
    #         the_sum += a[i]
    #     else:
    #         the_sum -= a[i]
    # return the_sum



# oppg 3
# def median(a:list)->int or float:
    # a_sorted = sorted(a)
    # for i in range(len(a_sorted)):
    #     if len(a_sorted)%2 != 0:
    #         index = (len(a_sorted)-1)//2
    #         median = a_sorted[index]
    #     else:
    #         high_index = len(a_sorted)//2
    #         low_index = high_index -1
    #         median = (a_sorted[low_index]+a_sorted[high_index])/2
    # return median


# # oppg 4
# def smallest_absolute_difference(a: list) -> int or float:
    # # lager en sortert kopi av listen
    # a_sorted = sorted(a)
    # # setter en vilkårlig start grense
    # smallest_difference = abs(a[0] - a[1])
    # # løper gjennom med enumerate og løper gjennom alle elementene bortsett fra det siste slik at [index+1] henter siste element
    # for index, element in enumerate(a_sorted[:-1]):
    #     # sjekker differenansen
    #     if abs(element-a_sorted[index+1]) < smallest_difference:
    #         smallest_difference = abs(element-a_sorted[index+1])
    # return smallest_difference


# # oppg 5a
# def string_to_dict(s: str) -> dict:
    # s_dict = dict()
    # for letter in s:
    #     if letter not in s_dict:
    #         s_dict[letter] = 1
    #     else:
    #         s_dict[letter] += 1
    # return s_dict


# def can_be_made_of_letters(word:str, letters:str) -> bool:
    # word_dict = string_to_dict(word)
    # letters_dict = string_to_dict(letters)
    # for key in word_dict.keys():
    #     if key not in letters_dict.keys():
    #         return False
    #     else:
    #        if word_dict[key] > letters_dict[key]:
    #             return False
    # return True


# oppg 5b
# def possible_words(wordlist:list, letters: str) -> list:
    # possible_words_list = list()
    # for word in wordlist:
    #     if can_be_made_of_letters(word, letters):
    #         possible_words_list.append(word)
    # return possible_words_list


# oppg 5c
# def read_file(path):
    # with open(path, 'rt', encoding='utf-8') as f:
    #     return f.read()


# def possible_words_from_file(path, letters):
    # file_content = read_file(path)
    # possible_words_list = list()
    # for line in file_content.splitlines():
    #     if can_be_made_of_letters(line, letters):
    #         possible_words_list.append(line)
    # return possible_words_list


# oppg 6a
# def compress(raw_binary: str) -> str:
    # compressed = str()
    # count = 1
    # # sjekker om det første tallet er 1
    # if raw_binary[0] == "1":
    #     compressed += "0 "
    # # løper gjennom strengen
    # for i in range(len(raw_binary)-1):
    #     # sjekker om det neste elementet er lik det forrige
    #     if raw_binary[i+1] == raw_binary[i]:
    #         # plusser på 1
    #         count += 1
    #     else:
    #         # legger til counten i compressed
    #         compressed += str(count) + " "
    #         # re-stiller den til 1, ettersom sett 1 gang
    #         count = 1
    # # legger til den siste mengden av elementen
    # compressed += str(count)
    # return compressed


# oppg 6b
# def decompress(compressed_binary: str) -> str:
    # raw_binary = str()
    # compressed = 0
    # for value in compressed_binary.split(" "):
    #     decompressed = str(compressed) * int(value)
    #     raw_binary += decompressed
    #     compressed = int(not compressed)   
    # return raw_binary


# oppg 7
# import csv
# def read_csv_file(path, **kwargs):
    # with open(path, "rt", encoding='utf-8') as file:
    #     return list(csv.reader(file,delimiter=";", **kwargs))

# def passing_criteria(student: list) -> bool:
    # if student[13:17].count("B") < 4:
    #     return False
    # else:
    #     if student[1] == "B":
    #         if student[8:13].count("B") < 3:
    #             return False
    #     else:
    #         if student[2:13].count("B") < 6 or student[8:13].count("B") < 3:
    #             return False
    # return True 



# def students_who_passed(path)-> list:
    # students_passed = list()
    # file_content = read_csv_file(path)
    # for line in file_content[1:]:
    #     if passing_criteria(line):
    #         students_passed.append(line[0])
    # return students_passed