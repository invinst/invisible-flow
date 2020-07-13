import subprocess

# from flask import jsonify
# from flask_injector import FlaskInjector
# from injector import inject
# from sqlalchemy.orm import validates
#
# from invisible_flow.app import copa_scrape
# from invisible_flow.app_factory import app
# from invisible_flow.constants import VALID_STATUSES
# # from invisible_flow.jobs.entities import JobRecord
# from invisible_flow.jobs.jobs_mapper import JobsMapper
#
# import pdb
#
# # job_ids = {}
# # counter = 0
#
# STARTED_STATUS = "STARTED"
# COMPLETED_STATUS = 'COMPLETED - SUCCESSFUL'
#
#
# @app.route("/start_copa_job")
# def start_copa_job():
#     retval = do_copa_job()
#     # copa_scrape()
#     return jsonify(retval)
#
#
# #
#
# def do_copa_job():
#     job_mapper = JobsMapper()
#
#     job = JobRecord(status=STARTED_STATUS)
#     saved_job = job_mapper.store_job(job)
#
#     run_copa_job_in_separate_process()
#
#     return saved_job
#
#     # return
#     # job_mapper.update_job(saved_job_id, COMPLETED_STATUS)
from multiprocessing import Process

from invisible_flow.app import copa_scrape

def save_me():


def run_copa_job_in_separate_process():
    # os.environ["foo"] = "bar"
    process = Process(target=copa_scrape)
    process.start()
    print("starting")
    # subprocess.run(["ls", "-l", "/dev/null"], capture_output=True, shell=True)
    print("finished external")
    process.join()
    # copa_scrape()


run_copa_job_in_separate_process()


#
#
# def get_job_status(id):
#     # job = JobRecord.get(id)
#     # return job.status
#     pass
#
# class JobRecord:
#
#     def __init__(self, status):
#         self.status = status
#         # self.job_id = job_id
#
#     def __repr__(self):
#         return f'<JobRecord (in memory) status: {self.status}>'
#
#     @validates('status')
#     def validate_status(self, attribute_name, attribute_value):
#         if attribute_value not in VALID_STATUSES:
#             raise ValueError(
#                 f'The status attribute on Job Record can only receive one of: {VALID_STATUSES}'
#                 f', but received {attribute_value}')
#
#     def __eq__(self, obj: object) -> bool:
#         return isinstance(obj, JobRecord) and obj.status == self.status
