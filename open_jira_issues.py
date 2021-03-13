from jira import JIRA
import json
import requests
from requests.auth import HTTPBasicAuth
import getpass

ISSUE_SUMMARY = "SAMPLE SUMMARY"
ISSUE_DESCRIPTION = "SAMPLE DESCRIPTION"

# your jira domain
server = "https://kittoh.atlassian.net/rest/api/3/issue"

# headers
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

email = "kitto.hernandes@gmail.com"
api_key = input("API key: ")

# auth = HTTPBasicAuth("kitto.hernandes@gmail.com", "bSmfRUKJXt2wkd6S5VgaCB66")

# open parsed report
with open('test_report_parsed.json') as j:
    report = json.load(j)

def jira_login(server):
    email = "kitto.hernandes@gmail.com"        # input("JIRA email: ")
    password = getpass.getpass(prompt="JIRA password:")
    api_key = input("API key: ")
    options = {
    "server": server
    }

    auth_jira = HTTPBasicAuth(
        email,
        api_key
    )
  
    return auth_jira

# jira_login(server)

response = requests.request(
    "POST",
    url = server,
    headers = headers,
    data = report,
    auth = (
        email,
        api_key
    )
)

print(response.text)

# print(report(response.text), sort_keys=True, indent=4, separators=(",", ": "))

# # jira = JIRA(options, basic_auth = (user, api_key))


# ticket = " "
# issue = jira.issue(ticket)

# summary = issue.fields.summary

# print('ticket: ', ticket, summary)

