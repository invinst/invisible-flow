# from invisible_flow.app import copa_scrape

print("here1")
from invisible_flow.jobs.jobs_mapper import JobsMapper
from invisible_flow.task import run_copa_scrape_and_monitor_progress

STARTED_STATUS = "STARTED"
COMPLETED_STATUS = 'COMPLETED'

'''
    This function is a placeholder until 183 is merged into master.
    The goal is to move copa_scrape out of app.py and into a separate file.
    This is because of circular dependency issues.
'''


def do_copa_job():
    print('Parent: creating job record')
    job = JobRecord(status=STARTED_STATUS)
    saved_job = JobsMapper.store_job(job)

    print('Parent: starting copa job in new process')
    run_copa_scrape_and_monitor_progress.delay(saved_job.job_id)
    # Process(target=run_copa_scrape_and_monitor_progress, args=(saved_job.job_id,)).start()

    print('Parent: returning job id of copa scrape')
    return saved_job


def get_job_status(id):
    job = JobsMapper.get_job(id)
    if job is None:
        raise Exception(f'Requested job id "{id}" is not in database')
    return job.status


class JobRecord:
    def __init__(self, status, job_id=None):
        self.status = status
        self.job_id = job_id

    def __repr__(self):
        return f'<JobRecord (in memory) status: {self.status}>'

    def __eq__(self, obj: object) -> bool:
        return isinstance(obj, JobRecord) and obj.status == self.status
