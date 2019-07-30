from attr import dataclass


@dataclass
class AllegationCategory:
    category: str
    category_code: str
    on_duty: str
    cr_id: str