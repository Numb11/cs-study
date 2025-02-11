from collections import defaultdict

def findAnagrams(file_path):
        anagramsDict = defaultdict(list) 
        with open(file_path) as file: 

            for line in file:
                word = line.strip().lower() 
                if word.isalpha(): 
                    sortedWord = "".join(sorted(word)) 
                    anagramsDict[sortedWord].append(word) 
        
        return anagramsDict 
    

anagramDict = findAnagrams("words.txt") 

if anagramDict:

    for anagrams in anagramDict.items():
        if len(anagrams[1]) > 1:
            print(anagrams[1])

