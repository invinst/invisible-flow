"""Changed dataofficerunknown years_on_force from integer to string type

Revision ID: bbd684b70856
Revises: 99c65ad0d581
Create Date: 2020-06-03 20:57:05.325154

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bbd684b70856'
down_revision = '99c65ad0d581'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_officerunknown')
    op.create_table('data_officerunknown',
                    sa.Column('id', sa.Integer(), nullable=True),
                    sa.Column('data_officerallegation_id', sa.Integer(), nullable=True),
                    sa.Column('age', sa.String(length=50), nullable=True),
                    sa.Column('gender', sa.String(length=1), nullable=True),
                    sa.Column('race', sa.String(length=50), nullable=True),
                    sa.Column('years_on_force', sa.String(50), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_officerunknown')
    op.create_table('data_officerunknown',
                    sa.Column('id', sa.Integer(), nullable=True),
                    sa.Column('data_officerallegation_id', sa.Integer(), nullable=True),
                    sa.Column('age', sa.String(length=50), nullable=True),
                    sa.Column('gender', sa.String(length=1), nullable=True),
                    sa.Column('race', sa.String(length=50), nullable=True),
                    sa.Column('years_on_force', sa.Integer(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###
