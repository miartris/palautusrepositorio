from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats


NATIONALITIES = [
    "FIN", "USA", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR", "SVK",
    "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS",
]

def _prompt_choice(console, prompt, choices):
    choice_text = "/".join(choices)
    while True:
        console.print(f"{prompt} [{choice_text}]: ", end="")
        choice = input().strip()
        if choice in choices:
            return choice
        console.print("Invalid choice.")


def _choose_season(console):
    seasons = [f"20{year}-{year + 1:02d}" for year in range(18, 27)]
    return _prompt_choice(console, "Choose season", seasons)


def _choose_ranking(stats, players, season, console):
    ranking_type = _prompt_choice(
        console,
        "Show top scorers by (1) nationality or (2) team?",
        ["1", "2"],
    )
    if ranking_type == "1":
        nationality = _prompt_choice(console, "Input a nationality", NATIONALITIES)
        return (
            f"Players from {nationality} season {season}",
            stats.top_scorers_by_nationality(nationality),
        )

    teams = sorted({
        team.strip()
        for player in players
        for team in player.teams.split(",")
    })
    team = _prompt_choice(console, "Input a team", teams)
    return (
        f"Top point scorers for {team} season {season}",
        stats.top_scorers_by_team(team),
    )


def _display_players(console, title, players):
    table = Table(title=title)
    table.add_column("Player", style="white")
    table.add_column("Team", style="magenta")
    table.add_column("goals", style="green")
    table.add_column("assists", style="green")
    table.add_column("points", style="green")
    for player in players:
        table.add_row(
            player.name,
            player.teams,
            str(player.goals),
            str(player.assists),
            str(player.points),
        )
    console.print(table)


def main():
    console = Console()
    while True:
        season = _choose_season(console)
        reader = PlayerReader(
            f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        )
        players = reader.get_players()
        stats = PlayerStats(players)
        title, ranked_players = _choose_ranking(stats, players, season, console)
        _display_players(console, title, ranked_players)

if __name__ == "__main__":
    main()
