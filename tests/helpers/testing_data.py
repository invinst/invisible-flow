import pandas as pd

transformed_data = pd.DataFrame(
    {
        'cr_id': ["1008899", "1087378", "1087387", "1087308", "1008913"],
        'officer_race': [['white'], ['african-american'], ['white', 'white'], ['asian'], ['asian']],
        'officer_gender': [['M'], ['M'], ['F', 'F'], ['M'], ['F']],
        'officer_age': [["40-49"], ["40-49"], ["40-49", "40-49"], ["40-49"], ["40-49"]]
    }
)

transformed_data_with_rows = pd.DataFrame(
    {
        'cr_id': ["1008899", "1087378", "1087387", "1087308", "1008913"],
        'number_of_officer_rows': [1, 1, 2, 1, 1],
        'officer_race': [['white'], ['african-american'], ['white', 'white'], ['asian'], ['asian']],
        'officer_gender': [['M'], ['M'], ['F', 'F'], ['M'], ['F']],
        'officer_age': [["40-49"], ["40-49"], ["40-49", "40-49"], ["40-49"], ["40-49"]]
    }
)

transformed_data_no_officer = pd.DataFrame(
    {
        'cr_id': ["1008899"],
        'number_of_officer_rows': [1],
        'officer_race': [['white']],
        'officer_gender': [['M']],
        'officer_age': [["40-49"]]
    }
)

transformed_data_with_beat_id = pd.DataFrame(
    {
        'cr_id': ["1008899", "1087378", "1087387", "1087308", "1008913"],
        'beat_id': ['0111', '0111', '0111', '0111', '0111'],
        'officer_race': [['white'], ['african-american'], ['white', 'white'], ['asian'], ['asian']],
        'officer_gender': [['M'], ['M'], ['F', 'F'], ['M'], ['F']],
        'officer_age': [["40-49"], ["40-49"], ["40-49", "40-49"], ["40-49"], ["40-49"]]
    }
)

expected_transformed_data_with_beat_id = pd.DataFrame(
    {
        'cr_id': ["1008899", "1087378", "1087387", "1087308", "1008913"],
        'number_of_officer_rows': [1, 1, 2, 1, 1],
        'beat_id': [433, 111, 111, 0, 0],
        'officer_race': [["White"], ["Black or African American"], ["White", "White"],
                         ["Hispanic, Latino, or Spanish Origin"], ["Hispanic, Latino, or Spanish Origin"]],
        'officer_gender': [['M'], ['M'], ['F', 'F'], ['M'], ['F']],
        'officer_age': [["40-49"], ["40-49"], ["40-49", "40-49"], ["40-49"], ["40-49"]]
    }
)

expected_load_data = pd.DataFrame(
    {
        'cr_id': ["1008899", "1087378", "1087387", "1087308", "1008913"],
        'beat_id': [433, 111, 111, 0, 0]
    }
)
