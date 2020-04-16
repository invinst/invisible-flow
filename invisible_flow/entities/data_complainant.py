from attr import dataclass


@dataclass
class Complainant:
    gender: str
    race: str
    age: int
    crid: str
