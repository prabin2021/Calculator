class Playlist:
    
    def __init__(self,playlist_name):
        self.playlist_name = playlist_name
        self.movie_list = []
        
    def add_movie(self, movie):
        self.movie_list.append(movie)
        print(f"{movie} is added")
    
    def remove_movie(self,movie):
        self.movie_list.remove(movie)
        print(f"{movie} is deleted")
        
    def show_movie(self):
        print("\nYour movie list:\n")
        count = 1
        for i in self.movie_list:
            print(count,"." ,i)
            count = count + 1
            
    
print("................Movie collection App....................")
        
playlist_name = input("Enter playlist name: ")
p1 = Playlist(playlist_name)

while True:
    
    print("\nYour available options:")
    print("1. Add Movie\n2. Remove Movie\n3. Show Playlist\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        movie = input("Enter movie name to add: ")
        p1.add_movie(movie)
        
    
    elif choice == "2":
        movie = input("Enter movie name to remove: ")
        p1.remove_movie(movie)
        
    elif choice == "3":
        p1.show_movie()
        
    elif choice == "4":
        print("Exiting the app")
        break
    
    else:
        print("Invalid Choice")
        