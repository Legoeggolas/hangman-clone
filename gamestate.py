"""
`gamestate` stores the class used to represent the state of the game at any given time.
"""

from selector import generateWordList

class GameState:
    """
    Represents the instantaneous state of the game

    ...

    Attributes
    ----------
    difficulty : str
        -- An all capital string to represent the difficulty of the game.
    wordList : list
        -- An ordered list that represents the words to be presented to the player.
    healthPoints : int
        -- The number of tries the user has at the word being presented.
    wordIter : iterator
        -- Iterator to wordList. Facilitates the fetching of words.
    currWord : Word
        -- Holds the word as it is being represented in the game.

    Methods
    -------
    getNextWord()
        -- Updates the word being used in the game.
    """

    def __init__(self, diffmode: str):
        """
        Parameters
        ----------
        diffmode
            -- The difficulty selected by the user. Represented by "EASY"/"MEDIUM"/"HARD".
        
        Raises
        ------
        ValueError
            If the provided diffmode is invalid.
        """

        if diffmode.upper() not in ["EASY", "MEDIUM", "HARD"]:
            raise ValueError("Unrecognized difficulty")
        
        self.difficulty = diffmode.upper()
        self.wordList = generateWordList(self.difficulty)

        difInt = ["EASY", "MEDIUM", "HARD"].index(self.difficulty)
        self.healthPoints = (2*len(self.wordList))//(2**(difInt))
        print(f"GAMESTATE READY WITH: worldListLength={len(self.wordList)}, HP={self.healthPoints}")
        
        self.wordIter = iter(self.wordList)
        self.currWord = None
    
    def getNextWord(self):
        """Updates the word currently being used in the game to the next on the list."""

        try:
            nextWord = next(self.wordIter)
            print("Word fetched: " + nextWord.finishedWord)
        except StopIteration:
            print("Word list exhausted")
            nextWord = None
        
        self.currWord = nextWord  