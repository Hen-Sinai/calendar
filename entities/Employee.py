from dataclasses import dataclass
from datetime import datetime, timedelta

from .Appointment import Appointment

@dataclass
class Employee:
    _name: str
    _mail: str
    _availability: dict = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def mail(self) -> str:
        return self._mail
    
    @property
    def availabilty(self) -> dict:
        return self._availability
    
    def __post_init__(self):
        if self._availability is None:
            self._availability = self.create_availability_slot()
    
    def create_availability_slot(self, start_date=None, end_date=None):
        availability = dict()
        
        if start_date is None:
            start_date = datetime.now().replace(second=0,microsecond=0) + timedelta(days=1)
        if end_date is None:
            end_date = datetime.now().replace(second=0,microsecond=0) + timedelta(days=2)
        
        current_date = start_date
        end_date = end_date.replace(hour=0, minute=0, second=0, microsecond=0)

        while current_date <= end_date:
            daily_availability = set()
            start_time = current_date.replace(hour=10, minute=0, second=0, microsecond=0)
            end_time = current_date.replace(hour=18, minute=0, second=0, microsecond=0)
            
            current_time = start_time
            while current_time < end_time:
                daily_availability.add(current_time.isoformat())
                current_time += timedelta(minutes=15)

            availability[current_date.date().isoformat()] = daily_availability
            current_date += timedelta(days=1)
            
        return availability
            
    def remove_availability_slot(self, appointment: Appointment):
        start_time = appointment.start_time
        end_time = appointment.end_time
        
        current_time = start_time
        while current_time < end_time:
            date_key = current_time.date()
            time_value = current_time.strftime('%H:%M')
            if date_key in self._availability and time_value in self._availability[date_key]:
                self._availability[date_key].remove(time_value)
            current_time += timedelta(minutes=15)
