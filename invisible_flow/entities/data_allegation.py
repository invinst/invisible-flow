from attr import dataclass


@dataclass
class Allegation:
    add1: str
    add2: str
    beat_id: str
    city: str
    incident_date: str
    is_officer_complaint: bool
    location: str
    summary: str

