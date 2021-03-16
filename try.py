from jira import JIRA
import click
import getpass

ISSUE_SUMMARY = "TEST SUMMARY from kittoh"
ISSUE_DESCRIPTION = """TEST
1.
2.
3.
"""


@click.command(
    short_help='Open a JIRA ticket with your report findings.'
)
# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
@click.option(
    '--project',
    required=True,
    help="The 3-4 character JIRA Project key."
)
# @click.option(
#     '--auth-file',
#     required=True,
#     type=click.Path(exists=True),
#     help='Path to the account authorization details JSON file.'
# )
# @click.option(
#     '--report-file',
#     required=True,
#     type=click.Path(exists=True),
#     help='Path to the HTML Report file.'
# )
# @click.option(
#     '--triage-file',
#     required=True,
#     help='Path to the Cloudsplaining Triage worksheet.'
# )
# @click.option(
#     '--data-file',
#     required=True,
#     type=click.Path(exists=True),
#     help='Path to the JSON Data file.'
# )
@click.option(
    '--server',
    # default="https://jira.atlassian.com",
    required=True,
    type=str,
    help='The JIRA server.'
)
@click.option(
    '--attachment',
    help='File path of the attachment.'
)

def open_jira_ticket(project, server, attachment):
    # def open_jira_ticket(project, auth_file, report_file, triage_file, data_file, server):
    jira = jira_login(server)
    issue = jira.create_issue(
        project=project,
        summary=ISSUE_SUMMARY,
        description=ISSUE_DESCRIPTION,
        issuetype={
            'name': 'Bug'
        }
    )
    # for file in [auth_file, report_file, triage_file, data_file]:
    add_attachment(jira, issue, attachment)

    print("Issue opened and attachments added. Metadata:")
    print(f"\tIssue ID: {issue.id}")
    print(f"\tIssue Key: {issue.key}")
    print("Attachments")
    list_attachments(issue)


def jira_login(server):
    # username = input("Enter your JIRA username")
    # password = getpass.getpass(prompt='Enter your JIRA password.')
    import os
    username = os.getenv("JIRA_EMAIL")
    api_key = os.getenv("JIRA_API_KEY")
    options = {
        "server": server,
    }
    # Supporting HTTP BASIC Auth right now.
    # You can extend this script to support Cookie-based, OAuth or Kerberos."""
    # Docs: https://jira.readthedocs.io/en/master/examples.html#authentication
    auth_jira = JIRA(
        options=options,
        basic_auth=(
            username,
            api_key
        )
    )
    return auth_jira

def add_attachment(jira, issue, attachment):
    """
    Adds an attachment.
    :param jira: JIRA session
    :param issue: Issue object
    :param attachment_path: Path to the file you want to attach
    :return:
    """
    # upload file from `/some/path/attachment.txt`
    jira.add_attachment(issue=issue, attachment='./test_report_parsed.json')

    # read and upload a file (note binary mode for opening, it's important):
    with open('test_report_parsed.json', 'rb') as f:
        jira.add_attachment(issue=issue, attachment=f)
        print(f"Uploaded: {attachment}")


def list_attachments(issue):
    for attachment in issue.fields.attachment:
        print("Name: '{filename}', size: {size}".format(
            filename=attachment.filename, size=attachment.size))
        # to read content use `get` method:
        print("Content: '{}'".format(attachment.get()))


if __name__ == '__main__':
    open_jira_ticket()
