from sqlalchemy.orm import validates

from invisible_flow.constants import JOB_DB_BIND_KEY, VALID_STATUSES
from manage import db


class JobRecord(db.Model):
    __bind_key__ = JOB_DB_BIND_KEY
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)

    def __repr__(self):
        return f'<JobRecord {self.id} status: {self.status}>'

    @validates('status')
    def validate_status(self, attribute_name, attribute_value):
        if attribute_value not in VALID_STATUSES:
            raise ValueError(
                f'The status attribute on Job Record can only receive one of: {VALID_STATUSES}'
                f', but received {attribute_value}')


def insert_job_record_into_database(job: JobRecord):
    db.session.add(job)
    db.session.commit()
