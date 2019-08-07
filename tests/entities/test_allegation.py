from invisible_flow.entities.data_allegation import Allegation


class TestAllegation:
    def test_allegation_to_array(self):
        allegation = Allegation(
            add1='add1',
            add2='add2',
            beat_id='beat',
            city='city',
            incident_date='incident_date',
            is_officer_complaint=True,
            location='',
            summary='',
            cr_id='1053951'
        )
        allegation_array = allegation.to_array()
        expected_array = [
            'add1',
            'add2',
            'beat',
            'city',
            'incident_date',
            True,
            '',
            '',
            '1053951'
        ]
        assert expected_array == allegation_array
