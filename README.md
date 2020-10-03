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
