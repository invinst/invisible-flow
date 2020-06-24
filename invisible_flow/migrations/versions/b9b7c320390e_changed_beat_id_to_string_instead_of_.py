"""changed beat_id to String instead of integer

Revision ID: b9b7c320390e
Revises: bbd684b70856
Create Date: 2020-06-24 19:55:15.612911

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from geoalchemy2.types import Geometry

# revision identifiers, used by Alembic.
revision = 'b9b7c320390e'
down_revision = 'bbd684b70856'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_allegation')
    op.create_table('data_allegation',
                    sa.Column('cr_id', sa.String(length=30), nullable=False),
                    sa.Column('crid', sa.String(length=30), nullable=True),
                    sa.Column('summary', sa.Text(), nullable=False),
                    sa.Column('add1', sa.String(length=16), nullable=False),
                    sa.Column('add2', sa.String(length=255), nullable=False),
                    sa.Column('source', sa.String(length=255), nullable=False),
                    sa.Column('beat_id', sa.String(), nullable=True),
                    sa.Column('city', sa.String(length=255), nullable=False),
                    sa.Column('incident_date', sa.DateTime(), nullable=True),
                    sa.Column('is_officer_complaint', sa.Boolean(), nullable=False),
                    sa.Column('location', sa.String(length=64), nullable=False),
                    sa.Column('old_complaint_address', sa.String(length=255), nullable=True),
                    sa.Column('subjects', postgresql.ARRAY(sa.String()), nullable=False),
                    sa.Column('point', Geometry(geometry_type='POINT', srid=4326), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('cr_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_allegation')
    op.create_table('data_allegation',
                    sa.Column('cr_id', sa.String(length=30), nullable=False),
                    sa.Column('crid', sa.String(length=30), nullable=True),
                    sa.Column('summary', sa.Text(), nullable=False),
                    sa.Column('add1', sa.String(length=16), nullable=False),
                    sa.Column('add2', sa.String(length=255), nullable=False),
                    sa.Column('source', sa.String(length=255), nullable=False),
                    sa.Column('beat_id', sa.Integer(), nullable=True),
                    sa.Column('city', sa.String(length=255), nullable=False),
                    sa.Column('incident_date', sa.DateTime(), nullable=True),
                    sa.Column('is_officer_complaint', sa.Boolean(), nullable=False),
                    sa.Column('location', sa.String(length=64), nullable=False),
                    sa.Column('old_complaint_address', sa.String(length=255), nullable=True),
                    sa.Column('subjects', postgresql.ARRAY(sa.String()), nullable=False),
                    sa.Column('point', Geometry(geometry_type='POINT', srid=4326), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('cr_id')
                    )
    # ### end Alembic commands ###
