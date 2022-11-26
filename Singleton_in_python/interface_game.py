"A Game Interface"

from abc import ABCMeta, abstractmethod


class IGame(metaclass=ABCMeta):
    "A Game Interface"
    @staticmethod
    @abstractmethod
    def add_winner(position, name, points, players):
        "Must implement add_winner"
