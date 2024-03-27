class Song:
    all=[]
    def __init__(self,name):
        self.name=name
        self.add_song_to_list(self)

    @classmethod
    def add_song_to_list(song,cls):
        cls.all.append(song)
    def show_song(cls):
        print([song for song in cls.name])
Oceans=Song("Oceans")
print(Song.show_song(Oceans))