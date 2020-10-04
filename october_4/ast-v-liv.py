# 6J0L2p0r

import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tabulate import tabulate

options = Options()
options.headless = False
chromedriver = "/Users/pauld/Documents/Python/chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path=chromedriver)

# Use the web browser to access the url
driver.get("https://www.scoreboard.com/game/6J0L2p0r/#game-statistics;0")
# wait for all the elements to load
time.sleep(2)

# Use BS4 to parse the page source obtained by the driver
soup = BeautifulSoup(driver.page_source, "html.parser")

# Close the web browser
driver.close()


# This is used to build a list of text values from all tags
def grab_tags(css_selector: str) -> list:
    return [t.getText(strip=True) for t in soup.select(css_selector)]


headers = grab_tags(".detail-experimental .statText--titleValue")
home_team = grab_tags(".detail-experimental .statText--homeValue")
away_team = grab_tags(".detail-experimental .statText--awayValue")

# glue all text items together per stat tab
# A list of tuples -> [(Ball Possesion, 53%, 47%), (Goal Attempts, 10, 5)...]
match_data = list(zip(headers, home_team, away_team))

# home and away team names and score
home_team = soup.find('div', class_='tname-home').a.text
away_team = soup.find('div', class_='tname-away').a.text
home_score = soup.select_one('.current-result .scoreboard:nth-child(1)').text
away_score = soup.select_one('.current-result .scoreboard:nth-child(2)').text

split_value = 15
# split match data list stat table -> there are 15 items per table -> 3 tables
statistics = [
    match_data[i:i+split_value] for i in range(0, len(match_data), split_value)
]

# three stat tables
match, first_half, second_half = statistics

# print any of them
print(tabulate(match, headers=["Stat:", home_team +
                               " " + home_score, away_team + " " + away_score]))
