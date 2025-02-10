annagramsDict = {} 
wLenDict = {}

with open("words.txt") as file:
    words = file.readlines()

for word in words:
    word = word.strip()
    annagramsDict.update({word : []})

    wLength = len(word)

    if wLength not in wLenDict:
        wLenDict.update({wLength:[(''.join(sorted(word)),word)]})
    else:
        wLenDict[wLength].append((''.join(sorted(word)),word))

for word in annagramsDict:

    sortedWord = ''.join(sorted(word))
    wordLen = len(word)

    simLenWords = wLenDict[wordLen]

    for simWordTup in simLenWords:
        if simWordTup[0] == sortedWord and simWordTup[1] != word:
            annagramsDict[word].append(simWordTup[1]) 