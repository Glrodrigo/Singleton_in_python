"A Leaderboard Singleton Class"


class Leaderboard():
    "The Leaderboard as a Singleton"
    _table = {}

    def __new__(cls):
        return cls

    @classmethod
    def print(cls):
        "A class level method"
        print("--- Position --- ------- Country ------- ---- Points ---- ------------------------------------- All Players -------------------------------------")
        for key, value in sorted(cls._table.items()):
            print(f"|\t{key}\t|\t{value[0]}\t|\t{value[1]}\t|\t{value[2]}\t|")
        print()

    @classmethod
    def add_winner(cls, position, name, points, players):
        "A class level method"
        cls._table[position] = name, points, players
