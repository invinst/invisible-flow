from multiprocessing import Process

from invisible_flow.jobs.entities import insert_job_record_into_database, JobRecordModel


def jobify(wrapped_function):
    def _wrapper(*args, **kwargs):
        print('here')
        process = Process(target=wrapped_function, args=args, kwargs=kwargs)

        job = JobRecordModel(status='STARTED')
        insert_job_record_into_database(job)

        process.start()

    return _wrapper
