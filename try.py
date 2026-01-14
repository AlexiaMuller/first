import math


v = input("What ya need \n1 + \n2 - \n3 / \n4 * \n5 cos \n6 sin\n ")


if v in ('1', '+', '1+', '+1'):
    a = int(input("a: "))
    b = int(input("b: "))
    w = a + b

elif v in ('2', '-', '2-', '-2'):
    a = int(input("a: "))
    b = int(input("b: "))
    w = a - b

elif v in ('3', '/', '3/', '/3'):
    a = int(input("a: "))
    b = int(input("b: "))
    w = float(a / b)

elif v in ('4', '*', '4*', '*4'):
    a = int(input("a: "))
    b = int(input("b: "))
    w = a * b

elif v in ('5', 'cos', '5cos', 'cos5'):
    a = int(input("a: "))
    w = math.cos(a)

elif v in ('6', 'sin', '6sin', 'sin6'):
    a = int(input("a: "))
    w = math.sin(a)

else:
    print("Invalid input")
    w= "wrong choice"

print("Your number ", w)

# def foo(x, y):
#     return x + y
#
#
# def bar(x, y):
#     return x * y
#
#
# def baz(x, y):
#     return x / y if y != 0 else "oops"
#
#
# A = 1
# B = 2
# C = 3
#
#
# print("Sum:", foo(A, B))
# print("Product:", bar(A, B))
# print("Division:", baz(C, 0))
#
#
# for i in range(5):
#     print(i * i, end=" ")
#     print("done")
