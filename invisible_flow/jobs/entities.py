from sqlalchemy.orm import validates  # type: ignore

from invisible_flow.constants import VALID_STATUSES, COPA_DB_BIND_KEY
from manage import db


class JobRecordModel(db.Model):
    __tablename__ = 'job_record'
    __bind_key__ = COPA_DB_BIND_KEY
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)

    def __repr__(self):
        return f'<JobRecord {self.id} status: {self.status}>'

    @validates('status')
    def validate_status(self, attribute_name, attribute_value):
        if attribute_value not in VALID_STATUSES:
            raise ValueError(
                f'The status attribute on Job Record can only receive one of: {VALID_STATUSES}'
                f', but received \"{attribute_value}\"')
        return attribute_value

    def __eq__(self, obj: object) -> bool:
        return isinstance(obj, JobRecordModel) and obj.id == self.id and obj.status == self.status


def insert_job_record_into_database(job: JobRecordModel):
    db.session.add(job)
    db.session.commit()
