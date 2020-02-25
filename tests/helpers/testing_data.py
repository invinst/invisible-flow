import pandas as pd

transformed_data = pd.DataFrame(
        {
            'cr_id': ["1008899", "1087378", "1087387", "1087308", "1008913"],
        }
    )


transformed_data_with_rows = pd.DataFrame(
        {
            'cr_id': ["1008899", "1087378", "1087387", "1087308", "1008913"],
            'number_of_officer_rows': [0, 0, 3, 2, 0]
        }
    )
