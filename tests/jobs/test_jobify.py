from unittest.mock import patch, Mock

from invisible_flow.jobs.jobify import jobify


def function_to_wrap(a):
    return a + 10


# @patch('invisible_flow.jobs.jobify.db')
@patch('invisible_flow.jobs.jobify.JobRecord')
@patch('invisible_flow.jobs.jobify.insert_job_record_into_database')
class TestJobify:

    @patch('invisible_flow.jobs.jobify.Process')
    def test_jobify_decorator_should_wrap_task_in_a_process(self, process_mock: Mock, insert_mock: Mock,
                                                            job_record_mock: Mock):
        wrapped_function = jobify(function_to_wrap)
        wrapped_function(1)

        process_mock.assert_called_with(target=function_to_wrap, args=(1,), kwargs={})

        process_mock.return_value.start.assert_called_with()

    @patch('invisible_flow.jobs.jobify.Process')
    def test_jobify_decorator_should_record_task_as_started(self, process_mock: Mock, insert_mock: Mock,
                                                            job_record_mock: Mock):
        wrapped_function = jobify(function_to_wrap)
        wrapped_function(1)

        process_mock.assert_called_with(target=function_to_wrap,
                                        args=(1,), kwargs={})

        process_mock.return_value.start.assert_called_with()
        insert_mock.assert_called_once()
