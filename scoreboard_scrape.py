import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.scoreboard.com/en/match/SO3Fg7NR/#match-statistics;0').text

soup = BeautifulSoup(source, 'lxml')

home_team = soup.find('div', class_='tname-home').a.text
away_team = soup.find('div', class_='tname-away').a.text
home_score = soup.select_one('.current-result .scoreboard:nth-child(1)').text
away_score = soup.select_one('.current-result .scoreboard:nth-child(2)').text
print("The home team is " + home_team, "and they scored " + home_score)
print()
print("The away team is " + away_team, "and they scored " + away_score)