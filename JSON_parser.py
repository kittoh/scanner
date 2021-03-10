#! /usr/bin/env python

import json
import pprint

with open('test_report.json', ) as j:
	data = json.load(j)

site = data['site']
alerts = site[0]['alerts']

print("Total Number of Issues: " + str(len(alerts)))

parsed = [riskdesc for riskdesc in alerts if riskdesc['riskdesc'] == 'Medium (Medium)' or riskdesc['riskdesc'] == 'High (High)']

print("Number of Prioritized Issues: " + str(len(parsed)))

with open('test_report_parsed.json', 'w') as jp:
	json.dump(parsed, jp)


# pp.pprint(parsed_json)

# for alert in alerts:
# 	name = alert['name']
# 	riskdesc = alert['riskdesc']
# 	alert_info[name] = riskdesc
# 	# print(json.dumps(alert_info, indent=2))
# 	pp = pprint.PrettyPrinter(indent=2)
# 	pp.pprint(alert_info)



# for issues in alert_info:
# 	name = alerts[0]['name']
# 	riskdesc = alerts[0]['riskdesc']
# 	risk_level[name] = riskdesc	
# 	print(risk_level)
# 	print(issues)
# print(type(alerts))
