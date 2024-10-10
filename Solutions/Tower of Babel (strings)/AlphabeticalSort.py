"""
Given a list with words, sort them on alphabetical basis.
The given dictionairy can include words with capital letters, but they should not be prioritised.

Note: when using sort(), capital words get prioritised over lower letter words.
"""

dictionairy = ["This", "excercise", "is", "pretty", "interesting"]
longer = ['The', 'world', 'of', 'language', 'has', 'been', 'turned', 'to', 'chaos', 'nobody', 'can', 'understand', 'another', 'It', 'is', 'your', 'task', 'gather', 'words', 'from', 'this', 'explanation', 'In', 'a', 'list', 'there', 'should', 'be', 'no', 'double', 'and', 'punctuation', 'marks', 'Good', 'luck']


dictionairyIndex = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5,
                    'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
                    'k':11, 'l':12, 'm':13, 'n':14, 'o':15,
                    'p':16, 'q':17, 'r':18, 's':19, 't':20,
                    'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

def insert_correctly(lijst: list[str], word: str):
    exactWord = word
    word = word.lower()
    for i in range(0, len(lijst)):
        curWord = lijst[i].lower()
        scanning = True
        j = 0
        while scanning:
            if j >= len(word):
                lijst.insert(i, exactWord)
                return
            if j >= len(curWord):
                break
            dictIndex = dictionairyIndex.get(curWord[j])
            wordIndex = dictionairyIndex.get(word[j])
            #print(curWord, dictIndex)
            #print(word, wordIndex)
            if dictIndex > wordIndex:
                lijst.insert(i, exactWord)
                return
            if dictIndex == wordIndex:
                j += 1
            if dictIndex < wordIndex:
                scanning = False
    lijst.append(exactWord)
    return

def sorting(lijst: list[str]):
    newLijst = []
    for word in lijst:
        insert_correctly(newLijst, word)
        #print(newLijst)
    return newLijst