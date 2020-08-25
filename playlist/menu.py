from playlist import Playlist

class Menu:

  def __init__(self):

    self.song_inven = Playlist()
    
    self.choices = {


      "1" : self.song_inven.show_all_songs,
 
      "2" : self.song_inven.create_song,
 
      "3" : self.song_inven.update_song,

      "4" : self.song_inven.delete_item,
 
      "Q" : print("Quit")

    }
  
  def display_menu(self):
      print(""" 
        **************************
          Welcome to Task Manager!
          How can we help you?  


          1. Show song

          2. Create song

          3. update song

          4. delete song

          Q. Quit program

          """)
    
  def run(self):
      
      while True:

        self.display_menu()

        choice = input("Please enter a choice:")

        if choice == 'Q':
          print("Thanks for using the playlist.")
          break

        action = self.choices[choice]

        if action:
          action()
        
        else:
          print("Please enter a valid choice")
