import os
import json
from pprint import pprint

current_location = os.path.dirname(os.path.abspath(__file__))

jsondata = open(current_location+'/account_manager/static/css/fontawesome/fontawesome_icons_list.json').read()
jsondata = json.loads(jsondata)

pprint(list(jsondata.items()))