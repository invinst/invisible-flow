from invisible_flow.jobs.entities import JobRecordModel
from manage import db


class JobsMapper:
    @staticmethod
    def store_job(job):
        job_model = JobRecordModel(status=job.status)

        db.session.add(job_model)
        db.session.commit()

        if job_model.id is not None:
            job.job_id = job_model.id
            return job
        else:
            raise Exception(f"Job model id was none! {job_model}, came from {job}")

    @staticmethod
    def get_job(job_id: float):
        return JobRecordModel.query.get(job_id)

    @staticmethod
    def update_job(job_id: int, new_status: str):
        JobsMapper.get_job(job_id).status = new_status
        db.session.commit()
