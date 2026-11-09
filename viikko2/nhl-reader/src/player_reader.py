import requests
from player import Player

class PlayerReader:
    def __init__(self, fetch_url):
        self.url = fetch_url

    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players
