numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]

#[expression for item in dataset if condition]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num %2 != 0]

print('Original Numbers: ', numbers)
print('Even Numbers: ', even_numbers)
print('Odd Numbers: ', odd_numbers)