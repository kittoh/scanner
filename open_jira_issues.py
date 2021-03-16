from jira import JIRA
import json
import requests
from requests.auth import HTTPBasicAuth
import getpass
import click

ISSUE_SUMMARY = "SAMPLE SUMMARY"
ISSUE_DESCRIPTION = "SAMPLE DESCRIPTION"

@click.command(
    short_help = 'This is a short help.'
)

@click.option(
    '--project',
    required=True,
    help="The 3-4 character JIRA Project key."
)

@click.option(
    '--auth-file',
    required=True,
    type=click.Path(exists=True),
    help='Path to the account authorization details JSON file.'
)

@click.option(
    '--report-file',
    required=True,
    type=click.Path(exists=True),
    help='Path to the HTML Report file.'
)

@click.option(
    '--server',
    # default="https://jira.atlassian.com",
    required=True,
    type=str,
    help='The JIRA server.'
)

def jira_login(server):
    email = "kitto.hernandes@gmail.com"        # input("JIRA email: ")
    password = getpass.getpass(prompt = "JIRA password: ")
    # api_key = input("API key: ")
    options = {
    "server": server
    }

    auth_jira = JIRA(
        options=options,
        basic_auth=(
            username,
            api_key
        )
    )
    return auth_jira

    auth_jira = HTTPBasicAuth(
        email,
        api_key
    )
  
    return auth_jira







# your jira domain
server = "https://kittoh.atlassian.net/rest/api/3/issue"

# headers
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

email = "kitto.hernandes@gmail.com"
api_key = input("API key: ")

# auth = HTTPBasicAuth("kitto.hernandes@gmail.com", api_key)

# open parsed report
def add_attachment(jira, issue, attachment_path):
    """
    Adds an attachment.
    :param jira: JIRA session
    :param issue: Issue object
    :param attachment_path: Path to the file you want to attach
    :return:
    """
    # upload file from `/some/path/attachment.txt`
    jira.add_attachment(issue=issue, attachment=attachment_path)

    # read and upload a file (note binary mode for opening, it's important):
    with open(attachment_path, 'rb') as f:
        jira.add_attachment(issue=issue, attachment=f)
    print(f"Uploaded: {attachment_path}")

with open('test_report_parsed.json') as j:
    report = json.load(j)



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

