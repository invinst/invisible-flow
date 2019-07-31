from typing import List, Tuple

import pandas as pd
from io import StringIO

from invisible_flow.entities.data_allegationcategory import AllegationCategory
from invisible_flow.entities.data_officer import Officer
from invisible_flow.entities.data_officerbadgenumber import OfficerBadgeNumber
from invisible_flow.entities.data_policeunit import PoliceUnit

from invisible_flow.transformers.transformer_base import TransformerBase


class AccusedTransformer(TransformerBase):

    def csv_to_entity_name_entity_list_tuples(self, csv_content) -> List[Tuple]:
        # what if we push each entity into a collection for use later
        # loop across rows of csv_content
        # 4 collections one for each entity
        # return a list of tuples [(name, [entity, entity]), (name, [entity, entity])]
        string_io_csv = StringIO(csv_content)
        accused_df = pd.read_csv(string_io_csv)
        # doing it this way leads to each entity having all the data for each column in a single
        # entity property, so category has all the rows ALLEGATION_CATEGORY entries in a single
        # entity instance, I'm not so sure this will plug into the db correctly
        return [
            (
                "allegationcategory",
                AllegationCategory(
                    category=str(accused_df['ALLEGATION_CATEGORY']),
                    category_code=str(accused_df['ALLEGATION_CATEGORY_CD']),
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

    def csv_to_entity_name_csv_tuples(self, csv_content) -> List[Tuple]:
        string_io_csv = StringIO(csv_content)
        accused_df = pd.read_csv(string_io_csv)
        allegationcategory_columns = [
            'ALLEGATION_CATEGORY',
            'ALLEGATION_CATEGORY_CD',
            'LOG_NO'
        ]
        officer_columns = [
            'BIRTH_YEAR',
            'OFFICER_FIRST_NAME',
            'SEX_CODE_CD',
            'OFFICER_LAST_NAME',
            'MIDDLE_INITIAL',
            'RACE_CODE_CD',
            'EMPLOYEE_POSITION',
            'LOG_NO'
        ]
        officerbadgenumber_columns = [
            'EMPLOYEE_NO',
            'STAR_NO',
            'LOG_NO'
        ]
        policeunit_columns = [
            'EMPLOYEE_DETAIL_UNIT',
            'EMPLOYEE_ASSIGN_UNIT',
            'LOG_NO'
        ]
        return [
            (
                'allegationcategory',
                accused_df.loc[:, allegationcategory_columns].rename(columns={
                    'ALLEGATION_CATEGORY': 'category',
                    'ALLEGATION_CATEGORY_CD': 'category_code',
                    'LOG_NO': 'cr_id'
                }).to_csv(index=False)
            ), (
                'officer',
                accused_df.loc[:, officer_columns].rename(columns={
                    'BIRTH_YEAR': 'birth_year',
                    'OFFICER_FIRST_NAME': 'first_name',
                    'SEX_CODE_CD': 'gender',
                    'OFFICER_LAST_NAME': 'last_name',
                    'MIDDLE_INITIAL': 'middle_initial',
                    'RACE_CODE_CD': 'race',
                    'EMPLOYEE_POSITION': 'rank',
                    'LOG_NO': 'cr_id'
                }).to_csv(index=False)
            ), (
                'officerbadgenumber',
                accused_df.loc[:, officerbadgenumber_columns].rename(columns={
                    'EMPLOYEE_NO': 'officer_id',
                    'STAR_NO': 'star',
                    'LOG_NO': 'cr_id'
                }).to_csv(index=False)
            ), (
                'policeunit',
                accused_df.loc[:, policeunit_columns].rename(columns={
                    'EMPLOYEE_DETAIL_UNIT': 'tags',
                    'EMPLOYEE_ASSIGN_UNIT': 'unit_name',
                    'LOG_NO': 'cr_id'
                }).to_csv(index=False)
            )
        ]

    def transform(self, one, two):
        pass
