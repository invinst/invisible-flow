import pytest

from invisible_flow.constants import VALID_STATUSES
from invisible_flow.jobs.entities import JobRecordModel
from manage import db


class TestJobRecord:

    @pytest.fixture(autouse=True)
    def set_up(self):
        db.session.close()
        db.drop_all()
        db.create_all()

    @pytest.mark.parametrize('status', VALID_STATUSES)
    def test_job_record_entity_allows_valid_statuses(self, status):
        try:
            JobRecordModel(status=status)
        except Exception:
            pytest.fail('this should not have thrown an exception')

    def test_job_record_entity_does_not_allow_invalid_statuses(self):
        with pytest.raises(ValueError) as actual_error:
            JobRecordModel(status='invalid status')

        expected_error_string = "The status attribute on Job Record can only receive one of: ['STARTED'," \
                                " 'COMPLETED'], but received \"invalid status\""
        assert expected_error_string == str(actual_error.value)

    def test_adding_job_record_to_db_works(self):
        for status in VALID_STATUSES:
            db.session.add(JobRecordModel(status=status))
        db.session.commit()
        assert len(JobRecordModel.query.all()) == len(VALID_STATUSES)
