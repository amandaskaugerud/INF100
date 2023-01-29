# kodesporing
# def f(x):
#     x+=1
#     return 2*x
# def g(x):
#     y = f(x)
#     y += f(x)
#     return f(y)
# print(g(f(1)))

# line = input()
# a, b = line.split()
# a = int(a)
# b = int(b)

# print(min(a,b))
# print(max(a,b))

# def is_palindrome(s):
#     for i in range(len(s)):
#         if s[-i] != s[-i-1]:
#             return False
#         else:
#             return True
# print(is_palindrome("ada"))

# def is_palindrome(s):
#     backwards = s[::-1]
#     return s == backwards
# print(is_palindrome("ada"))

# def number_of_occurrences(a,x):
#     count = 0
#     for i in a:
#         # number = float(number)
#         if i == x:
#             count += 1
#     return count

# def number_of_occurences_in_a_for_values_b(a,b):
#     c = []
#     for i in range(len(a)):
#         c.append(number_of_occurrences(a,b[i]))
#     return c


# def mode(a):
#     for i in a:
#         if number_of_occurrences(a,i) == max(number_of_occurences_in_a_for_values_b(a,a)):
#             return float(i)

# print(locals())

# import csv
# exampleFile = open('exampleWithHeader.csv')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# print(exampleData)

A = 12

print(f"{A:d}")
