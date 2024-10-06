print('Counting Letters...\n')
words = open("words.txt").read()
letterDict = {}
for letter in words:
    if letter in letterDict:
        letterDict[letter] = letterDict[letter] + 1
    else:
        letterDict[letter] = 1
print(letterDict)
