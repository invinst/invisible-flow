from invisible_flow.transformers.transformer_base import TransformerBase
from invisible_flow.entities.data_investigator import Investigator
import pandas as pd
from io import StringIO


class InvestigatorTransformer(TransformerBase):
    def row_to_investigator(df):
        return Investigator(last_name=df['INVST_LAST_NAME'],
                            first_name=df['INVST_FIRST_NAME'],
                            middle_initial=df['MIDDLE_INITIAL'],
                            gender=df['SEX'],
                            race=df['RACE'],
                            appointed_date=df['APPOINTED_DATE'],
                            officer_id=0)

    def transform_investigator_csv_to_entity_list(csv_content):
        csv_content_IO = StringIO(csv_content)
        df = pd.read_csv(csv_content_IO)
        df = df.replace(pd.np.nan, '', regex=True)
        return [InvestigatorTransformer.row_to_investigator(row) for _, row in df.iterrows()]

    def transform(self, response_type, file_content: str):
        return InvestigatorTransformer.transform_investigator_csv_to_entity_list(csv_content=file_content)
