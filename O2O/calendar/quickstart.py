
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client, file
from oauth2client import tools
from oauth2client.file import Storage

from dateutil import parser            
from datetime import datetime 

import datetime

try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def create_event(data, u_name):

    credentials = get_credentials(u_name)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    event = {
      'summary': data['summary'],
      'location': data['location'],
      'description': data['description'],
      'start': {
        'dateTime': data['start'],
        'timeZone': 'Asia/Seoul',
      },
      'end': {
        'dateTime': data['end'],
        'timeZone': 'Asia/Seoul',
      },
      'recurrence': [
        #'RRULE:FREQ=DAILY;COUNT=2'
      ],
      'attendees': [
        #{'email': 'lpage@example.com'},
        #{'email': 'sbrin@example.com'},
      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          #{'method': 'email', 'minutes': 24 * 60},
          #{'method': 'popup', 'minutes': 10},
        ],
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print ('Event created: %s' % (event.get('htmlLink')))  
    return(event.get('htmlLink'))

def date_trans(s):
    return parser.parse(s).strftime('%Y-%m-%d')

def get_credentials(user):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials/POSTECH')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, str(user)+'.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    '''
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    '''
    '''
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    
    print('Getting the upcoming 10 events')
    
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
    event = {
      'summary': 'Example I/O 2017',
      'location': 'My home',
      'description': 'A chance to hear more about Google\'s developer products.',
      'start': {
        'dateTime': '2017-11-25T09:00:00',
        'timeZone': 'Asia/Seoul',
      },
      'end': {
        'dateTime': '2017-11-25T17:00:00',
        'timeZone': 'Asia/Seoul',
      },
      'recurrence': [
        #'RRULE:FREQ=DAILY;COUNT=2'
      ],
      'attendees': [
        #{'email': 'lpage@example.com'},
        #{'email': 'sbrin@example.com'},
      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          #{'method': 'email', 'minutes': 24 * 60},
          #{'method': 'popup', 'minutes': 10},
        ],
      },
    }


    '''
    

    create_event(data)



if __name__ == '__main__':
    main()
