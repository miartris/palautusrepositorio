class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = list(filter(lambda player: player.nationality == nationality, self.players))
        players = sorted(players_by_nationality, key = lambda player: player.points, reverse = True)
        return players

    def top_scorers_by_team(self, team):
        players_by_team = list(filter(lambda player: player.teams == team, self.players))
        return sorted(players_by_team, key=lambda player: player.points, reverse=True)

    def top_goal_scorers(self, how_many):
        """Palauttaa eniten maaleja tehneet pelaajat maalien mukaan laskevassa järjestyksessä."""
        ranked_players = sorted(
            self.players,
            key=lambda player: player.goals,
            reverse=True
        )

        return ranked_players[:how_many]
