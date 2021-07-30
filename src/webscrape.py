# %%
import urllib
import urllib.request
import requests as r
import os
from bs4 import BeautifulSoup
import pandas
import time
# %%

#ti9_path = os.path.join("data", "ti9")
#ti9_url = "https://www.dotabuff.com/esports/events/284-ti9-group-main/matches?page="

class db_match_ids():
    def __init__(self, event_url):
        #temp code
        if(event_url.find("ti9") == -1):
            print("Warning: Non ti9 events are not supported properly atm.")
        self.event_url = event_url
    
    #outside function for getting match ids
    def get_match_ids(self):
        if(self.match_ids is None):
            self.match_ids = []
            status = True
            i = 11
            while(status):
                try:
                    request = r.get(self.event_url+str(i), headers =
                        {"User-Agent": "Mozilla/5.0 "})  
                    status, add_ids = self.request_matches(request.text)
                    self.match_ids.extend(add_ids)
                except r.exceptions.RequestException as e:
                    status = False
                    print(e.reason)
                #don't make dotabuff mad :)
                time.sleep(1)
                i += 1
        return self.match_ids

    def request_matches(self, content):
        cur_ids = []
        soup = BeautifulSoup(content, 'html.parser')
        #cur_page = soup.find("span", attrs = {"class": "page current"})
        status = True
        tbody = soup.find("table", attrs = {"class": "table table-striped table-condensed recent-esports-matches"}).tbody 
        for trow in tbody.children:
            if len(trow.contents) == 1 and 'no-data' in trow.td['class']:
                status = False
                break
            else:
                cur_ids.append(trow.find('td', attrs={"class": "cell-mediumlarge"}).a['href'])
        return status, cur_ids

    #private helper methods for each specific feature

class db_match_data():
    '''
    Initiate with file path for where to store event data, 
    Takes selected match features and stores in a pandas dataframe 
    Inputs: 
    event_path - directory to put data, current one by default
    match_ids - list of match ids 
    '''
    def __init__(self, event_path=".", match_ids):
        os.makedirs(event_path, exist_ok = True)
        self.event_path = event_path
        if(match_ids is list):
            self.match_ids = match_ids
        elif(match_ids is db_match_data):
            self.match_ids = match_ids.get_match_ids()
        else:
            print("Match ids are not formatted properly!")
            self.match_ids = []
        
        index = [(x.split("/", maxsplit = 1))[1] for x in self.match_ids]
        #columns = []
        self.df = pd.dataframe(index=index)        
    
    def get_match_ids(self):
        return self.match_ids
    
    # %%
    # sample match id - 4982200558 
    # liquid vs eg lower bracket game 2
    # Input: data_type
    def connect(self, data_type, match_id):
        #don't make dotabuff mad :)
        time.sleep(0.5)
        #faking a user-agent
        try:
            request = r.get("https://www.dotabuff.com/matches/" + str(match_id) + "/" + str(data_type), 
                headers = {"User-Agent": "Mozilla/5.0 "})  
            return request.text
        except r.exceptions.RequestException as e:
            print(e.reason)
        return None

    # %%
    #
    def get_match_data(self):
        cols = ['victory'] 
        self.df = pd.DataFrame(columns = cols)
        for cur_id in self.match_ids:
            data = main_page(cur_id)
            data.update()
            self.df.append(data)
        return self.df

    # %%
    # Extracting kills from main match page 
    def main_page(self, match_id):
        content = connect("", match_id)
        if(content is None):
            print("Failed to connect, terminating")
            return None
        else:
            data = {}
            soup = BeautifulSoup(content, 'html.parser')
            match_res = soup.find("div", attrs={"class": "match-show"})
            #first direct child div as of 7/16/2020
            match_winner = match_res.find("div", recursive=False)
            #who won
            if("radiant" in match_winner['class']):
                data['victory'] = 'radiant'
            else:
                data['victory'] = 'dire'
            kills_dur = match_res.find("div", attrs={"class": "match-victory-subtitle"}).children
            data['r_kill'], data['dur'], data['d_kill'] = [str(x.string) for x in kills_dur]
            radiant_data = soup.find("div", attrs={"class": "team-results"}).find("section", attrs={"class": "radiant"}).find("table")
            dire_data = soup.find("div", attrs={"class": "team-results"}).find("section", attrs={"class": "radiant"}).find("table")
            return data

    # %%
    def ind_team_result(self, table):
        team_data = {}
        cur = table.find("tbody")



    # %%
    #get items/heroes        
    #create categories of heroes/itmes
    def builds(self):
        
    def teamcomp(self):

    #get farm distribution (xp and gold)
    def farm(self):
        

    #get damage/healing distribution/cc time
    def combat(self):

    #get time of first tower/time of tier3
    def objectives(self):


    


#temp driver code
if __name__ == "__main__":
    ti9_path = os.path.join("data", "ti9")
    ti9_url = "https://www.dotabuff.com/esports/events/284-ti9-group-main/matches?page="
    print("Does this work?")

    data = ti_data(9, ti9_path)
    match_ids = fetch_match_ids(ti9_url)
    print(len(match_ids))
    print(match_ids)



# %%
# Excess testing code
    sample_url = "https://www.dotabuff.com/matches/4983489657"
    

# %%

