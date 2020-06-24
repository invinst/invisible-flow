import pdb

import pytest

from invisible_flow.constants import COPA_DB_BIND_KEY
from invisible_flow.copa.allegation_loader import AllegationLoader
import pandas as pd

from invisible_flow.copa.data_allegation import DataAllegation
from manage import db

class TestAllegationLoader:

    @pytest.fixture(autouse=True)
    def set_up(self):
        db.session.close()
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)

    @pytest.mark.focus
    def test_allegation_loader_should_load_new_rows(self):
        test_loader = AllegationLoader()

        fake_new_rows = pd.DataFrame({
            "cr_id": ["33333333", "1111111", "999999", "100000", "100007"],
            "beat_id": ["111", "112", "114", "121", ""]
        })

        test_loader.load_allegation_into_db(fake_new_rows)

        queried_allegation_data = DataAllegation.query.all()
        #pdb.set_trace()

        assert(len(queried_allegation_data) == len(fake_new_rows.index))

