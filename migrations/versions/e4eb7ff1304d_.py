"""empty message

Revision ID: e4eb7ff1304d
Revises: 92b265ccde53
Create Date: 2020-05-03 22:58:39.393041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4eb7ff1304d'
down_revision = '92b265ccde53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'menu_items', 'restaurants', ['restaurant_id'], ['id'])
    op.create_foreign_key(None, 'reservations', 'restaurants', ['restaurant_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reservations', type_='foreignkey')
    op.drop_constraint(None, 'menu_items', type_='foreignkey')
    # ### end Alembic commands ###