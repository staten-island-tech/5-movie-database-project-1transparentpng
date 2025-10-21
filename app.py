import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

## File One
'''for movie in data:
    print(movie["title"])'''
## File Two
'''yearafter = int(input("Type a year and i'll find all movies made AFTER that year. >>"))
for movie in data:
    if movie["year"] > yearafter:
        print(movie["title"])'''
## File Three
'''yearafter = int(input("Type a year and i'll find all movies made AFTER that year. >> "))
yearbefore = int(input("Now, type a year AFTER the year you just gave and i'll find all movies made BEFORE that year. >> "))
for movie in data:
    if movie["year"] > yearafter and movie["year"] < yearbefore:
        print(movie["title"])'''
## File Four
yearduring = int(input("Type a year and i'll find all movies made DURING that year. >> "))
for movie in data:
    if movie["year"] == yearduring:
        print(movie["title"])
## File Five

## File Six
def filterGenre():
    listGenre = []
    genre = input("Please give me a Genre to filter movies by.")
    listGenre.append(genre)
    for movie in data  

