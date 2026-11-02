import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        searchFor = "Semenko"
        player = self.stats.search(searchFor)
        self.assertEqual(player.name, searchFor)

    def test_search_not_in_names(self):
        searchFor = "Turhapuro"
        name = self.stats.search(searchFor)
        self.assertEqual(name, None)

    def test_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)

    def test_team_none(self):
        players = self.stats.team("Jokerit")
        self.assertEqual(players, [])

    def test_top(self):
        top = self.stats.top(1)
        self.assertEqual(top.pop(0).name, "Gretzky")
        
