import datetime

from invisible_flow.copa.converter import convert_sql_alchemy_obj_to_dict
from invisible_flow.copa.data_allegation import DataAllegation


class TestConverter:
    def get_data_allegation(self):
        return DataAllegation(
            cr_id='cr_id',
            summary='summary',
            add1='add1',
            add2='add2',
            beat_id=1,
            city='city',
            incident_date=datetime.datetime.utcnow(),
            is_officer_complaint=True,
            location='location',
            old_complaint_address='old_complaint_address',
            subjects={"Bassil Abdelal", "Richie Cole", "Omar Young", "Leevon Carter"},
            point='0101000020E61000009FB3603DC9EA55C0138E6A227DD84440',
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )

    def test_convert_data_allegation_to_dict(self):
        allegation = self.get_data_allegation()

        expected_dict_like = {
            'cr_id': 'cr_id',
            'summary': 'summary',
            'add1': 'add1',
            'add2': 'add2',
            'beat_id': 1,
            'city': 'city',
            'incident_date': allegation.incident_date,
            'is_officer_complaint': True,
            'location': 'location',
            'old_complaint_address': 'old_complaint_address',
            'subjects': {"Bassil Abdelal", "Richie Cole", "Omar Young", "Leevon Carter"},
            'point': '0101000020E61000009FB3603DC9EA55C0138E6A227DD84440',
            'created_at': allegation.created_at,
            'updated_at': allegation.updated_at
        }

        assert convert_sql_alchemy_obj_to_dict(allegation) == expected_dict_like
