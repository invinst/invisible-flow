import datetime

import pytest

from invisible_flow.copa.data_allegation_category import DataAllegationCategory


class TestDataAllegationCategory:

    def get_data_allegation_category(self):
        return DataAllegationCategory(
            id=1,
            category='category',
            category_code='category_code',
            allegation_name='allegation_name',
            on_duty=True,
            citizen_dept='citizen_dept',
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()

        )

    def test_create_data_allegation_category(self):
        try:
            self.get_data_allegation_category()
        except Exception:
            pytest.fail('this should not have thrown an exception')
