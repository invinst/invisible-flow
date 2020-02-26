from sqlalchemy.orm import relationship

from invisible_flow.constants import COPA_DB_BIND_KEY
from manage import db
from datetime import datetime
# These libraries lack mypy typing
from geoalchemy2 import Geometry  # type: ignore
from sqlalchemy.dialects import postgresql  # type: ignore


class DataArea(db.Model):
    __bind_key__ = COPA_DB_BIND_KEY
    __tablename__ = 'data_area'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    area_type = db.Column(db.String(30), nullable=False)
    polygon = db.Column(Geometry(geometry_type='MULTIPOLYGON', srid=4326))
    tags = db.Column(postgresql.ARRAY(db.String(20)), nullable=False, default=[])
    median_income = db.Column(db.String(100))
    alderman = db.Column(db.String(255))
    commander_id = db.Column(db.Integer)
    description = db.Column(db.String(255))
    police_hq_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    allegation_beat = relationship('DataAllegation',
                                   primaryjoin='and_(DataArea.id==DataAllegation.beat_id, '
                                               'DataArea.name==DataAllegation.beat_name)')

    def __repr__(self):
        return f'<id: {self.id}, ' \
               f'name: {self.name}, ' \
               f'area_type: {self.area_type}, ' \
               f'polygon: {self.polygon}, ' \
               f'tags: {self.tags}, ' \
               f'median_income: {self.median_income}, ' \
               f'alderman: {self.alderman}, ' \
               f'commander_id: {self.commander_id}, ' \
               f'description: {self.description}, ' \
               f'police_hq_id: {self.police_hq_id}, ' \
               f'created_at: {self.created_at}, ' \
               f'updated_at: {self.updated_at}, ' \
               f'>'

    def __getitem__(self, index):
        return self.__getattribute__(index)
