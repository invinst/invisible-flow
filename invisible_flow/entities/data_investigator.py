from attr import dataclass


@dataclass
class Investigator:
    last_name: str
    first_name: str
    middle_initial: str
    gender: str
    race: str
    appointed_date: str
    officer_id: int
