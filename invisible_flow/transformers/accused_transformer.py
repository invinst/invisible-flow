from typing import List, Tuple

import pandas as pd
from io import StringIO

from invisible_flow.entities.data_allegationcategory import AllegationCategory
from invisible_flow.entities.data_officer import Officer
from invisible_flow.entities.data_officerbadgenumber import OfficerBadgeNumber
from invisible_flow.entities.data_policeunit import PoliceUnit

from invisible_flow.transformers.transformer_base import TransformerBase


class AccusedTransformer(TransformerBase):
    # TODO We need a method that returns a collection of name/entity tuples

    def csv_to_entity_name_entity_list_tuples(self, accused_df) -> List[Tuple]:
        # what if we push each entity into a collection for use later
        # loop across rows of csv_content
        # 4 collections one for each entity
        # return a list of tuples [(name, [entity, entity]), (name, [entity, entity])]
        return [
            (
                "allegationcategory",
                AllegationCategory(
                    category=str(accused_df['ALLEGATION_CATEGORY']),
                    category_code=str(accused_df['ALLEGATION_CATEGORY_CD']),
                    on_duty=str(accused_df['EMPLOYEE_ON_DUTY']) == 'Yes',
                    cr_id=str(accused_df['LOG_NO'])
                )
            ),
            (
                "officer",
                Officer(
                    birth_year=str(accused_df['BIRTH_YEAR']),
                    first_name=str(accused_df['OFFICER_FIRST_NAME']),
                    gender=str(accused_df['SEX_CODE_CD']),
                    last_name=str(accused_df['OFFICER_LAST_NAME']),
                    middle_initial=str(accused_df['MIDDLE_INITIAL']),
                    race=str(accused_df['RACE_CODE_CD']),
                    rank=str(accused_df['EMPLOYEE_POSITION']),
                    cr_id=str(accused_df['LOG_NO'])
                )
            ),
            (
                "officerbadgenumber",
                OfficerBadgeNumber(
                    officer_id=str(accused_df['EMPLOYEE_NO']),
                    star=str(accused_df['STAR_NO']),
                    cr_id=str(accused_df['LOG_NO'])
                )
            ),
            (
                "policeunit",
                PoliceUnit(
                    tags=str(accused_df['EMPLOYEE_DETAIL_UNIT']),
                    unit_name=str(accused_df['EMPLOYEE_ASSIGN_UNIT']),
                    cr_id=str(accused_df['LOG_NO'])
                )
            )
        ]

    def transform_csv_to_accused_entities(self, csv_content: str) -> List:
        string_io_csv = StringIO(csv_content)
        df = pd.read_csv(string_io_csv)
        return [AccusedTransformer.csv_to_entity_name_entity_list_tuples(self, row) for _, row in df.iterrows()]

    def transform(self, one, two):
        pass
