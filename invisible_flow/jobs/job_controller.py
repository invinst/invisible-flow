from multiprocessing import Process

# from invisible_flow.app import copa_scrape
from time import sleep

from invisible_flow.jobs.jobs_mapper import JobsMapper

STARTED_STATUS = "STARTED"
COMPLETED_STATUS = 'COMPLETED - SUCCESSFUL'

'''
    This function is a placeholder until 183 is merged into master.
    The goal is to move copa_scrape out of app.py and into a separate file.
    This is because of circular dependency issues.
'''
def copa_scrape():
    sleep(40)

def do_copa_job():
    print('Creating job record')
    job = JobRecord(status=STARTED_STATUS)
    saved_job = JobsMapper.store_job(job)

    print('starting new process')
    Process(target=run_copa_scrape_and_monitor_progress, args=(saved_job.job_id,)).start()

    print('parent return child process job')
    return saved_job


def run_copa_scrape_and_monitor_progress(job_id):
    print('new process starting scrape')
    copa_scrape()
    print('new process updating job status')
    JobsMapper.update_job(job_id, COMPLETED_STATUS)
    print('new process exiting')


def get_job_status(id):
    # job = JobRecord.get(id)
    # return job.status
    pass


class JobRecord:
    def __init__(self, status, job_id=None):
        self.status = status
        self.job_id = job_id

    def __repr__(self):
        return f'<JobRecord (in memory) status: {self.status}>'

    def __eq__(self, obj: object) -> bool:
        return isinstance(obj, JobRecord) and obj.status == self.status
