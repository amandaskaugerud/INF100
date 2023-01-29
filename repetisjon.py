
### 1. Find and correct the mistakes

# The following code tries to find the area of your living room
# width = int(input("What is the width of your living room in meters? ")) # gjør om fra str til int
# length = int(input("What is the length of your living room in meters? ")) # gjør om fra str til int

# area = width * length #fjerne det dobble gangetegnet
# print(f"Your living room is {area} m^2.") # gjør om til en f-string


# #### 2. Write a program that asks for the user's first name, then their last name.
# #### The program should then put the two names together and greet the user by their full name.

# # Your code goes here
# first_name = input("Hva er fornavnet ditt? ")
# last_name = input("hva er etternavnet ditt? ")

# print(f"Ditt fulle navn er {first_name} {last_name}")

# Write a function that returns the mean of three numbers
# def mean_of_three(a,b,c):
#     return (a+b+c)/3
# tall1 = int(input("Skriv et tall "))
# tall2 = int(input("Skriv et tall "))
# tall3 = int(input("Skriv et tall "))

# print(mean_of_three(tall1,tall2,tall3))

# # Write a function that finds the difference between two whole numbers
# def find_difference(a,b):
#     return a-b
# tall1 = int(input("Skriv et tall "))
# tall2 = int(input("Skriv et tall "))
# print(find_difference(tall1,tall2))

# def valid_choice(input):
#     if input == "Rock" or "Paper" or "Scissors":
#         return True
#     else:
#         return False
# svar = input()
# print(valid_choice(svar))

# What does the following line of code print, and in what order?

# def print_one():
#     print(1)
#     return 0

# print(print("3") or print_one() and print("2")) #først printer den 3 deretter kaller den på funksjonen print_one()
# # deretter printer den hele printen som alle de andre "små" printene ligger i

# def string_int_count(s):
#     for i in range(len(s)+1):
#         print(i)
# ord = input("Skriv et ord: ")
# string_int_count(ord)


# def divisible_by_n(a, n):
#     for i in range(0,a+1):
#         if i%n == 0:
#             print(i)
# number = int(input("Skriv et tall: "))
# antall = int(input("Skriv hva tallet skal være delelig på: "))
# divisible_by_n(number, antall)


# def multiples_of_3_or_5():
#     sum = 0
#     for i in range(1000):
#         if i%3 == 0 or i%5 == 0:
#             sum = sum + i
#     print(sum)
# multiples_of_3_or_5()

# def fizzbuzz(n):
#     for i in range(1,n+1):
#         if i%3 == 0 and i%5 == 0:
#             print("FizzBuzz")
#         elif i%5 == 0:
#             print("Buzz")
#         elif i%3 == 0:
#             print("Fizz")
#         else:
#             print(i)
# antall = int(input("Skriv et tall: "))
# fizzbuzz(antall)


# def char_count(s):
#     for i in range(len(s)+1):
#         print(i)
# string = input("Skriv et ord: ")
# char_count(string)

# def reverse_string(s):
#     print(s[::-1])
# string = input("Skriv et ord: ")
# reverse_string(string)

# def swap_chars(s):
#     print(s[-1]+s[1:-1]+s[0])
# string = input("Skriv et ord: ")
# swap_chars(string)

# def mix(s1, s2):
#     teller = 0
#     s2 = s2.split()
#     for i in range(len(s2)):
#         if s1 == s2[i]:
#             teller += 1
#     print(teller)
# string1 = input("Skriv et ord: ")
# string2 = input("Skriv en setning: ")
# mix(string1, string2)

# def lower_higher(lst, a):
#     lower = []
#     higher = []
#     for i in range(len(lst)):
#         if lst[i] < a:
#             lower.append(lst[i])
#         elif lst[i]>a:
#             higher.append(lst[i])
#     return f"liste med tall under {a}: {lower}\nliste med tall over {a}: {higher}"
# lst = [1,6,9,11,22,3,5,100,67,88,64,0,2,3,4]
# a = 20
# print(lower_higher(lst,a))




# def sort_list_tuples(lst):
#     """
#     Write a Python program to get a list,
#     sorted in increasing order by the last element in each tuple,
#     from a given list of non-empty tuples.
#     """
#     pass


# def duplicates(lst):
    # ny_lst = []
    # for i in range(len(lst)):
    #     if lst[i] in ny_lst:
    #         continue
    #     else:
    #         ny_lst.append(lst[i])
    # return ny_lst
# # lst = ["ekorn", "svale", "svane", "rev","ulv","ekorn"]
# # lst = [1,2,3,4,7,9,1,4,3]
# print(duplicates(lst))


# def slice_list(lst, n):
#     """
#     Create a function that takes a list, and returns a list of n sub-lists.
#     """
#     pass
