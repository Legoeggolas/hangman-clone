"""
`selector` defines the functions used to create the list of words that
are presented to the user in the game.
"""

from csv import reader
from random import shuffle, randint
import sys
import os


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
    
    # Get a displayable string
    def getDashedWord(self):
        dword = self.dashedWord[:]
        for index in range(len(dword)):
            dword[index] += "   "
        
        return "".join(dword)
    
    # Place a character into the leftmost blank space
    def placeChar(self, char):
        index = self.dashedWord.index('_')

        if self.finishedWord[index] == char:
            self.dashedWord[index] = char
            return True
        
        return False

    def isFinished(self):
        return self.finishedWord == "".join(self.dashedWord)
        

# Auxiliary function to translate the CSV files into a usable list
def _parseWordList(diffmode: str) -> list:
    try:
        wd = sys._MEIPASS
    except AttributeError:
        wd = os.getcwd()
        
    if diffmode == "EASY":
        file_path = os.path.join(wd,"wordsrc","easy.csv")
    elif diffmode == "MEDIUM":
        file_path = os.path.join(wd,"wordsrc","medium.csv")
    else:
        file_path = os.path.join(wd,"wordsrc","hard.csv")
    
    wordList = []
    with open(file_path, 'r') as dat:
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