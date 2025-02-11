from collections import defaultdict



annagramsDict = defaultdict(list)
wLenDict = defaultdict(list)

with open("words.txt") as file:
    words = file.readlines()

for word in words:
    word = word.strip()
    annagramsDict.update({word : []})

    wLength = len(word)

    wLenDict[wLength].append((''.join(sorted(word)),word))

for word in words:

    sortedWord = ''.join(sorted(word))
    wordLen = len(word)

    simLenWords = wLenDict[wordLen]

    for word, sorted in simLenWords:
        if word == sortedWord and sorted != word:
            annagramsDict[word].append(sorted) 