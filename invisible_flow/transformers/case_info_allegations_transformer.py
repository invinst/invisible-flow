from invisible_flow.entities.data_allegation import Allegation
import pandas as pd
from io import StringIO


class CaseInfoAllegationsTransformer:
    @staticmethod
    def row_to_allegation(df):
        return Allegation(
            add1=str(df['STREET_NO']),
            add2=str(df['STREET_NME']),
            beat_id=str(df['OCCURANCE_BEAT']),
            city="{} {} {}".format(df['CITY'], df['STATE'], df['ZIP_CD']),
            incident_date=str(df['COMPLAINT_DATE']),
            is_officer_complaint=str(df['COMPLAINANT_TYPE']) == 'CPD_EMPLOYEE',
            location=str(df['LOCATION_CODE']),
            summary=""
        )

    @staticmethod
    def transform_case_info_csv_to_allegation(csv_content: str) -> [Allegation]:
        string_io_csv = StringIO(csv_content)
        df = pd.read_csv(string_io_csv)
        return [CaseInfoAllegationsTransformer.row_to_allegation(row) for _, row in df.iterrows()]


