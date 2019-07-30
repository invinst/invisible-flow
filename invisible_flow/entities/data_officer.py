from attr import dataclass


@dataclass
class Officer:
    birth_year: str
    first_name: str
    gender: str
    last_name: str
    middle_initial: str
    race: str
    rank: str
    cr_id: str