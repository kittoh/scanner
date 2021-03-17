from jira import JIRA
import click

ISSUE_SUMMARY = "TEST SUMMARY from kittoh"
ISSUE_DESCRIPTION = """TEST
1.
2.
3.
"""

@click.command(
    short_help='Open a JIRA ticket with your report findings.'
)
@click.option(
    '--server',
    # default="https://jira.atlassian.com",
    required=True,
    type=str,
    help='The JIRA server.'
)
@click.option(
    '--project',
    required=True,
    help="The 3-4 character JIRA Project key."
)
# @click.option(
#     '--attachment',
#     help='File path of the attachment.'
# )

def open_jira_ticket(project, server):
    jira=jira_login(server)
    issue=jira.create_issue(
        project = project,
        summary = ISSUE_SUMMARY,
        description = ISSUE_DESCRIPTION,
        issuetype = {
            'name': 'Bug'
        }
    )

    # with open('report.txt', 'rb') as f:
    #     jira.add_attachment(issue=issue, attachment=f)
    #     f.close()
    attachment_item = open('test_report_parsed.json', 'rb')
    jira.add_attachment(issue=issue, attachment=attachment_item)

    print("Issue opened and attachments added. Metadata:")
    print(f"\tIssue ID: {issue.id}")
    print(f"\tIssue Key: {issue.key}")
    print("Attachments")

def jira_login(server):

    import os
    email = os.getenv("JIRA_EMAIL")
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
            email,
            api_key
        )
    )
    return auth_jira


if __name__ == '__main__':
    open_jira_ticket()