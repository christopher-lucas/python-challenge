import os
txtPath = os.path.join('Desktop','Declaration.txt')

import string

lines = 0
words = 0
characters = 0

for line in txtPath:
    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
    characters = characters + len(line)
print(lines)
print(words)
print(characters)