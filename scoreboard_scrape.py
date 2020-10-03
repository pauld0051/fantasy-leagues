import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.scoreboard.com/en/match/SO3Fg7NR/#match-statistics;0').text

soup = BeautifulSoup(source, 'lxml')

home_team = soup.find('div', class_='tname-home').a.text

print(home_team)

away_team = soup.find('div', class_='tname-away').a.text

print(away_team)
