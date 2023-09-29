from dataclasses import dataclass
from datetime import date, datetime, timedelta

@dataclass
class Appointment:
    _summary: str
    _location: str
    _description: str
    _start_time: date
    _end_time: date
    _color: int = 1
    
    @property
    def summary(self) -> str:
        return self._summary
    
    @property
    def location(self) -> str:
        return self._location
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def start_time(self) -> date:
        return self._start_time

    @property
    def end_time(self) -> date:
        return self._end_time
    
    def calculate_end_time(self, length: int) -> date:
        start_time = datetime.strptime(self._start_time, '%H:%M')
        end_datetime = start_time + timedelta(minutes=length)
        return end_datetime.date()