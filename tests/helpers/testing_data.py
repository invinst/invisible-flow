import pandas as pd

transformed_data = pd.DataFrame(
        {
            'crid': ["1008899", "1087378", "1087387", "1087308", "1008913"],
        }
    )


transformed_data_with_rows = pd.DataFrame(
        {
            'crid': ["1008899", "1087378", "1087387", "1087308", "1008913"],
            'number_of_officer_rows': [1, 1, 2, 1, 1]
        }
    )


transformed_data_no_officer = pd.DataFrame(
        {
            'crid': ["1008899"],
            'number_of_officer_rows': [1]
        }
    )

transformed_data_with_beat_id = pd.DataFrame(
        {
            'crid': ["1008899", "1087378", "1087387", "1087308", "1008913"],
            'number_of_officer_rows': [1, 1, 2, 1, 1],
            'beat_id': ['0111', '0111', '0111', '0111', '0111']
        }
)

expected_transformed_data_with_beat_id = pd.DataFrame(
        {
            'crid': ["1008899", "1087378", "1087387", "1087308", "1008913"],
            'number_of_officer_rows': [1, 1, 2, 1, 1],
            'beat_id': [433, 111, 111, 0, 0]
        }
)
