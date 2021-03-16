# upload file from `/some/path/attachment.txt`
jira.add_attachment(issue=issue, attachment='./test_report_parsed.json')

# read and upload a file (note binary mode for opening, it's important):
with open('test_report_parsed.json', 'rb') as f:
    jira.add_attachment(issue=issue, attachment=f)

# attach file from memory (you can skip IO operations). In this case you MUST provide `filename`.
from io import StringIO
attachment = StringIO()
attachment.write(attachment)
jira.add_attachment(issue=issue, attachment=attachment, filename='content.txt')