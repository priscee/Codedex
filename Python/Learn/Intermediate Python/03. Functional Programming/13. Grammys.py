from functools import reduce

playlist = [
  ('What Was I Made For?', 3.42),
  ('Just Like That', 5.05), ('Song 3', 6.8),
  ('Leave The Door Open', 4.02),
  ('I Can\'t Breath', 4.47),
  ('Bad Guy', 3.14)
  ]

#filter()
def longer_than_five_minutes(x):
  return x[1] > 5.00

filter_playlist = filter(longer_than_five_minutes, playlist)

print(list(filter_playlist))
print('\n')

#map()
def minutes_to_seconds(x):
  duration = x[1]
  minutes = int(duration)
  seconds = (duration - minutes) * 100
  return minutes * 60 + seconds

map_playlist = list(map(minutes_to_seconds, playlist))

print(list(map_playlist))
print('\n')

#reduce()
def add_durations(x, y):
  duration = y[1]
  return x + duration

total_playtime = reduce(add_durations, playlist, 0)

print(total_playtime)