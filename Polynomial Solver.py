import math

a = int(input("enter a"))
b = int(input("Enter b"))
sqrB = b**2
c = int(input("enter c"))


quadraticRight = math.sqrt(sqrB + 4 * a * c)


x = str((-b + quadraticRight) / (2 * a))
x2 = str((-b - quadraticRight) / (2 * a))

answers = "The answers are " + x + " and " + x2
print(answers)