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

    def transform_invesitgator_entities_to_df(entities):
        column_names = [prop.name for prop in getattr(
            Investigator, "__attrs_attrs__", None)]
        get_property_values = lambda invest_entity, column_list: [getattr(invest_entity,prop) for prop in column_list]
        investigator_entity_values = list(map(lambda obj:get_property_values(obj, column_names), entities))
        df = pd.DataFrame(investigator_entity_values, columns= column_names)
        return df

    def transform_investigator_csv_to_investigator_csv(csv_content):
         investigator_entity_list = InvestigatorTransformer.transform_investigator_csv_to_entity_list(csv_content)
         df = InvestigatorTransformer.transform_invesitgator_entities_to_df(investigator_entity_list)
         return df.to_csv(index=False)


    def transform(self, response_type, file_content: str):
        return InvestigatorTransformer.transform_investigator_csv_to_entity_list(csv_content=file_content)
