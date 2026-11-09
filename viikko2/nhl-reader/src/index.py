from rich.console import Console
from rich.table import Table
from rich import print
from player import PlayerStats
from player_reader import PlayerReader



def main():
    console = Console()
    while True:
        season_string = "["
        for x in range(18,27):
            season_string = season_string + f"20{str(x)}-{str(x+1)}"
        season_string = season_string + "]: "
        print(f"[purple] Choose season from {season_string}[/purple]", end="")
        i = input()
        valid_seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25",
                         "2025-26", "2026-27"]
        if not i in valid_seasons:
            print("[bold red]Enter input like 2018-19\n[/bold red]")
        i2 = None
        nationality_list = ["FIN", "USA", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR", "SVK", "DEN", "NED"
                                         , "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS"]
        while not i2 in nationality_list:
            print("Input a nationality from [", end="")
            print(*nationality_list, sep="/", end="")
            print("]: ")
            i2 = input()

        reader = PlayerReader(f"https://studies.cs.helsinki.fi/nhlstats/{i}/players")
        players = reader.get_players()
        stats = PlayerStats(players)
        country_players = stats.top_scorers_by_nationality(i2)
        table = Table(title=f"Players from {i2} season {i}")
        table.add_column("Released", style="white")
        table.add_column("teams", style="magenta")
        table.add_column("goals", style="green")
        table.add_column("assists", style="green")
        table.add_column("points", style="green")
        for player in country_players:
            print(player)
            table.add_row(player.name, player.teams, str(player.goals), str(player.assists), str(player.points))
        console.print(table)

if __name__ == "__main__":
    main()
