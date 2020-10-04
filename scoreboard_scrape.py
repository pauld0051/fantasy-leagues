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
#home_stats = soup.select_one('div', id='tab-match-statistics', class_=statText--homeValue:nth-child(1)').text
#print(home_stats)

url = 'https://www.scoreboard.com/en/match/SO3Fg7NR/#match-statistics;0'

headers = {'X-Fsign': 'SW9D1eZo'}
match_id = re.search(r'match/([^/]+)/', url).group(1)
data_url = 'https://d.scoreboard.com/en/x/feed/d_st_{match_id}_en_1'.format(
    match_id = match_id)

soup = BeautifulSoup(requests.get(
    data_url, headers=headers).content, 'html.parser')

# locate row, that contains "Ball Possession":
row = soup.select_one('.statRow:has(*:contains("Ball Possession"))')

home_value = row.select_one('.statText--homeValue').text.replace('%', '')
away_value = row.select_one('.statText--awayValue').text.replace('%', '')

print(home_team, "had " + home_value, "% ball possession") 
print(away_team, "had " + away_value, "% ball possession")
print()

# locate row, that contains "Goal Attempts":
row = soup.select_one('.statRow:has(*:contains("Goal Attempts"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "goal attempts")
print(away_team, "had " + away_value, "goal attempts")
print()

# locate row, that contains "Shots on Goal":
row = soup.select_one('.statRow:has(*:contains("Shots on Goal"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "shots on goal")
print(away_team, "had " + away_value, "shots on goal")
print()

# locate row, that contains "Shots off Goal":
row = soup.select_one('.statRow:has(*:contains("Shots off Goal"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "shots off goal")
print(away_team, "had " + away_value, "shots off goal")
print()

# locate row, that contains "Blocked Shots":
row = soup.select_one('.statRow:has(*:contains("Blocked Shots"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "blocked shots")
print(away_team, "had " + away_value, "blocked shots")
print()

# locate row, that contains "Free Kicks":
row = soup.select_one('.statRow:has(*:contains("Free Kicks"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "free kicks")
print(away_team, "had " + away_value, "free kicks")
print()

# locate row, that contains "Corner Kicks":
row = soup.select_one('.statRow:has(*:contains("Corner Kicks"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "corner kicks")
print(away_team, "had " + away_value, "corner kicks")
print()

# locate row, that contains "Offsides":
row = soup.select_one('.statRow:has(*:contains("Offsides"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "offsides")
print(away_team, "had " + away_value, "offsides")
print()

# locate row, that contains "Goalkeeper Saves":
row = soup.select_one('.statRow:has(*:contains("Goalkeeper Saves"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "goalkeeper saves")
print(away_team, "had " + away_value, "goalkeeper saves")
print()

# locate row, that contains "Fouls":
row = soup.select_one('.statRow:has(*:contains("Fouls"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "fouls")
print(away_team, "had " + away_value, "fouls")
print()

# locate row, that contains "Yellow Cards":
row = soup.select_one('.statRow:has(*:contains("Yellow Cards"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "yellow cards")
print(away_team, "had " + away_value, "yellow cards")
print()

# locate row, that contains "Total Passes":
row = soup.select_one('.statRow:has(*:contains("Total Passes"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "total passes")
print(away_team, "had " + away_value, "total passes")
print()

# locate row, that contains "Tackles":
row = soup.select_one('.statRow:has(*:contains("Tackles"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "tackles")
print(away_team, "had " + away_value, "tackles")
print()

# locate row, that contains "Attacks":
row = soup.select_one('.statRow:has(*:contains("Attacks"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "attacks")
print(away_team, "had " + away_value, "attacks")
print()

# locate row, that contains "Dangerous Attacks":
row = soup.select_one('.statRow:has(*:contains("Dangerous Attacks"))')

home_value = row.select_one('.statText--homeValue').text
away_value = row.select_one('.statText--awayValue').text

print(home_team, "had " + home_value, "dangerous attacks")
print(away_team, "had " + away_value, "dangerous attacks")
print()

