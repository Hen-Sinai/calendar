from dataclasses import dataclass

from google.oauth2.credentials import Credentials

@dataclass
class Employee_config_data:
    _name: str
    _credentials_file: str
    _token_file: str
    _creds: Credentials = None
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def credentials_file(self) -> str:
        return self._credentials_file
    
    @property
    def token_file(self) -> str:
        return self._token_file
    
    @property
    def creds(self) -> Credentials:
        return self._creds
    
    @creds.setter
    def creds(self, new_creds: Credentials):
        self._creds = new_creds
