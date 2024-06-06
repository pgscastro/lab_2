movies = {
    "Inception": {"year": 2010, "rating": 8.8, "genre": "Sci-Fi"},
    "The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
    "The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
    "Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
    "Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
}

for k, v in movies.items():
    print("The movie" + k + "was released in:", + v["year"], "with a rating of:", v["rating"], "and it's genre is:", v["genre"])

print(max(float(rating["rating"]) for rating in movies.values()))

movies["Matrix"] = {"year": 1999, "rating:": 8.7, "genre": "Sci-Fi"}
movies["Inception"]["rating"] = 9.0
del movies["Pulp Fiction"]
print(movies)