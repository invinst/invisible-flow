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
    cr_id: str

    def __iter__(self):
        return iter([
            self.add1,
            self.add2,
            self.beat_id,
            self.city,
            self.incident_date,
            self.is_officer_complaint,
            self.location,
            self.summary,
            self.cr_id
        ])

    def to_array(self):
        return [
            self.add1,
            self.add2,
            self.beat_id,
            self.city,
            self.incident_date,
            self.is_officer_complaint,
            self.location,
            self.summary,
            self.cr_id
        ]
