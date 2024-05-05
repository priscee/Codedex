'''
Pythagorean Theorem
'''

a = int(input("Enter a number for side a: "))
b = int(input("Enter a number for side b: "))

c = ((a ** 2) + (b ** 2)) ** 0.5

print(c)

'''
Quadratic Formula
'''

h = int(input("Enter a number for side h: "))
i = int(input("Enter a number for side i: "))
j = int(input("Enter a number for side j: ")) 

x1 = (-(i)+(((i ** 2) - (4*h*j)) ** 0.5)) / (2 * h)
x2 = (-(i)-(((i ** 2) - (4*h*j)) ** 0.5)) / (2 * h)

print(x1), print(x2)