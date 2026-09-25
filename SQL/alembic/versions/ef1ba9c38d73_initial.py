"""Initial

Revision ID: ef1ba9c38d73
Revises: 
Create Date: 2026-09-25 13:03:31.954000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ef1ba9c38d73'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # SQLite has limited ALTER TABLE support, so we skip the generated 
    # alter_column statements here and just let Alembic stamp the DB.
    pass

def downgrade() -> None:
    pass
