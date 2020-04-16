from attr import dataclass


@dataclass
class PoliceUnit:
    tags: str
    unit_name: str
    crid: str
