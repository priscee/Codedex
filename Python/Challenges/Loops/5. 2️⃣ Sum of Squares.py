number = int(input("Enter an integer: "))

total = 0

for i in range(number, 0, -1):
  total += i ** 2

print(total)