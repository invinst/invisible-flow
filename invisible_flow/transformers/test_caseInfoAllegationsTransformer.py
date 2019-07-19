from unittest import TestCase

from invisible_flow.entities.data_allegation import Allegation
from invisible_flow.transformers.case_info_allegations_transformer import CaseInfoAllegationsTransformer

first_row = '1053951,05-MAY-12,06-MAY-12,11-MAY-12,13-JUN-12,"ADMINISTRATIVELY CLOSED","COMMERCIAL / BUSINESS OFFICE",1100,"West","63RD ST","","CHICAGO","ILLINOIS","60621","712","05A","EXCESSIVE FORCE / ON DUTY - INJURY","GROUP 05 - OFFICE OF PROFESSIONAL STANDARDS INVESTIGATIONS","No","CIVILIAN","IPRA"'


class TestCaseInfoAllegationsTransformer():
    def test_transform_case_info_csv_to_allegation(self):
        with open('head_case_info.csv') as file:
            actual_allegations = CaseInfoAllegationsTransformer.transform_case_info_csv_to_allegation(file.read())
            allegation_to_test = actual_allegations[0]
            expected_allegation = Allegation(
                add1="1100",
                add2="63RD ST",
                beat_id="712",
                city="CHICAGO ILLINOIS 60621",
                incident_date="11-MAY-12",
                is_officer_complaint=False,
                location="COMMERCIAL / BUSINESS OFFICE",
                summary=""
            )
            assert allegation_to_test == expected_allegation
            assert len(actual_allegations) == 9

    def test_transform_allegations_to_database_ready_df(self):
        a = Allegation(
            add1="asdf",
            add2="asdf",
            beat_id="asdf",
            city="asdf",
            incident_date="asdf",
            is_officer_complaint=True,
            location="",
            summary=''
        )
        df = CaseInfoAllegationsTransformer.transform_allegations_to_database_ready_df([a])
        print(df)
