from multiprocessing import Process

# from invisible_flow.app import copa_scrape
from time import sleep

from invisible_flow.jobs.jobs_mapper import JobsMapper
from manage import db

STARTED_STATUS = "STARTED"
COMPLETED_STATUS = 'COMPLETED'

'''
    This function is a placeholder until 183 is merged into master.
    The goal is to move copa_scrape out of app.py and into a separate file.
    This is because of circular dependency issues.
'''


def copa_scrape():
    sleep(40)


def do_copa_job():
    print('Parent: creating job record')
    job = JobRecord(status=STARTED_STATUS)
    saved_job = JobsMapper.store_job(job)

    print('Parent: starting copa job in new process')
    Process(target=run_copa_scrape_and_monitor_progress, args=(saved_job.job_id,)).start()

    print('Parent: returning job id of copa scrape')
    return saved_job


def run_copa_scrape_and_monitor_progress(job_id):
    print('Child: disposing of old database connections')
    # doing this because: https://stackoverflow.com/questions/22752521/uwsgi-flask-sqlalchemy-and-postgres-ssl-error-decryption-failed-or-bad-reco
    # Solution taken from here: https://stackoverflow.com/questions/45215596/flask-and-celery-on-heroku-sqlalchemy-exc-databaseerror-psycopg2-databaseerro
    # Documentation for solution is here: https://docs.sqlalchemy.org/en/13/core/connections.html#engine-disposal
    db.engine.dispose()
    print('Child: starting scrape')
    copa_scrape()
    print('Child: scrape finished, updating job status')
    JobsMapper.update_job(job_id, COMPLETED_STATUS)
    print('Child: exiting')


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
