class Pokemon:
  def __init__(self, entry, name, types, description, height, weight, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.height = height
    self.weight = weight
    self.is_caught = is_caught

  def speak(self):
    print(self.name + ', ' + self.name + '!')

  def display_details(self):
    print('Entry Number: ' + self.entry)
    print('Name: ' + str(self.name))

    if len(self.types) == 1:
      print('Type: ' + self.types[0])
    else:
      print('Type: ' + self.types[0] + '/' + self.types[1])
    
    print('Description: ' + self.description)
    print('Height: ' + self.height + 'm')
    print('Weight: ' + self.weight + 'kg')

    if self.is_caught:
      print(self.name + ' caught!')
    else:
      print(self.name + ' has not been caught.')
    
bulbasaur = Pokemon('#0001', 'Bulbasaur', ['Grass', 'Poison'], "For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.", 0.7, 6.9, True)
charmander = Pokemon('#0004', 'Charmander', ['Fire'], "If Charmander is healthy, the flame on the tip of its tail will burn vigorously and won't go out even if it gets a bit wet.", 0.6, 8.5, False)
squirtle = Pokemon('#0007', 'Squirtle', ['Water'], 'Its shell is soft immediately after it is born. In no time at all, the shell becomes so resilient that a prodding finger will bounce right off it.', 0.5, 9.0, True)
pikachu = Pokemon('#0025', 'Pikachu', ['Electric'], 'Possesses cheek sacs in which it stores electricity. This clever forest-dweller roasts tough berries with an electric shock before consuming them.', 0.4, 6.0, True)
psyduck = Pokemon('#0054', 'Psyduck', ['Water'], "Suffers perpetual headaches. If the agony grows too great, Psyduck’s latent power erupts, contrary to Psyduck’s intent. Ergo, I am exploring ways to ease the pain.", 0.8, 19.6, False)
ponyta = Pokemon('#0077', 'Ponyta', ['Fire'], "These Pokémon live in herds out in the grassland. Newborn foals lack their fiery manes, which will develop about an hour after birth.", 1.0, 30.0, True)

print(vars(bulbasaur))
bulbasaur.speak()
print('\n')
print(vars(charmander))
charmander.speak()
print('\n')
print(vars(squirtle))
squirtle.speak()
print('\n')
print(vars(pikachu))
pikachu.speak()
print('\n')
print(vars(psyduck))
psyduck.speak()
print('\n')
print(vars(ponyta))
ponyta.speak()