"""Update prediction model with serialiazed data

Revision ID: f14c37993d04
Revises: 4f4fe3921983
Create Date: 2025-01-06 04:06:28.669609

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f14c37993d04'
down_revision: Union[str, None] = '4f4fe3921983'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###