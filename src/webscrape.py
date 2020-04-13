import urllib
import os
import bs4

ti9_path = os.path.join("data", "ti9")
ti9_url = "https://www.dotabuff.com/esports/events/284-ti9-group-main/matches?page="

def fetch_match_id(ti):
    #todo -> add ability to analyze previous internationals/other DPC events
    if(ti != 9):
        print("Other events not available right now.")
    else:
        os.makedirs(ti9_path, exist_ok = True)
        for i in range(1, 2):
            content = ""
            #faking a user-agent
            request = urllib.request.Request(ti9_url+str(i), headers =
             {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"})
            response = urllib.request.urlopen(request)
            try:
                content = response.read()
                print(content)
            finally:
                response.close()

fetch_match_id(9)

                
