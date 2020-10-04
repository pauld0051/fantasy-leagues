import requests
import re
import csv
from bs4 import BeautifulSoup

source = requests.get('https://www.scoreboard.com/en/match/SO3Fg7NR/#match-statistics;0').text

soup = BeautifulSoup(source, 'lxml')

home_team = soup.find('div', class_='tname-home').a.text
away_team = soup.find('div', class_='tname-away').a.text
home_score = soup.select_one('.current-result .scoreboard:nth-child(1)').text
away_score = soup.select_one('.current-result .scoreboard:nth-child(2)').text
print("The home team is " + home_team, "and they scored " + home_score)
print("The away team is " + away_team, "and they scored " + away_score)
print()

row1 = "Goals For"
row2 = "Possession"
row3 = "Goal Attempts"
row4 = "Shot on Goal"
row5 = "Shots off Goal"
row6 = "Blocked Shots"
row7 = "Free kicks"
row8 = "Corner Kicks"
row9 = "Offsides"
row10 = "Goalkeeper Saves"
row11 = "Fouls"
row12 = "Red Cards"
row13 = "Yellow Cards"
row14 = "Total Passes"
row15 = "Tackles"
row16 = "Attacks"
row17 = "Dangerous Attacks"
row18 = "Goals Against"

url = 'https://www.scoreboard.com/en/match/SO3Fg7NR/#match-statistics;0'

headers = {'X-Fsign': 'SW9D1eZo'}
match_id = re.search(r'match/([^/]+)/', url).group(1)
data_url = 'https://d.scoreboard.com/en/x/feed/d_st_{match_id}_en_1'.format(
    match_id = match_id)

soup = BeautifulSoup(requests.get(
    data_url, headers=headers).content, 'html.parser')

# locate row, that contains "Ball Possession":
row = soup.select_one('.statRow:has(*:contains("Ball Possession"))')

home_value2 = row.select_one('.statText--homeValue').text.replace('%', '')
away_value2 = row.select_one('.statText--awayValue').text.replace('%', '')

print(home_team, "had " + home_value2, "% ball possession") 
print(away_team, "had " + away_value2, "% ball possession")
print()

# locate row, that contains "Goal Attempts":
row = soup.select_one('.statRow:has(*:contains("Goal Attempts"))')

home_value3 = row.select_one('.statText--homeValue').text
away_value3 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value3, "goal attempts")
print(away_team, "had " + away_value3, "goal attempts")
print()

# locate row, that contains "Shots on Goal":
row = soup.select_one('.statRow:has(*:contains("Shots on Goal"))')

home_value4 = row.select_one('.statText--homeValue').text
away_value4 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value4, "shots on goal")
print(away_team, "had " + away_value4, "shots on goal")
print()

# locate row, that contains "Shots off Goal":
row = soup.select_one('.statRow:has(*:contains("Shots off Goal"))')

home_value5 = row.select_one('.statText--homeValue').text
away_value5 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value5, "shots off goal")
print(away_team, "had " + away_value5, "shots off goal")
print()

# locate row, that contains "Blocked Shots":
row = soup.select_one('.statRow:has(*:contains("Blocked Shots"))')

home_value6 = row.select_one('.statText--homeValue').text
away_value6 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value6, "blocked shots")
print(away_team, "had " + away_value6, "blocked shots")
print()

# locate row, that contains "Free Kicks":
row = soup.select_one('.statRow:has(*:contains("Free Kicks"))')

home_value7 = row.select_one('.statText--homeValue').text
away_value7 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value7, "free kicks")
print(away_team, "had " + away_value7, "free kicks")
print()

# locate row, that contains "Corner Kicks":
row = soup.select_one('.statRow:has(*:contains("Corner Kicks"))')

home_value8 = row.select_one('.statText--homeValue').text
away_value8 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value8, "corner kicks")
print(away_team, "had " + away_value8, "corner kicks")
print()

# locate row, that contains "Offsides":
row = soup.select_one('.statRow:has(*:contains("Offsides"))')

home_value9 = row.select_one('.statText--homeValue').text
away_value9 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value9, "offsides")
print(away_team, "had " + away_value9, "offsides")
print()

# locate row, that contains "Goalkeeper Saves":
row = soup.select_one('.statRow:has(*:contains("Goalkeeper Saves"))')

home_value10 = row.select_one('.statText--homeValue').text
away_value10 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value10, "goalkeeper saves")
print(away_team, "had " + away_value10, "goalkeeper saves")
print()

# locate row, that contains "Fouls":
row = soup.select_one('.statRow:has(*:contains("Fouls"))')

home_value11 = row.select_one('.statText--homeValue').text
away_value11 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value11, "fouls")
print(away_team, "had " + away_value11, "fouls")
print()

# locate row, that contains "Red Cards": Currently commented out until a noneType error can be overcome
#row = soup.select_one('.statRow:has(*:contains("Red Cards"))')

#home_value12 = row.select_one('.statText--homeValue').text
#away_value12 = row.select_one('.statText--awayValue').text

#print(home_team, "had " + home_value12, "red cards")
#print(away_team, "had " + away_value12, "red cards")
#print()

# locate row, that contains "Yellow Cards":
row = soup.select_one('.statRow:has(*:contains("Yellow Cards"))')

home_value13 = row.select_one('.statText--homeValue').text
away_value13 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value13, "yellow cards")
print(away_team, "had " + away_value13, "yellow cards")
print()

# locate row, that contains "Total Passes":
row = soup.select_one('.statRow:has(*:contains("Total Passes"))')

home_value14 = row.select_one('.statText--homeValue').text
away_value14 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value14, "total passes")
print(away_team, "had " + away_value14, "total passes")
print()

# locate row, that contains "Tackles":
row = soup.select_one('.statRow:has(*:contains("Tackles"))')

home_value15 = row.select_one('.statText--homeValue').text
away_value15 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value15, "tackles")
print(away_team, "had " + away_value15, "tackles")
print()

# locate row, that contains "Attacks":
row = soup.select_one('.statRow:has(*:contains("Attacks"))')

home_value16 = row.select_one('.statText--homeValue').text
away_value16 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value16, "attacks")
print(away_team, "had " + away_value16, "attacks")
print()

# locate row, that contains "Dangerous Attacks":
row = soup.select_one('.statRow:has(*:contains("Dangerous Attacks"))')

home_value17 = row.select_one('.statText--homeValue').text
away_value17 = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value17, "dangerous attacks")
print(away_team, "had " + away_value17, "dangerous attacks")
print()

with open('week_x.csv', 'w', newline='') as csvfile:
    fieldnames = ['Stats:', home_team, away_team]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(
        {'Stats:': row1, home_team: home_score, away_team: away_score})
    writer.writerow(
        {'Stats:': row2, home_team: home_value2, away_team: away_value2})
    writer.writerow(
        {'Stats:': row3, home_team: home_value3, away_team: away_value3})
    writer.writerow(
        {'Stats:': row4, home_team: home_value4, away_team: away_value4})
    writer.writerow(
        {'Stats:': row5, home_team: home_value5, away_team: away_value5})
    writer.writerow(
        {'Stats:': row6, home_team: home_value6, away_team: away_value6})
    writer.writerow(
        {'Stats:': row7, home_team: home_value7, away_team: away_value7})
    writer.writerow(
        {'Stats:': row8, home_team: home_value8, away_team: away_value8})
    writer.writerow(
        {'Stats:': row9, home_team: home_value9, away_team: away_value9})
    writer.writerow(
        {'Stats:': row10, home_team: home_value10, away_team: away_value10})
    writer.writerow(
        {'Stats:': row11, home_team: home_value11, away_team: away_value11})
    #writer.writerow(
        #{'Stats:': row12, home_team: home_value12, away_team: away_value12})
    writer.writerow(
        {'Stats:': row13, home_team: home_value13, away_team: away_value13})
    writer.writerow(
        {'Stats:': row14, home_team: home_value14, away_team: away_value14})
    writer.writerow(
        {'Stats:': row15, home_team: home_value15, away_team: away_value15})
    writer.writerow(
        {'Stats:': row16, home_team: home_value16, away_team: away_value16})
    writer.writerow(
        {'Stats:': row17, home_team: home_value17, away_team: away_value17})
    writer.writerow(
        {'Stats:': row18, home_team: away_score, away_team: home_score})
