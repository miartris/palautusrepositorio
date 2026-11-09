from player import Player, PlayerStats
from player_reader import PlayerReader

def main():

    reader = PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2024-25/players")
    players = reader.get_players()
    stats = PlayerStats(players)

    finnish_players = stats.top_scorers_by_nationality("FIN")
    
    for player in finnish_players:
        print(player)


if __name__ == "__main__":
    main()
