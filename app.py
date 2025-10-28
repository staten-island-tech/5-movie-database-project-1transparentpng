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
'''yearduring = int(input("Type a year and i'll find all movies made DURING that year. >> "))
for movie in data:
    if movie["year"] == yearduring:
        print(movie["title"])'''
## File Five
def findMovie():
    search = input("What movie would you like to search for?")
    for movie in data:
        title = movie["title"]
        if search in title: 
## "in" searches for the string / variable in the other string / variable provided. this line finds if the search var (the user input, a string) is found in the title of the searched movie. If it is, it prints it
            print(movie["title"])
findMovie()
## File Six
'''def filterGenre():
    genre = input("Please give me a Genre to filter movies by.")
    if not genre:
        print("You did not input a genre!")
    for movie in data:
        if genre in movie["genres"]:
            print(movie["title"])'''
