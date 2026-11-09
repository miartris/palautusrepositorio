class Player:
    def __init__(self, player_data):
        self.name = player_data['name']
        self.nationality = player_data['nationality']
        self.assists = player_data['assists']
        self.goals = player_data['goals']
        self.points = self.assists + self.goals
        self.teams = player_data['team']
        self.games = player_data['games']

    def __repr__(self):
        return f"Player(name={self.name!r}, team={self.teams!r})"

    def __str__(self):
        return f"{self.name:22}{self.teams:16}{self.goals} + {self.assists} = {self.points}"
