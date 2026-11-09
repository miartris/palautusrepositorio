import pytest

from src.player import Player
from src.player_stats import PlayerStats


def make_player(name, nationality, assists, goals, team):
    return Player(
        {
            "name": name,
            "nationality": nationality,
            "assists": assists,
            "goals": goals,
            "team": team,
            "games": 50,
        }
    )


@pytest.fixture

def player_stats():
    players = [
        make_player("Alex Finnish", "FIN", assists=20, goals=10, team="AAA"),
        make_player("Bobby Finnish", "FIN", assists=5, goals=20, team="BBB"),
        make_player("Casey Canadian", "CAN", assists=15, goals=15, team="AAA"),
    ]
    return PlayerStats(players)


def test_top_scorers_by_nationality_filters_and_sorts_by_points(player_stats):
    result = player_stats.top_scorers_by_nationality("FIN")

    assert [player.name for player in result] == ["Alex Finnish", "Bobby Finnish"]
    assert [player.points for player in result] == [30, 25]


def test_top_scorers_by_nationality_returns_empty_for_unknown_nationality(player_stats):
    assert player_stats.top_scorers_by_nationality("SWE") == []


def test_top_scorers_by_team_filters_and_sorts_by_points(player_stats):
    result = player_stats.top_scorers_by_team("AAA")

    assert [player.name for player in result] == ["Alex Finnish", "Casey Canadian"]
    assert [player.points for player in result] == [30, 30]


def test_top_scorers_by_team_returns_empty_for_unknown_team(player_stats):
    assert player_stats.top_scorers_by_team("ZZZ") == []


def test_top_goal_scorers_sorts_by_goals_and_limits_results(player_stats):
    result = player_stats.top_goal_scorers(2)

    assert [player.name for player in result] == ["Bobby Finnish", "Casey Canadian"]
    assert [player.goals for player in result] == [20, 15]


def test_top_goal_scorers_returns_empty_for_zero_limit(player_stats):
    assert player_stats.top_goal_scorers(0) == []
