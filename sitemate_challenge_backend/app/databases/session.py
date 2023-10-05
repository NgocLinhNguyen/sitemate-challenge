import os
from contextlib import contextmanager
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, scoped_session
import greenlet


db_session = scoped_session(sessionmaker(autocommit=False))
db_flask_session = scoped_session(
    sessionmaker(autocommit=False),
    scopefunc=greenlet.getcurrent
)


def db_engine():
    engine = create_engine(
        os.getenv('DATABASE_URI'), pool_size=20
    )
    return engine


@contextmanager
def session_scope(scope=None, auto_commit=True, auto_close=True):
    """Provide a transactional scope around a series of operations."""
    session = scope
    try:
        yield session
        if auto_commit:
            session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        if auto_close:
            session.close()
