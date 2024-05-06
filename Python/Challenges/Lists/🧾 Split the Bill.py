bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

total = 0
for item in bill:
  total += item

my_share = total / 4
my_share = round(my_share, 2)

print(f'${my_share}')