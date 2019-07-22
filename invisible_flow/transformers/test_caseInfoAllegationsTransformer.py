import pandas as pd

from invisible_flow.entities.data_allegation import Allegation
from invisible_flow.transformers.case_info_allegations_transformer import CaseInfoAllegationsTransformer


class TestCaseInfoAllegationsTransformer():
    def test_transform_case_info_csv_to_allegation(self):
        with open('head_case_info.csv') as file:
            actual_allegations = CaseInfoAllegationsTransformer.transform_case_info_csv_to_allegation(file.read())
            allegation_to_test = actual_allegations[0]
            expected_allegation = Allegation(
                add1='1100',
                add2='63RD ST',
                beat_id='712',
                city='CHICAGO ILLINOIS 60621',
                incident_date='11-MAY-12',
                is_officer_complaint=False,
                location='COMMERCIAL / BUSINESS OFFICE',
                summary=''
            )
            assert allegation_to_test == expected_allegation
            assert len(actual_allegations) == 9

    def test_transform_allegations_to_database_ready_df(self):
        a = Allegation(
            add1='add1',
            add2='add2',
            beat_id='beat_id',
            city='city',
            incident_date='incident_date',
            is_officer_complaint=True,
            location='location',
            summary='summary'
        )
        allegations = [a, a]
        df = CaseInfoAllegationsTransformer.transform_allegations_to_database_ready_df(allegations)
        source_arrays = [[
            'add1',
            'add2',
            'beat_id',
            'city',
            'incident_date',
            True,
            'location',
            'summary'
        ], [
            'add1',
            'add2',
            'beat_id',
            'city',
            'incident_date',
            True,
            'location',
            'summary'
        ]]
        column_names = [
            'add1',
            'add2',
            'beat_id',
            'city',
            'incident_date',
            'is_officer_complaint',
            'location',
            'summary'
        ]
        expected_df = pd.DataFrame(source_arrays, columns=column_names)
        assert expected_df.equals(df)

    def test_case_info_csv_to_allegation_csv(self):
        with open('single_row_case_info.csv') as input_file,\
                open('single_row_case_info_allegation.csv') as expected_output_file:
            initial_case_info_content = input_file.read()
            actual_output = CaseInfoAllegationsTransformer.case_info_csv_to_allegation_csv(initial_case_info_content)
            expected_output = expected_output_file.read()
            assert actual_output == expected_output

