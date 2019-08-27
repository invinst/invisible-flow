import pytest

from invisible_flow.constants import JOB_DB_BIND_KEY, VALID_STATUSES
from invisible_flow.jobs.entities import JobRecord
from manage import db


class TestJobRecord:

    @pytest.fixture
    def get_db(self):
        db.create_all(bind=JOB_DB_BIND_KEY)

        yield db

    @pytest.mark.parametrize('status', VALID_STATUSES)
    def test_job_record_entity_allows_valid_statuses(self, status):
        try:
            JobRecord(status=status)
        except Exception:
            pytest.fail('this should not have thrown an exception')

    def test_job_record_entity_does_not_allow_invalid_statuses(self):
        with pytest.raises(ValueError) as actual_error:
            JobRecord(status='invalid status')

        expected_error_string = "The status attribute on Job Record can only receive one of: ['STARTED'," \
                                " 'COMPLETED - SUCCESSFUL', 'COMPLETED - ERROR'], but received invalid status"
        assert expected_error_string == str(actual_error.value)

    def test_adding_job_record_to_db_works(self, get_db):
        for status in VALID_STATUSES:
            get_db.session.add(JobRecord(status=status))
        get_db.session.commit()
        assert len(JobRecord.query.all()) == len(VALID_STATUSES)
