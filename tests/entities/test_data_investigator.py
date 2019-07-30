from invisible_flow.entities.data_investigator import Investigator


class TestInvestigator:
    def test_values_are_unmodified(self):
        investigator = Investigator(last_name='lastname',
                                    first_name='first name',
                                    middle_initial='middle',
                                    gender='M',
                                    race="BLACK",
                                    appointed_date='',
                                    officer_id=232)

        assert investigator.last_name == 'lastname'
        assert investigator.first_name == 'first name'
        assert investigator.middle_initial == 'middle'
        assert investigator.gender == 'M'
        assert investigator.race == "BLACK"
        assert investigator.appointed_date == ''
        assert investigator.officer_id == 232
