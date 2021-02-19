# Imports
import re
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

# Request the page
page = rq.get("https://en.wikipedia.org/wiki/List_of_video_game_franchises")

# Create soup
soup = BeautifulSoup(page.content, "html.parser")

# Find all links which link to the other Wikipedia pages (for instance, videogame pages)
all_links = soup.find_all("a", attrs={"href": re.compile("^/wiki")})

# Extract titles from link (it will extract everything, not only game titles)
all_titles = [title.get_text() for title in all_links]

# Extract only game titles (the last in 'Zuma')
game_titles = all_titles[:785]

# Esport to a csv
pd.Series(game_titles).to_csv("./data/game_titles.csv")