import random
import pandas as pd

def test(onset, vowel, prevOnset, prevVowel):
    if onset != prevOnset and vowel != prevVowel:
        return True
    else:   
        return False

# fields = ['word', 'onset', 'vowel']
df = pd.read_csv('CantonWordList.csv')      # read word list

Allonset = list(set(df['onset'].tolist()))      # get all onsets
Allvowel = list(set(df['vowel'].tolist()))      # get all vowels

wordList = df['word'].tolist()                  # get list of every word
onsetvowelList = df['onset+vowel'].tolist()
total = len(wordList)

randList = []
randList2 = []
prevOnset = ""
prevVowel = ""

while len(randList) != total:
    tmp = random.choice(Allonset) + random.choice(Allvowel)     # randomly select onset+vowel
    if(tmp in onsetvowelList and test(tmp[0], tmp[1:], prevOnset, prevVowel)):  # check if onset+vowel is in list and does not match with previous onset+vowel
        tmpword = wordList[onsetvowelList.index(tmp)]
        randList.append(tmpword)
        randList2.append(tmp)
        onsetvowelList.remove(tmp)
        wordList.remove(tmpword)
        prevOnset = tmp[0]
        prevVowel = tmp[1:]
        
# export to csv
df = pd.DataFrame({'word': randList, 'onset+vowel': randList2})
df.to_csv('CantonWordList_rand.csv', index=False)