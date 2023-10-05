from app.databases.models.base import (
    DeclarativeBase, Base, DateTimestamp
)
import sqlalchemy as sa


class Issue(DeclarativeBase, Base, DateTimestamp):
    __tablename__ = 'issues'

    id = sa.Column(sa.String, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }
