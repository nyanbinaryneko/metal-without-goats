from genre import Genre

class Band:
    bandname = ""
    location = ""
    genres_unsanitized = ""
    active = ""
    genres_cleaned = []
    genres = []

    def __init__(self, band):
       bandname = band["bandname"]
       location = band["location"]
       genres_unsanitized = band["genres_unsanitized"]
       active = band["active"]

    def add_to_genres(self, genre_string):
        print("here in add to genres")