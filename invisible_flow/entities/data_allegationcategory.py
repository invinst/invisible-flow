from attr import dataclass


@dataclass
class AllegationCategory:
    category: str
    category_code: str
    on_duty: bool
    cr_id: str