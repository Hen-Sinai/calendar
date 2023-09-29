from __future__ import print_function

import datetime
from typing import List

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config.config import get_credentials
from entities import Appointment, Employee, Employee_creds

# def init_employees(employees_data) -> List[Employee]:
#     employees = []
    
#     for name in employees_name:
#         employees.append(Employee(name, ))
    

def get_calendar_events(employees_credentials: List[Employee_creds]):
    appointments = []
    try:
        for employee_cred in employees_credentials:
            service = build('calendar', 'v3', credentials=employee_cred.creds)

            time_min = datetime.datetime.utcnow().isoformat() + 'Z'
            max_datetime = (datetime.datetime.utcnow() + datetime.timedelta(days=90)).isoformat() + 'Z'

            events_result = service.events().list(calendarId='primary', 
                                                timeMin=time_min, timeMax=max_datetime,
                                                singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])

            # You can process and print the events for this user as needed
            for event in events:
                start = event['start'].get('dateTime')
                end = event['end'].get('dateTime')
                
                date = start.date()
                print(start, end)

    except HttpError as error:
        print('An error occurred for this user: %s' % error)

def main():
    creds = get_credentials()
    get_calendar_events(creds)
    
    # employee = Employee(
    #     _name='John Doe',
    #     _mail='john@example.com'
    # )
    # print(employee)

if __name__ == '__main__':
    main()
