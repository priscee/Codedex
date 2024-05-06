#City, latitude, longitude
my_city = ('Singapore', 1.352083, 103.819839)

friend1_city = ('London', 51.507351, -0.127758)
print(friend1_city)
friend2_city = ('Boston', 42.360081, -71.058884)
print(friend2_city)
friend3_city = ('Shanghai', 31.230391, 121.473701)
print(friend3_city)

everyone0 = my_city + friend1_city + friend2_city + friend3_city
print(everyone0)

everyone1 = (
  ('London', 51.507351, -0.127758), 
  ('Boston', 42.360081, -71.058884),
  ('Shanghai', 31.230391, 121.473701)
)
print(everyone1)