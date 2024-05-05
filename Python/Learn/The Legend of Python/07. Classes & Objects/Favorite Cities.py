class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

singapore = City('Singapore', 'Singapore', 6000000, ["Garden's by The Bay", "MBS", "Zoo"])

print(vars(singapore))