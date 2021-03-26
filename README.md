# SCANNER

__SCANNER__ (Tentative name 😅)

This is a basic multi-part security scanning pipeline.

_The FLOW_

GitHub Action(local) --> Docker - OWASP ZAP Scan --> Parser --> Jira

_The SEQUENCE_

1. ZAP Scan - Baseline
2. JSON Parser
3. Jira Issue Creator

_The Process_

1. Running OWASP ZAP Scan
   - ZAP Scan will be ran locally from a Docker Image to have full control of its parameters
   - These are the guide for running scans: https://www.zaproxy.org/docs/docker/about/
   - If you want to run it locally via Github Actions, you need to configure this: https://github.com/nektos/act
   
2. Parsing the Results
   - Parsing the json results from ZAP Scan using Python script - 2_json_parser.py

3. Creating Jira Issues
   - The parsed results will then be attached to a Jira Issue which is 
     opened by a Python script - 3_jira_issue_creator


