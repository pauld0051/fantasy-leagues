# fantasy-leagues

*October 2*: Added first scraper set to scrape a known classroom site designed for scraping. Original files and tutorial
found here: <https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/>

Initial scraper uses beautifulsoup: <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>

Next steps: Create a set of commands to scrape one of the known statistical sites.

*October 3*: First attempts at scraping from a previously finalized match.

- Web address for scraping: <https://www.scoreboard.com/en/match/SO3Fg7NR/#match-statistics;0>

- Initial help from: <https://www.youtube.com/watch?v=ng2o98k983k&list=PLss08gouif4S-g6FyV-mAvCC0O2DyIVY9>

- How to get to the nth child of a class: <https://bit.ly/36sOY05>

Continued with adding all the variables. Scraper now accurately picks up:

- *Home* and *Away* teams

- *Goals*. Will need to use this as a calculation for "goals against" too

- *Ball Possession*

- *Goal Attempts*

- *Shots on Goal*

- *Shots off Goal*

- *Blocked Shots*

- *Free Kicks*

- *Corner Kicks*

- *Offsides*

- *Goalkeeper Saves*

- *Fouls*

- *Yellow Cards*

- *Total Passes*

- *Tackles*

- *Attacks*

- *Dangerous Attacks*

Much of the source code was aided by Andrej Kesely at [stackoverflow](https://bit.ly/3lgGmhr).

Second version of the scoreboard scraper now also works. This is titled selenium_scraper.py. This requires an install of [selenium](https://pypi.org/project/selenium/) and [chrome driver](https://chromedriver.chromium.org/downloads) with path. Before installing check your Chrome browser version because this actually opens a browser, reads it, closes it, and parses the information.

Credit for the selenium version: baduker at [stackoverflow](https://bit.ly/3lgGmhr).

The next phase is to get this data into usable formats.

*October 4*: Completed one full week for data but found a bug occurring with the Man-United v Tottenham game.

*'match, first_half, second_half = statistics*
*ValueError: too many values to unpack (expected 3)*

It is not clear yet what caused this error to only occur in this game. The current fix was to use the code from scoreboard_scrape.py. This ran successfully and may become the code for the scraper as opposed to the more neat and tidy selenium_scraper.py.

- Added CSV support for scoreboard_scrape.py

Currently the CSV support, although works as expected, extends the code to over 250 lines lone. The selenium_scraper code is significantly shorter, but CSV support has not been as easy to come by. Currently, red cards (for instance) throw up a noneType error as if no red cards are given, the stat is not available on the site. This means that the code stops if no red cards are present. Although soup can skip this error, it would then mean the CSV won't show "0" for red cards. Working on a fix for this currently.

- Update on Red Card Error
Have fixed the error with help from Gad at [stackoverflow](https://bit.ly/33uiMaM)

All data now successfully enters CSV format.
