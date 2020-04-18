import requests
import json
import pandas as pd

"""
https://api.opendota.com/api/schema
https://github.com/chriscdm/OpenDota_API_Call/blob/master/00_Original_Data_Collection.ipynb
https://www.opendota.com/explorer
https://api.opendota.com/api
https://gamedev.stackexchange.com/questions/177283/how-to-use-open-dota-api
"""




r = requests.get("https://api.opendota.com/api/leagues/")

r2 = requests.get("https://api.opendota.com/api/leagues/11823/")

with open('output.json', 'w') as out:
                json.dump(r.json(), out, sort_keys=True, indent='\t')