new_add=lambda n:n+12
print(new_add(2))
def my_func(x):
    return lambda n:n+x
my_century=my_func(100)
print(my_century(2000))
def my_age(birthYr):
    return lambda p:p-birthYr
my_age_now=my_age(2005)
print(my_age_now(2024))
class Album:

    GENRES = ["Hip-Hop", "Pop", "Jazz"]
    album_count = 0

    def __init__(self, genre, date):
        if self.check_genre(genre):
            self.increase_album_count()
            self.genre = genre
            self.release_date = date

    @classmethod
    def check_genre(cls, genre):
        return genre in cls.GENRES

    @classmethod
    def increase_album_count(cls, increment=1):
        cls.album_count += increment
Esther_album=Album("churchisha","02-03-24")
Benji_album=Album("reaching out","03-03-24")
#Album.album_count+=1
print(Album.album_count)