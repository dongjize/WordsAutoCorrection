import re

misspell = open("wiki_misspell.txt", "r")
correct = open("wiki_correct.txt", "r")
dictionary = open('dict.txt', 'r')
for w in misspell:
    for d in dictionary:
        pass

with open("wiki_misspell.txt", "r") as f:
    for word in f.readlines():
        pass
