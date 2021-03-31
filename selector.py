"""
`selector` defines the functions used to create the list of words that
are presented to the user in the game.
"""

class _Word:
    # Represents a single word
    def __init__(self, finword, clues):
        self.finishedWord = finword
        self.clueList = clues

# Prototype function
def generateWordList(diffmode: str):
    """
    Generates the word list required by the GameState

    Parameters
    ----------
    diffmode : str
        An uppercase string that represents the difficulty of the game.
    """

    pass