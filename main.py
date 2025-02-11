from collections import defaultdict

def findAnagrams(file_path):
    try:
        anagramsDict = defaultdict(list) 
        with open(file_path) as file: #Open the text file

            for line in file:
                word = line.strip().lower() #Strip lines removing newline characters, enforce lower to ensure matches can be made if the incorrect data is input
                if word.isalpha(): #Ignore digits as these are of incorrect type
                    sortedWord = "".join(sorted(word)) #Sort the word alphabetically then return to string using join method
                    anagramsDict[sortedWord].append(word) #Add sorted word as a key if possible, append the word to thr key-value list dicts
        
        return anagramsDict # Return the dictionary/hashtable object
    
    #Error handling for file not foound or lack of permission
    except FileNotFoundError as e:
        print(f"File not found {e}, check file/path")
        return None
    except PermissionError as e:
        print(f"File operation not permitted {e}, check file/path")
        return None
    

anagramDict = findAnagrams("words.txt") #Calling the function initialised and defined above with file path string as arg

if anagramDict:

    for anagrams in anagramDict.items():
        if len(anagrams[1]) > 1:
            print(",".join(anagrams[1]))