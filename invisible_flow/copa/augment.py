import pandas as pd


class Augment:
    def get_transform_copa_data(self, allegation_rows: str):
        print(pd.read_csv(allegation_rows))
