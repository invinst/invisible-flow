from invisible_flow.jobs.entities import JobRecordModel
from manage import db


class JobsMapper:
    def store_job(self, job):
        job_model = JobRecordModel(status=job.status)

        db.session.add(job_model)
        db.session.commit()

        db.session.close()

        if job_model.id is not None:
            return job_model
        else:
            raise Exception(f"Job model id was none! {job_model}, came from {job}")


    def get_job(self, job_id: float):
        return JobRecordModel.query.get(job_id)

    def update_job(self, job_id: int, new_status: str):
        self.get_job(job_id).status = new_status
        db.session.commit()