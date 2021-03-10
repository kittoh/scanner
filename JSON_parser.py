#! /usr/bin/env python

import json

with open('test_report.json', ) as j:
	data = json.load(j)

site = data['site']
alerts = site[0]['alerts']

print("Total Number of Issues: " + str(len(alerts)))

parsed = [riskdesc for riskdesc in alerts if riskdesc['riskdesc'] == 'Medium (Medium)' or riskdesc['riskdesc'] == 'High (High)']

print("Number of Prioritized Issues: " + str(len(parsed)))

with open('test_report_parsed.json', 'w') as jp:
	json.dump(parsed, jp)
