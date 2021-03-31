"""
`selector` defines the functions used to create the list of words that
are presented to the user in the game.
"""

import csv
from random import shuffle

class _Word:
    """Represents a single word"""

    def __init__(self, finword: str, clues: list):
        """
        findword -- The word in it's complete state.
        clues -- A list of all the clues associated with this word.
        """

        self.finishedWord = finword
        self.clueList = clues



def _parseWordList(diffmode: str) -> list:
    if diffmode == "EASY":
        fname = "easy.csv"
    elif diffmode == "MEDIUM":
        fname = "medium.csv"
    else:
        fname = "hard.csv"
    
    wordList = []
    with open(fname, 'r') as dat:
        writer = csv.writer(dat)
        fields = next(writer)

        for row in writer:
            wordList.append(_Word(row[0], row[1:]))
    
    return wordList

# Prototype function
def generateWordList(diffmode: str) -> list:
    """
    Generates the word list required by the GameState

    Parameters
    ----------
    diffmode 
        -- An uppercase string that represents the difficulty of the game.
    """

    wordList = _parseWordList(diffmode)
    shuffle(wordList)

    return wordList