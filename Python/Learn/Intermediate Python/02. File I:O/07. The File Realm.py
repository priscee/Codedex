liked_songs = {
  'Cruel Summer': 'Taylor Swift',
  'Bad Habits': 'Ed Sheeran',
  'Paradise': 'Coldplay',
  'Uptown Funk': 'Bruno Mars'
}

def write_liked_songs_to_file(songs, file):
  with open("liked_songs.txt", 'w') as file:
    file.write("Liked Songs:\n")
    for songs, artist in songs.items():
      file.write(f"{songs} by {artist}\n")

write_liked_songs_to_file(liked_songs, "liked_songs.txt")