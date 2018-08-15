import json
import sys
import re

def convert_to_genre_dict(gens, genres_dirty):
    genres =  genres_dirty.split("/")
    for i in range(0, len(genres)):
        genre = {}
        g = ""
        print("genre: " + genres[i])
        genre_tokens = genres[i].split(" ")
        if(len(genre_tokens) > 2):
            genre.__setitem__("modifier", genre_tokens[0])
            for j in range(1, len(genre_tokens)):
                g += genre_tokens[j] + " "
                print("g: " + g)
        else:
            g = str(genres[i])
        genre.__setitem__("genre", g.strip())
        print("genre in dict (k,v): " + str(genre))
        gens.append(genre)

if __name__ =="__main__":
    band_list = []
    parsed = {}

    with open(sys.argv[1], "r+", encoding="utf-8") as f:
        try:
            band_list = json.loads(f.read(), encoding="utf-8")
        except Exception as e:
            print("JSON Error!!: " + e)
        
        num_of_bands = len(band_list)
        #clean early/later
        #print("here1 " + str(num_of_bands))
        for i in range(0, num_of_bands):
            genres_dirty = band_list[i]["genres_unsanitized"]
            genres = []
            print(genres_dirty)
            if "(early)" not in genres_dirty:
                convert_to_genre_dict(genres, genres_dirty)
                print("gens" + str(genres))
