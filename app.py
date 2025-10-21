import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

## File One
'''for movie in data:
    print(movie["title"])'''
## File Two
'''yearafter = int(input("Type a year and i'll find all movies made AFTER that year."))
for movie in data:
    if movie["year"] > yearafter:
        print(movie["title"])'''
## File Three
yearafter = int(input("Type a year and i"))
## File Four

## File Five

## File Six


