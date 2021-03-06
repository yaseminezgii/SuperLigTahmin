import pyfiglet
result = pyfiglet.figlet_format("Puan Durumu") 
print(result) 

import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

url = "https://tr.beinsports.com/lig/super-lig/puan-durumu"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

players={
"Player1": ['Galatasaray', 'Trabzonspor', 'Fenerbahçe', 'M.Başakşehir', 'DG Sivasspor','Göztepe','Beşiktaş', 'Aytemiz Alanyaspor'],
"Player2" : ['M.Başakşehir','Trabzonspor','DG Sivasspor', 'Galatasaray','Fenerbahçe', 'Aytemiz Alanyaspor','Beşiktaş','Göztepe'],
"Player3": ['Fenerbahçe', 'Trabzonspor','M.Başakşehir','Galatasaray','Aytemiz Alanyaspor','DG Sivasspor','Göztepe','Beşiktaş'],
"Player4":  ['Trabzonspor','M.Başakşehir','Galatasaray','Fenerbahçe','DG Sivasspor','Beşiktaş', 'Göztepe','Aytemiz Alanyaspor'],
"Player5": ['Galatasaray', 'Trabzonspor', 'Fenerbahçe','Beşiktaş','DG Sivasspor','Aytemiz Alanyaspor','Göztepe','Gaziantep FK'],
"Player6" : ['Trabzonspor','M.Başakşehir','Galatasaray','Fenerbahçe','DG Sivasspor','Beşiktaş','Aytemiz Alanyaspor','Göztepe'],
"Player7": ['Galatasaray','M.Başakşehir', 'Trabzonspor','Fenerbahçe','DG Sivasspor','Beşiktaş','Aytemiz Alanyaspor','Göztepe'],
"Player8": ['Trabzonspor','Galatasaray','M.Başakşehir','Fenerbahçe','DG Sivasspor','Beşiktaş','Aytemiz Alanyaspor','Göztepe']
}
  
teams = [team.text.strip() for team in soup.find_all("td", {"class":"team_link"})]
#print('Güncel Puan Tablosu :' "\n", "\n", teams, "\n")

def main(players):
    
    for player, p_teams in players.items(): # loop over each player and answers
        # e.g.
        # player = Player1
        # p_teams = ['Galatasaray', 'Trabzonspor', ...]
        count = 0
        count_2 = 0
        if teams[:1] == p_teams[:1]:
            count+=2           
        for x,y in enumerate(p_teams):
            if teams.index(y) - p_teams.index(y)==0:
                count += 1     
            if teams.index(y) != p_teams.index(y):            
                a = p_teams.index(y)-teams.index(y)
                if a>0:
                    a*=-1
                count_2 += a                
        totalpuan = count+count_2
        print (player, "Toplam Puan:", totalpuan)

main(players)  # pass dictionary to function
