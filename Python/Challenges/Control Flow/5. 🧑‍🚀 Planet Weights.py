print("It is year 2199, we have become an interplanetary species and can travel to other planets in the solar system.\n")
earth_weight = float(input("Enter your Earth weight : "))
print("\n1. Mercury")
print("2. Venus")
print("3. Mars")
print("4. Jupiter")
print("5. Saturn")
print("6. Uranus")
print("7. Neptun\n")
planet_num = int(input("Choose a planet: "))


if planet_num == 1:
  destination_weight = 0.38 * earth_weight
  print("Your destination weight is " + str(destination_weight))
elif planet_num == 2:
  destination_weight = 0.91 * earth_weight
  print("\nYour destination weight is " + str(destination_weight))
elif planet_num == 3:
  destination_weight = 0.38 * earth_weight
  print("\nYour destination weight is " + str(destination_weight))
elif planet_num == 4:
  destination_weight = 2.53 * earth_weight
  print("\nYour destination weight is " + str(destination_weight))
elif planet_num == 5:
  destination_weight = 1.07 * earth_weight
  print("\nYour destination weight is " + str(destination_weight))
elif planet_num == 6:
  destination_weight = 0.89 * earth_weight
  print("\nYour destination weight is " + str(destination_weight))
elif planet_num == 7:
  destination_weight = 1.14 * earth_weight
  print("\nYour destination weight is " + str(destination_weight))
else:
  print("\nInvalid planet number")