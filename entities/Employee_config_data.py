from dataclasses import dataclass
from datetime import date, datetime, timedelta

@dataclass
class User_config_data:
    _name: str
    _credentials_file: str
    _token_file: str
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def credentials_file(self) -> str:
        return self._credentials_file
    
    @property
    def token_file(self) -> str:
        return self._token_file