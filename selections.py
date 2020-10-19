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

    {
        'type': 'list',
        'name': 'shots_on_goal',
        'message': "Choose a team that you think will have the most shots on goal",
        'choices': get_team_options,

    },

    {
        'type': 'list',
        'name': 'shots_off_goal',
        'message': "Choose a team that you think will have the most shots off goal",
        'choices': get_team_options,

    },
]

answers = prompt(questions)
#print_json(answers)
print(answers)
print(answers['home_team_goals']) # These are the parameters that need to be removed after each answer selected. 
print(answers['away_team_goals'])
