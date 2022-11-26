# pylint: disable=too-few-public-methods

"Singleton Use Case Example Code."

from game1 import Game1
from game2 import Game2
from game3 import Game3


# The Client
# All games share and manage the same leaderboard because it is a singleton.
GAME1 = Game1()
GAME1.add_winner(2, "Argentina", "13", "Player1, Player2, Player3, Player4, Player5, Player6, Player7, Player8, Player9")

GAME2 = Game2()
GAME2.add_winner(3, "Portugual", "15", "Player1, Player2, Player3, Player4, Player5, Player6, Player7, Player8, Player9")

GAME3 = Game3()
GAME3.add_winner(1, "Brasil   ", "19", "Player1, Player2, Player3, Player4, Player5, Player6, Player7, Player8, Player9")

GAME4 = Game3()
GAME4.add_winner(4, "Alemanha ", "12", "Player1, Player2, Player3, Player4, Player5, Player6, Player7, Player8, Player9")

GAME5 = Game3()
GAME5.add_winner(5, "Gana     ", "10", "Player1, Player2, Player3, Player4, Player5, Player6, Player7, Player8, Player9")

GAME1.leaderboard.print()
GAME2.leaderboard.print()
GAME3.leaderboard.print()
