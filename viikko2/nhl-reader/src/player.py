class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.points = self.assists + self.goals
        self.teams = dict['team']
        self.games = dict['games']
        self.id = dict['id']

    def __str__(self):
        return f"{self.name:20}{self.teams:16}{self.goals} + {self.assists} = {self.points}"



class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = list(filter(lambda player: player.nationality == nationality, self.players))
        players = sorted(players_by_nationality, key = lambda player: player.points, reverse = True)
        return players
        