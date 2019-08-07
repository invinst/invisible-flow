from typing import List, Tuple

from invisible_flow.entities.data_allegation import Allegation
import pandas as pd
from io import StringIO

from invisible_flow.transformers.transformer_base import TransformerBase


class CaseInfoAllegationsTransformer(TransformerBase):
    @staticmethod
    def row_to_allegation(df):
        return Allegation(
            add1=str(df['STREET_NO']),
            add2=str(df['STREET_NME']),
            beat_id=str(df['OCCURANCE_BEAT']),
            city=f"{df['CITY']} {df['STATE']} {df['ZIP_CD']}",
            incident_date=str(df['COMPLAINT_DATE']),
            is_officer_complaint=str(df['COMPLAINANT_TYPE']) == 'CPD_EMPLOYEE',
            location=str(df['LOCATION_CODE']),
            summary="",
            cr_id=str(df['LOG_NO'])
        )

    @staticmethod
    def transform_case_info_csv_to_allegation(csv_content: str) -> List[Allegation]:
        string_io_csv = StringIO(csv_content)
        df = pd.read_csv(string_io_csv)
        return [CaseInfoAllegationsTransformer.row_to_allegation(row) for _, row in df.iterrows()]

    @staticmethod
    def transform_allegations_to_database_ready_df(allegations: List[Allegation]) -> pd.DataFrame:
        column_names = [
            'add1',
            'add2',
            'beat_id',
            'city',
            'incident_date',
            'is_officer_complaint',
            'location',
            'summary',
            'cr_id'
        ]

        return pd.DataFrame([allegation.to_array() for allegation in allegations], columns=column_names)

    @staticmethod
    def case_info_csv_to_allegation_csv(csv_content: str) -> str:
        allegations = CaseInfoAllegationsTransformer.transform_case_info_csv_to_allegation(csv_content)
        df = CaseInfoAllegationsTransformer.transform_allegations_to_database_ready_df(allegations)
        # todo handle empty data df transform, results in list of columns returned
        return df.to_csv(index=False)

    def transform(self, response_type: str, file_content: str) -> List[Tuple[str, str]]:
        # todo look at filename and figure out extension type and choose
        # todo if csv convert from binary to plain text
        return [("allegations", CaseInfoAllegationsTransformer.case_info_csv_to_allegation_csv(file_content))]
