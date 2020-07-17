from unittest.mock import patch

from invisible_flow.jobs.job_controller import JobRecord
from invisible_flow.jobs.job_controller import run_copa_scrape_and_monitor_progress, do_copa_job


class TestJobController:

    @patch('invisible_flow.jobs.job_controller.JobsMapper', autospec=True)
    @patch('invisible_flow.jobs.job_controller.Process', autospec=True)  # mocking the single copa_scrape function
    def test_do_copa_job_should_spawn_process_store_job_and_return_job_id(self, process_mock, jobs_mapper_mock):
        jobs_mapper_mock.store_job.return_value = JobRecord(status="STARTED", job_id=1)

        saved_job = do_copa_job()

        assert saved_job.job_id == 1
        jobs_mapper_mock.store_job.assert_called_with(JobRecord(status="STARTED"))
        process_mock.assert_called_with(target=run_copa_scrape_and_monitor_progress, args=(1,))

    @patch('invisible_flow.jobs.job_controller.copa_scrape', autospec=True)
    @patch('invisible_flow.jobs.job_controller.JobsMapper.update_job')
    def test_job_status_is_updated_when_copa_scrape_done(self, update_job_mock, copa_scrape_mock):
        run_copa_scrape_and_monitor_progress(job_id=1)

        copa_scrape_mock.assert_called()
        update_job_mock.assert_called_with(1, "COMPLETED")
