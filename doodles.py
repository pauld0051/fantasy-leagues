from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator
from pprint import pprint


def get_team_options(answers):
    options = ["Arsenal", "Aston Villa", "Brighton", "Burnley",
               "Chelsea", "Crystal Palace", "Everton", "Fulham",
               "Leeds", "Leicester", "Liverpool", "Man City",
               "Man Utd", "Newcastle", "Sheffield Utd", "Southampton",
               "Spurs", "West Brom", "West Ham", "Wolves"]
    return options


def get_away_team_options(answers):
    options = ["Liverpool", "Man City",
               "Man Utd", "Newcastle", "Sheffield Utd", "Southampton",
               "Spurs", "West Brom", "West Ham", "Wolves"]
    return options


def get_home_team_options(answers):
    options = ["Arsenal", "Aston Villa", "Brighton", "Burnley",
               "Chelsea", "Crystal Palace", "Everton", "Fulham",
               "Leeds", "Leicester"]
    return options

def get_team_selections():
    selections_prompt = {
        'type': 'list',
        'name': 'selections',
        'message': 'Choose the team that.... Insert variable here',
        'choices': get_team_options
    }
    answers = prompt.prompt(selections_prompt)
    return answers['selections']

def get_away_team_options(answers):
    options = ["Liverpool", "Man City",
               "Man Utd", "Newcastle", "Sheffield Utd", "Southampton",
               "Spurs", "West Brom", "West Ham", "Wolves"]
    return options


def get_home_team_options(answers):
    options = ["Arsenal", "Aston Villa", "Brighton", "Burnley",
               "Chelsea", "Crystal Palace", "Everton", "Fulham",
               "Leeds", "Leicester"]
    return options


def home_goals():
    selection = get_home_team_options()
    print(home_goals())
    home_goals()

