from song import Song

class Playlist:
  def __init__(self):
    self.all_songs = []
    self.latest_id = 0

  def create_song(self):
    artist = input("Enter the artist:")
    song_name = input("Enter the name of the song:")
    length = input("Enter the length of the song:")
    genre = input("Enter the genre of the song:")    
    new_item = Song(self.latest_id, artist, song_name, length, genre)
    self.all_songs.append(new_item)
    self.latest_id +=1 


  def delete_item(self):
    try:
      item_id = int(input("enter id of song to delete"))
      song = self.all_songs[item_id]
      self.all_songs.remove(song)
      
    except ValueError:
      print("only integer's are allowed")

  def show_all_songs(self):

    if len(self.all_songs) > 0:
      for song in self.all_songs:
        print(song)
    else:
      print("There is no song on the playlist...")
  
  def update_song(self):
    while True:
      name = input("Please enter the name of the song or (q) to exit: ")
      if name == 'q':
        return
        
      for song in self.all_songs:
        
        if name == song.song_name:
          while True:
            attribute = int(input("What do you like to update? (1) Name of the song. (2) Name of the artist. (3) The length. (4) Genre: " ))

            if attribute == 1:
              new_name = input("Please enter a new name for the song:")
              song.song_name = new_name

            elif attribute == 2:
              new_artist = input("Plase enter a new artist:")
              song.artist = new_artist
            elif attribute == 3:
              new_length = input("what is the length of the song")
              song.length = new_length
            elif attribute == 4:
              new_genre = input("what is the genre of the song: ")
              song.genre = new_genre
            else:
              print("enter valid option")
            
            while True:

              more_update = int(input("\n\n\nDo you want to update other information? (1) Yes. (2) No"))
            
              if more_update == 1:
                break
              
              elif more_update == 2:
                return
              
              else:
                print("Invalid option")
                continue
            
            

      print(f"{name} doesn't exist in our database. Please try again.")
