import urllib
import urllib.request
import os
from bs4 import BeautifulSoup
import pandas
import time

#ti9_path = os.path.join("data", "ti9")
#ti9_url = "https://www.dotabuff.com/esports/events/284-ti9-group-main/matches?page="

class ti_data():
    def __init__(self, ti, ti_path):
        #temp code
        if(ti != 9):
            print("Warning: Other events are not supported properly atm.")
        self.ti = ti
        os.makedirs(ti_path, exist_ok = True)
        self.ti_path = ti_path
    
    #outside function for getting match ids
    def fetch_match_ids(self, ti_url):
        self.match_ids = []
        status = True
        i = 11
        while(status):
            #faking a user-agent
            request = urllib.request.Request(ti_url+str(i), headers =
                {"User-Agent": "Mozilla/5.0 "})  #(Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"})
            #with urllib.request.urlopen(request) as response:
            try:
                response = urllib.request.urlopen(request)
                status, add_ids = self.request_matches(response)
                self.match_ids.extend(add_ids)
            except urllib.error.HTTPError as e:
                status = False
                print(e.reason)
            #don't make dotabuff mad :)
            time.sleep(1)
            i += 1
        return self.match_ids

    def request_matches(self, response):
        cur_ids = []
        content = response.read()
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


    def get_match_data(self, match_ids):
        #TODO
        pass

    #private helper methods for each specific feature

#look at https://kaijento.github.io/2017/04/09/web-scraping-dotabuff.com/

#temp driver code

