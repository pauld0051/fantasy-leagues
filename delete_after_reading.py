import requests
import numpy as np

# Event id
id = 1032723
# apiKey (only 1 works currently)
apiKey = 1

# the 'f' here allows you to pass variables, such as id, into a string inside {}
r = requests.get(
    f'https://www.thesportsdb.com/api/v1/json/{apiKey}/lookupeventstats.php?id={id}')

arr_stats = np.array([r.json()])

r2 = requests.get(
    f'https://www.thesportsdb.com/api/v1/json/{apiKey}/lookupevent.php?id={id}')

arr_events = np.array([r2.json()])

match_status = arr_events[0]['events'][0]['strStatus']

event_id = arr_events[0]['events'][0]['idEvent']
home_team = arr_events[0]['events'][0]['strHomeTeam']
away_team = arr_events[0]['events'][0]['strAwayTeam']
home_score = arr_events[0]['events'][0]['intHomeScore']
away_score = arr_events[0]['events'][0]['intAwayScore']
home_shots_on_goal = arr_stats[0]['eventstats'][0]['intHome']
away_shots_on_goal = arr_stats[0]['eventstats'][0]['intAway']
home_shots_off_goal = arr_stats[0]['eventstats'][1]['intHome']
away_shots_off_goal = arr_stats[0]['eventstats'][1]['intAway']
home_total_shots = arr_stats[0]['eventstats'][2]['intHome']
away_total_shots = arr_stats[0]['eventstats'][2]['intAway']
home_blocked_shots = arr_stats[0]['eventstats'][3]['intHome']
away_blocked_shots = arr_stats[0]['eventstats'][3]['intAway']
home_shots_inside_box = arr_stats[0]['eventstats'][4]['intHome']
away_shots_inside_box = arr_stats[0]['eventstats'][4]['intAway']



print("Check to see if the match has finished before progressing: " + match_status)
print("Use this number to assign to an event ID: " + event_id)
print("Home team and score: " + home_team + " " + home_score)
print("Away team and score: " + away_team + " " + away_score)
print("Home goals: " + home_score)
print("Away goals: " + away_score)
print("Goals against " + home_team + " ", away_score)
print("Goals against " + away_team + " ", home_score)
print(home_team + " had " + home_shots_on_goal + " shots on goal")
print(away_team + " had " + away_shots_on_goal + " shots on goal")
print(home_team + " had " + home_shots_off_goal + " shots off goal")
print(away_team + " had " + away_shots_off_goal + " shots off goal")
print(home_team + " had " + home_total_shots + " shots in total")
print(away_team + " had " + away_total_shots + " shots in total")
print(home_team + " had " + home_blocked_shots + " shots blocked")
print(away_team + " had " + away_blocked_shots + " shots blocked")
print(home_team + " had " + home_shots_inside_box + " shots from inside the box")
print(away_team + " had " + away_shots_inside_box + " shots from inside the box")


