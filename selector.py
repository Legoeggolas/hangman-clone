"""
`selector` defines the functions used to create the list of words that
are presented to the user in the game.
"""

from csv import reader
from random import shuffle, randint

class _Word:
    """Represents a single word"""

    def __init__(self, finword: str, clues: list, diff: str):
        """
        finword -- The word in it's complete state.
        clues -- A list of all the clues associated with this word.
        diff -- The difficulty of the word.
        """

        self.finishedWord = finword
        
        self.dashedWord = list(finword)
        difInt = ["EASY", "MEDIUM", "HARD"].index(diff)
        for _ in range(len(finword) - (len(finword)+difInt)//(2+difInt)):
            self.dashedWord[randint(0, len(self.dashedWord)-1)] = "_"
        
        self.clueList = clues
    
    def getDashedWord(self):
        dword = self.dashedWord[:]
        for index in range(len(dword)):
            dword[index] += "   "
        
        return "".join(dword)
    
    def placeChar(self, char):
        index = self.dashedWord.index('_')

        if self.finishedWord[index] == char:
            self.dashedWord[index] = char
            return True
        
        return False

    def isFinished(self):
        return self.finishedWord == "".join(self.dashedWord)
        

    
def _parseWordList(diffmode: str) -> list:
    if diffmode == "EASY":
        fname = r"easy.csv"
    elif diffmode == "MEDIUM":
        fname = r"medium.csv"
    else:
        fname = r"hard.csv"
    
    wordList = []
    with open(fname, 'r') as dat:
        filereader = reader(dat)
        fields = next(filereader)
        for row in filereader:
            wordList.append(_Word(row[0], row[1:], diffmode))
    
    return wordList



def generateWordList(diffmode: str) -> list:
    """
    Generates the word list required by the GameState

    Parameters
    ----------
    diffmode 
        -- An uppercase string that represents the difficulty of the game.
    """
    
    wordList = []
    if diffmode == "EASY":
        wordList.extend(_parseWordList("EASY"))
    elif diffmode == "MEDIUM":
        wordList.extend(_parseWordList("EASY"))
        wordList.extend(_parseWordList("MEDIUM"))
    else:
        wordList.extend(_parseWordList("MEDIUM"))
        wordList.extend(_parseWordList("HARD"))

    shuffle(wordList)

    return wordList