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
@click.option(
    '--attachment_path',
    help='File path of the attachment.'
)

def open_jira_ticket(project, server, attachment_path):
    jira=jira_login(server)
    issue=jira.create_issue(
        project = project,
        summary = ISSUE_SUMMARY,
        description = ISSUE_DESCRIPTION,
        issuetype = {
            'name': 'Bug'
        }
    )
    attachment_item = open(attachment_path, 'rb')
    jira.add_attachment(issue=issue, attachment=attachment_item)
    
    print("Issue opened and attachments added. Metadata:")
    print(f"\tIssue ID: {issue.id}")
    print(f"\tIssue Key: {issue.key}")
    print(f"Uploaded: {attachment_item}")

def jira_login(server):

    import os
    email = os.getenv("JIRA_EMAIL")
    api_key = os.getenv("JIRA_API_KEY")
    options = {
        "server": server,
    }
    
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
