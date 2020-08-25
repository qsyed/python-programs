class Song:
  def __init__(self, song_id, artist, song_name, length, genre):
    self.song_id = song_id
    self.artist = artist
    self.song_name = song_name
    self.length = length 
    self.genre = genre
    
  def __str__(self):
    return f"\n\n Id:{self.song_id} \n Artist: {self.artist} \nName: {self.song_name} \nLength: {self.length} \nGenre: {self.genre}"