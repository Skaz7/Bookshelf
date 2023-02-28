file = "./genres.txt"
with open(file, "r") as f:
    genres_list = f.read().splitlines()

for num, genre in enumerate(genres_list, start=1):
    print(num, genre)
