import pandas as pd
from invisible_flow.copa.data_allegation_category import AllegationCategory


class Augment:
    def get_augmented_copa_data(self, allegation_rows: str):
        df = pd.read_csv(allegation_rows)

        categories = df.loc[:, 'current_category'].unique()

        category_code_map = pd.DataFrame(
            AllegationCategory.query.with_entities(AllegationCategory.category, AllegationCategory.category_code)
        )

        if len(category_code_map) > 0:
            for category in categories:
                # civil_suits_code is the category_code from data_allegationcategories
                # table that corresponds to the current category in this loop
                civil_suits_code = \
                    category_code_map.loc[category_code_map['category'] == category]['category_code'].values[0]
                df = df.replace(category, civil_suits_code)

        return df
