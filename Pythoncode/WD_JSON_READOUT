#WD json readout

#for json support import library
import json
import sha256


#variables
json_file = "WD.json"
TestString = "Passwort"

HashString = sha256.sha256(TestString)
Hash = HashString.hexdigest
print(hash)

with open(json_file) as f:
 data = json.load(f)
 
for dic in data: 
   json_team = dic['team_name']
   json_player = dic['player_name']
   json_score = dic['score']
   print( json_team + "\t " + json_player + "\t " + json_score)
#   json_event = dic['event["type"]']
#   print(json_event + " - " + json_team + ": " + json_player)