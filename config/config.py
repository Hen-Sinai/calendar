from __future__ import print_function

import os.path
from typing import List

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from entities import User_creds, User_config_data

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_credentials() -> List[User_creds]:
    user_credentials = [
        User_config_data('Hen', 'credentials/hen_credentials.json', 'tokens/hen_token.json'),
        User_config_data('Limor', 'credentials/limor_credentials.json', 'tokens/limor_token.json')
    ]

    creds_list = []
    for user_info in user_credentials:
        token_file = os.path.join(os.path.dirname(__file__), user_info.token_file)
        credentials_file = os.path.join(os.path.dirname(__file__), user_info.credentials_file)

        creds = None
        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)

            with open(token_file, 'w') as token:
                token.write(creds.to_json())
                
        creds_list.append(User_creds(user_info.name, creds))
        
    return creds_list