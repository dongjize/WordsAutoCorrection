import Levenshtein

dictionary = open("data/dict.txt", "r")
misspell = open("data/wiki_misspell.txt", "r")
correct = open("data/wiki_correct.txt", "r")
# rectified = open("data/rectified_edit.txt", "w")

w = misspell.readlines()[0]
dist, d = min([(Levenshtein.distance(w.strip(), d.strip()), d) for d in dictionary])
print(dist, d)

# for d in dictionary:
#     Levenshtein.distance(w.strip(), d.strip())

# for w in misspell.readlines():
#     w = w.strip()
#     for d in dictionary:
#         d = d.strip()
#         Levenshtein.distance(w, d)

# Levenshtein.distance()
