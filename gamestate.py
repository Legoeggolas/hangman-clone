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
    currWordIndex : int
        -- The index of the word to be, or being, presented.

    Methods
    -------
    readyState()
        -- Readies the state to be used to begin a game.
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
        self.wordList = list()
        self.healthPoints = 0
        self.currWordIndex = 0
    
    def readyState(self):
        """Makes the state ready for use in an actual game environment."""

        self.wordList = generateWordList(self.difficulty)
        
        self.healthPoints = (2*len(self.wordList))//(2**(["EASY", "MEDIUM", "HARD"].index(self.difficulty)))