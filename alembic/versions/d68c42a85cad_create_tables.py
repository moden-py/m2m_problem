"""create tables

Revision ID: d68c42a85cad
Revises: 
Create Date: 2017-01-30 12:33:29.863809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd68c42a85cad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Country_test',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('geoid', sa.Integer, nullable=False, unique=True),
        sa.Column('name', sa.String(64), nullable=False),
    )

    op.create_table(
        'Address_test',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('Country_id', sa.Integer, sa.ForeignKey("Country_test.id"),
                  nullable=False),
        sa.Column('type', sa.Enum('business',
                                  'mail',
                                  'billing',
                                  name='address_type_test'), nullable=False),
    )

    op.create_table(
        'Establishment_test',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(64), nullable=False),
    )

    op.create_table('EstablishmentAddress_test',
        sa.Column('establishment_id', sa.Integer,
                  sa.ForeignKey("Establishment_test.id"),
                  primary_key=True),
        sa.Column('address_id', sa.Integer,
                  sa.ForeignKey("Address_test.id"),
                  primary_key=True),
        )


def downgrade():
    connection = op.get_bind()
    op.drop_table('EstablishmentAddress_test')
    op.drop_table('Establishment_test')
    op.drop_table('Address_test')
    connection.execute('DROP TYPE address_type_test;', execution_options=None)
    op.drop_table('Country_test')
