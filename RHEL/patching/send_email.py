# Core imports
import os
import sys

# 3rd-party imports
import sendgrid  # pip install sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv  # pip install python-dotenv

# Local app imports
# none at this time


# Notes
# From: https://docs.sendgrid.com/for-developers/sending-email/quickstart-python
# Response codes: https://docs.sendgrid.com/api-reference/how-to-use-the-sendgrid-v3-api/responses#status-codes


# Get the file path from the passed arg
# Note this is a bad plan lol. Do some input validation here.
# This sets the email body (the 'content' var) to the text in the dnf history info file
if len(sys.argv) > 1:
    file_path = str(sys.argv[1])
    file = open(file_path, 'r')
    file_contents = file.read()
    content = Content("text/plain", file_contents)
    file.close()
else:
    # No file path arg (or any arg) was passed
    content = Content("text/plain", "Patching completed on RHEL9-Srv01.")



# Load the .env file
load_dotenv()


# Initial variables
sg_api_key = os.getenv('SENDGRID_API_KEY')


# Build the mail object parameters
sg = sendgrid.SendGridAPIClient(api_key=sg_api_key)
from_email = Email("alerts@gridnorth.tech")
to_email = To("brian@gridnorth.tech")
subject = "ALERT: Patching complete on RHEL9-Srv01"
mail = Mail(from_email, to_email, subject, content)


# get a JSON-ready representation of the mail object
mail_json = mail.get()


# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)  # Code 202 = success (see response code link above)
print(response.headers)


