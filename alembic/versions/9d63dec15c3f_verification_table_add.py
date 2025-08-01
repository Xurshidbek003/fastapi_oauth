"""verification table add

Revision ID: 9d63dec15c3f
Revises: f621a2f0f918
Create Date: 2025-07-14 16:40:58.468936

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d63dec15c3f'
down_revision: Union[str, Sequence[str], None] = 'f621a2f0f918'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('verification_codes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('hashed_password', sa.String(length=255), nullable=True),
    sa.Column('code', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_verification_codes_email'), 'verification_codes', ['email'], unique=False)
    op.create_index(op.f('ix_verification_codes_id'), 'verification_codes', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_verification_codes_id'), table_name='verification_codes')
    op.drop_index(op.f('ix_verification_codes_email'), table_name='verification_codes')
    op.drop_table('verification_codes')
    # ### end Alembic commands ###
