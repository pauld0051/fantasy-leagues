from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator
from pprint import pprint

teams = ["Arsenal", "Aston Villa", "Brighton", "Burnley",
         "Chelsea", "Crystal Palace", "Everton", "Fulham",
         "Leeds", "Leicester", "Liverpool", "Man City",
         "Man Utd", "Newcastle", "Sheffield Utd", "Southampton",
         "Spurs", "West Brom", "West Ham", "Wolves"]

home_teams = ["Arsenal", "Aston Villa", "Brighton", "Burnley",
              "Chelsea", "Crystal Palace", "Everton", "Fulham",
              "Leeds", "Leicester"]

away_teams = ["Liverpool", "Man City",
              "Man Utd", "Newcastle", "Sheffield Utd", "Southampton",
              "Spurs", "West Brom", "West Ham", "Wolves"]


def get_team_options(answers):
    options = teams
    return options


def get_away_team_options(answers):
    options = away_teams
    return options


def get_home_team_options(answers):
    options = home_teams
    return options


questions = [
    {
        'type': 'list',
        'name': 'home_team_goals',
        'message': "Choose a home team that you think will score the most goals",
        'choices': get_home_team_options,

    },

    {
        'type': 'list',
        'name': 'away_team_goals',
        'message': "Choose an away team that you think will score the most goals",
        'choices': get_away_team_options,

    },
]

answers = prompt(questions)
print_json(answers)  # use the answers as input for your app
pprint(answers)
