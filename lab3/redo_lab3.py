# # oppg 1
# def multiples_of_seven_up_to(n: int):
#     for i in range(7,n,7):
#         print(i)

# # oppg 2
# def multiplication_table(n: int):
#     for i in range(1,n+1):
#         print(f"{i}:", end=" ")
#         for j in range(1,n+1):
#             print(i*j, end=" ")
#         print()

# # oppg 3
# def dummy_chatbot():
#     while True:
#         print("Hi! Do you want to talk to me?")
#         answer  = input()
#         if answer == "no":
#             print("All right, bye!")
#             break
#         else:
#             print("That's cool!")
# dummy_chatbot()

# # oppg 4a
# def cross_sum(n: int) -> int:
#     cross_sum_of_n = 0
#     while n>0:
#         cross_sum_of_n += n%10
#         n = n//10
#     return cross_sum_of_n

# # oppg 4b
# def nth_number_with_cross_sum_x(n: int, x: int) -> int:
#     count = 0
#     check = 0
#     while True:
#         count += 1
#         if cross_sum(count) == x:
#             check += 1
#             if check == n:
#                 return count

# # oppg 5
# def split_line(x_lo ,x_hi ,n):
#     length = float((x_hi-x_lo)/n)
#     for i in range(n):
#         print(x_lo, end=" ")
#         x_lo = x_lo + length
#         print(x_lo)

# # oppg 6a
# def g(x: int or float) -> float:
#     return 1/8*x**2-2*x+10

# def almost_equals(a, b):
#     return abs(a - b) < 0.0000001

# # oppg 6b
# def approx_area_under_g(x_lo: int, x_hi: int) -> float:
#     approx_area = 0
#     for x_i in range(x_lo,x_hi):
#         approx_area += g(x_i)
#     return approx_area

# # oppg 6c
# def riemann_sum_g(x_lo, x_hi, n) -> float:
#     approx_area = 0
#     length = float((x_hi-x_lo)/n)
#     for i in range(n):
#         x_i = x_lo + (length*i)
#         approx_area += length* g(x_i)
#     return approx_area

# # oppg 6d
# def riemann_sum(f,x_lo,x_hi,n):
#     approx_area = 0
#     length = float((x_hi-x_lo)/n)
#     for i in range(n):
#         x_i = x_lo + (length*i)
#         approx_area += length* f(x_i)
#     return approx_area
