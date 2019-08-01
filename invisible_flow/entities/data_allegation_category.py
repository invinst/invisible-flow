from attr import dataclass


@dataclass
class AllegationCategory:
    category: str
    category_code: str
    cr_id: str
