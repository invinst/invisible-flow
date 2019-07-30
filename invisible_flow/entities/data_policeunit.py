from attr import dataclass


@dataclass
class PoliceUnit:
    tags: str
    unit_name: str
    cr_id: str