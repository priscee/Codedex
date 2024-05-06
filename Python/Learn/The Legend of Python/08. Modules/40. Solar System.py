from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)
r = 0

if random_planet == 'Mercury':
  r = 2440
elif random_planet == 'Venus':
  r = 6052
elif random_planet == 'Earth':
  r = 6371
elif random_planet == 'Mars':
  r = 3390
elif random_planet == 'Saturn':
  r = 58232
else:
  print("Opps! An error occurred")

area = round(4 * pi * r * r)

print(f"Area of {random_planet}: {area} sq m")