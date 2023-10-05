from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, TIMESTAMP


DeclarativeBase = declarative_base()


class Base(object):
    session = None

    def __init__(self, session=None, **data):
        for key, value in data.iteritems():
            setattr(self, key, value)


class DateTimestamp():
    created_at = Column(
        TIMESTAMP, nullable=True, default=datetime.utcnow
    )
    updated_at = Column(
        TIMESTAMP, nullable=True, onupdate=datetime.utcnow,
        default=datetime.utcnow
    )
