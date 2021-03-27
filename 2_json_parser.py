#! /usr/bin/env python

import json
from sys import argv

# run this command: python your_script.py file_input file_output
script, file_in, file_out = argv

with open(file_in) as j:
	data = json.load(j)

site = data['site']
alerts = site[0]['alerts']

print("Total Number of Issues: " + str(len(alerts)))

parsed = [riskdesc for riskdesc in alerts if riskdesc['riskdesc'] == 'Medium (Medium)' or riskdesc['riskdesc'] == 'High (High)']

print("Number of Prioritized Issues: " + str(len(parsed)))

with open(file_out, 'w') as jp:
	json.dump(parsed, jp)
