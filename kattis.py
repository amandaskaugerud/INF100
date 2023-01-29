# def count_vowels(s):
#     antall_vokal = 0
#     for bokstav in s:
#         if bokstav in "aeiouAEIOU":
#             antall_vokal = antall_vokal+ 1
#     return antall_vokal
# s = input("")
# print(count_vowels(s))

# x, y, n = list(map(int, input().split()))

# for i in range(1, n + 1):
#     if i % x == 0 and i % y == 0:
#         print("FizzBuzz")
#     elif i % x == 0:
#         print("Fizz")
#     elif i % y == 0:
#         print("Buzz")
#     else:
#         print(i)

# def digit_swap(tall):
#     tall = int(tall)
#     siffer = tall%10
#     tall = tall//10
#     print(siffer, end="")
#     print(tall)
# number = input()
# digit_swap(number)

# def oddities(n):
#     for i in range(n):
#         case = int(input())
#         if case % 2 == 0:
#             print(f"{case} is even")
#         else:
#             print(f"{case} is odd")
# antall = int(input())
# oddities(antall)

# s = input()

# if len(set(s)) == len(s):
#     print(1)
# else:
#     print(0)

# # lager to variabler med liste og l tar inn det som kommer før gitt splitt merke og r tar inn det etter
# l, r = input().split("()")
# # sjekker deretter at l og r er like lange/har lik verdi
# if l == r:
#     print("correct")
# else:
#     print("fix")

# a,b = input().split(" ")
# a = int(a)
# b = int(b)

# operasjon = 0
# while a!=b: 
#     if a%2==0 and a>=b:
#         operasjon += 1
#         a//=2
#     else:
#         operasjon += 1
#         a += 1
# print(operasjon)

# def license_to_launch():
#     antall_dager = input()
#     værmelding = input()
#     junk_forecast_string = værmelding.split()
#     junk_forecast = []
#     for tall in range(junk_forecast):
#         junk_forecast += [int(tall)]
#     min_value = min(junk_forecast)
#     for i in range(len(junk_forecast)):
#         if min_value == junk_forecast[i]:
#             return i
# print(license_to_launch())



# first_line = input()
# n,m = first_line.split(" ")
# n = int(n)
# m = int(m)
# tt = []
# for i in range(n):
#     line = input()
#     split_line = line.split(" ")
#     split_line_number = []
#     for str_item in split_line:
#         num_item = int(str_item)
#         split_line_number.append(num_item)
#     tt.append(split_line_number)

# print(tt)

# n = int(input())
# languages = [int(x) for x in input().split(" ")]
# min_akwardness = n
# for i in range(n):
#     for j in range(n):
#         if i != j:
#             if languages[i] == languages[j]:
#                 distance_i_j = abs(i-j)
#                 if distance_i_j < min_akwardness:
#                     min_akwardness = distance_i_j
# print(min_akwardness)



# n = int(input())
# def find_latest_occurence_of_before(last_saw_value, val):
#     return last_saw_value[val]

# last_saw_value = dict()
# languages = [int(x) for x in input().split(" ")]
# min_akwardness = n
# for i in range(n):
#    j = last_saw_value.get([languages[i]],-1)
#    if j>= 0:
#     distance_i_j = abs(i-j)
#     if distance_i_j < min_akwardness:
#         min_akwardness = distance_i_j
#     last_saw_value[languages[i]] = i
# print(min_akwardness)
