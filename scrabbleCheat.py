
import twl as scrabble
import os
import time



def getLetters(letters=[]):
    for x in range(7):
        l = input(str(x+1) + ' ~ Enter a letter ->  ')
        letters.append(l)
    return letters

def checkVaild(word):
    x = scrabble.check(word)
    return x

def getPossibleWords(letters):
    return list(scrabble.anagram(letters))

def checkScore(word,score=0):
    LETTER_SCORES = {"a": 1, "b": 3, "c": 3, "d": 2,
                     "e": 1, "f": 4, "g": 2, "h": 4,
                     "i": 1, "j": 8, "k": 5, "l": 1,
                     "m": 3, "n": 1, "o": 1, "p": 3,
                     "q": 10, "r": 1, "s": 1, "t": 1,
                     "u": 1, "v": 4, "w": 4, "x": 8,
                     "y": 4, "z": 10}
    for x in word:
        n = int(LETTER_SCORES[x])
        score += n
    return int(score)



validWords = []
allScores = {}

try:
    
    print('\ninput your scrabble hand below:\n ')
    
    letters = getLetters()
    wordOptions = getPossibleWords(letters)
    
    for x in wordOptions:
        valid = checkVaild(x)
        if valid == True:
            validWords.append(x)
        else:
            pass
    
    for y in validWords:
        score = checkScore(y)
        allScores.update({y:score})
    max_word = max(allScores, key=allScores.get)
    resp = max_word + ' with ' + str(allScores[max_word]) + 'points'
    time.sleep(0.5)
    os.system(f'say {resp}')
    print(' ')
    print('____________________________________')
    print("BEST OPTION ->  " + str(max_word) + ' ~ ' + str(allScores[max_word]) + ' pts')
    print(' ')
    for i in allScores:
        print(i + ' ~ ' + str(allScores[i]) + ' pts')
    print(' ')
    print('TOTAL: ' + str(len(allScores)) + ' words')
    print(' ')

except:
    print(' ')
    print('____________________________________')
    print('your on your own this time...\n<error.no words found for given letters>')
    print(' ')


