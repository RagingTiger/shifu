import os
import sys
import threading
import gmail

def assessment_form_response(request):
    # setup initial vars
    html_format = ("<!DOCTYPE html><html><head><style></style></head><body>"
                   "<p>{}</p></body></html>")
    query =  request.args
    headers = request.headers
    user_ip = request.remote_addr
    fstr = '{}: {}<br><br>'
    assessment = ''

    # get request arg key/val
    for key, value in query.items():
      assessment += fstr.format(key.capitalize(), value)

    # get user ip key/val
    assessment += fstr.format('User-IP', user_ip)

    # get headers key/val
    for key, value in headers.items():
      assessment += (fstr.format(key, value))

    # get info for email subject
    subject = query['name'].replace(' ', '+') + ' | ' + \
              query['email'] + ' | ' + \
              query['gender'].replace(' ', '+') + ' | ' + \
              query['ethnicity'].replace(' ', '+') + ' | ' + user_ip

    # format into html
    html_response = html_format.format(assessment)

    # send email
    try:
        # get env vars
        gmail_creds = {'account': os.environ['GMAIL_ACCOUNT'],
                       'psswd': os.environ['GMAIL_APP_PSSWD']}

        # start gmail SMTP session
        gm = gmail.Gmail(gmail_creds['account'], gmail_creds['psswd'])

        # prepare email message
        message = {'subject': subject, 'body': html_response}

        # send mesage asynchronously
        backend = threading.Thread(target=gm.send_message,
                                   args=(message['subject'], message['body']))
        backend.start()

    except KeyError:
        sys.exit('ENV variables unset for GMAIL account')
