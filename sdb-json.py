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

#print(arr_stats)

r2 = requests.get(
    f'https://www.thesportsdb.com/api/v1/json/{apiKey}/lookupevent.php?id={id}')

arr_events = np.array([r2.json()])

#print(arr_events)
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
home_outside_box = arr_stats[0]['eventstats'][5]['intHome']
away_outside_box = arr_stats[0]['eventstats'][5]['intAway']
home_corners = arr_stats[0]['eventstats'][6]['intHome']
away_corners = arr_stats[0]['eventstats'][6]['intAway']
home_offsides = arr_stats[0]['eventstats'][7]['intHome']
away_offsides = arr_stats[0]['eventstats'][7]['intAway']
home_possession = arr_stats[0]['eventstats'][8]['intHome']
away_possession = arr_stats[0]['eventstats'][8]['intAway']
home_yellow_cards = arr_stats[0]['eventstats'][9]['intHome']
away_yellow_cards = arr_stats[0]['eventstats'][9]['intAway']
home_red_cards = arr_stats[0]['eventstats'][10]['intHome']
away_red_cards = arr_stats[0]['eventstats'][10]['intAway']
home_saves = arr_stats[0]['eventstats'][11]['intHome']
away_saves = arr_stats[0]['eventstats'][11]['intAway']
home_total_passes = arr_stats[0]['eventstats'][12]['intHome']
away_total_passes = arr_stats[0]['eventstats'][12]['intAway']
home_accurate_passes = arr_stats[0]['eventstats'][13]['intHome']
away_accurate_passes = arr_stats[0]['eventstats'][13]['intAway']
home_passes_percent = arr_stats[0]['eventstats'][14]['intHome']
away_passes_percent = arr_stats[0]['eventstats'][14]['intAway']
home_fouls = arr_stats[0]['eventstats'][15]['intHome']
away_fouls = arr_stats[0]['eventstats'][15]['intAway']

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
print(home_team + " took " + home_shots_inside_box + " shots from inside the box")
print(away_team + " took " + away_shots_inside_box + " shots from inside the box")
print(home_team + " took " + home_outside_box + " shots from outside the box")
print(away_team + " took " + away_outside_box + " shots from outside the box")
print(home_team + " had " + home_corners + " corners")
print(away_team + " had " + away_corners + " corners")
print(home_team + " had " + home_offsides + " offsides")
print(away_team + " had " + away_offsides + " offsides")
print(home_team + " had " + home_possession + "% possession")
print(away_team + " had " + away_possession + "% possession")
print(home_team + " had " + home_yellow_cards + " yellow cards")
print(away_team + " had " + away_yellow_cards + " yellow cards")
print(home_team + " had " + home_red_cards + " red cards")
print(away_team + " had " + away_red_cards + " red cards")
print(home_team + " had " + home_saves + " goalkeeper saves")
print(away_team + " had " + away_saves + " goalkeeper saves")
print(home_team + " had " + home_total_passes + " total passes")
print(away_team + " had " + away_total_passes + " total passes")
print(home_team + " had " + home_accurate_passes + " accurate passes")
print(away_team + " had " + away_accurate_passes + " accurate passes")
print(home_team + " had " + home_passes_percent + "% pass accuracy")
print(away_team + " had " + away_passes_percent + "% pass accuracy")
print(home_team + " had " + home_fouls + " fouls")
print(away_team + " had " + away_fouls + " fouls")







