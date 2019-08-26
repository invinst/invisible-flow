import pytest

from invisible_flow.app_factory import AppFactory
from invisible_flow.constants import JOB_DB_BIND_KEY, VALID_STATUSES
from invisible_flow.jobs.entities import JobRecord
from manage import setup_db


class TestJobRecord:

    @pytest.fixture
    def db(self):
        db = setup_db(AppFactory.create_app())
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
