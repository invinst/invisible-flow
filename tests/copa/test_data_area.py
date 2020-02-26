import pytest
import datetime

from invisible_flow.copa.data_area import DataArea


class TestDataArea:

    def get_data_area(self):
        return DataArea(
            id=1,
            name='name',
            area_type='beat',
            polygon='0106000020E6',
            tags={'tag1', 'tag2'},
            median_income='median_income',
            alderman='alderman',
            commander_id=300,
            description='description',
            police_hq_id=1,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )

    def test_create_data_allegation(self):
        try:
            self.get_data_area()
        except Exception:
            pytest.fail('this should not have thrown an exception')

# Should test querying for data_area?
