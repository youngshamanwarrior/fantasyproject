import requests
import numpy as np
import pandas as pd
import espn_api
import config
from espn_api.football import League
league = League(league_id=1624952, year=2024, espn_s2= config.espn_s2, swid= config.swid)

treTeam = league.teams[0]
willTeam = league.teams[1]
louTeam = league.teams[2]
nickTeam = league.teams[3]
joeTeam = league.teams[4]
austinTeam = league.teams[5]
hugeyTeam = league.teams[6]
jackTeam = league.teams[7]
lukeTeam = league.teams[8]
billyTeam = league.teams[9]
marshTeam = league.teams[10]
connorTeam = league.teams[11]

print(marshTeam.roster)
puka_nacua= marshTeam.roster[0]
print(puka_nacua.lineupSlot)



