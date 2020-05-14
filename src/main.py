import os
import pandas
import webscrape

ti9_path = os.path.join("data", "ti9")
ti9_url = "https://www.dotabuff.com/esports/events/284-ti9-group-main/matches?page="
print("Does this work?")

data = webscrape.ti_data(9, ti9_path)
match_ids = data.fetch_match_ids(ti9_url)
print(len(match_ids))
print(match_ids)