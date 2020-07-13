from collections import namedtuple
from unittest import mock
from unittest.mock import Mock, patch, call

import pytest

# from invisible_flow.jobs.entities import JobRecord
from invisible_flow.jobs.job_controller import start_copa_job, JobRecord, do_copa_job
import pdb


class MockJobRecord(object):
    pass


class TestJobController:
    blah = MockJobRecord()

    # db_mock =
    # manage.py
    @patch('invisible_flow.jobs.job_controller.JobsMapper', autospec=True)
    @patch('invisible_flow.jobs.job_controller.copa_scrape', autospec=True)  # mocking the single copa_scrape function
    # @patch('invisible_flow.jobs.job_controller.JobRecord', new_callable=MockJobRecord)
    def test_startCopaJob_should_start_copa_job_and_return_job_id(self, copa_scrape_mock, jobs_mapper_mock):
        JobRecordModel = namedtuple('JobRecordModel', ['id'])
        jobs_mapper_mock.return_value.store_job.return_value = JobRecordModel(id=1)

        retval = do_copa_job()

        assert retval.id == 1
        expected_started_job_record = JobRecord(status="STARTED")

        jobs_mapper_mock.return_value.store_job.assert_called_with(expected_started_job_record)
        copa_scrape_mock.assert_called()

# def test_should_return_
