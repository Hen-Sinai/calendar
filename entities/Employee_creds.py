from dataclasses import dataclass

from google.oauth2.credentials import Credentials

@dataclass
class Employee_creds:
    _name: str
    _creds: Credentials
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def creds(self) -> Credentials:
        return self._creds