from typing import Type
from sqlalchemy.orm import load_only
from sqlalchemy.orm import Session
from app.databases.models.base import Base
from sqlalchemy import exc
import uuid


class BaseService(object):
    session: Type[Session] = None
    model: Type[Base] = None

    def index(
            self, limit=10, offset=0, order_by=['id', 'asc'], **conditions
    ):
        query = self.session.query(self.model)
        for key, value in conditions.items():
            if isinstance(value, list):
                query = query.filter(getattr(self.model, key).in_(value))
                continue
            query = query.filter(getattr(self.model, key) == value)

        total = query.count()

        if order_by:
            query = query.order_by(getattr(
                getattr(self.model, order_by[0]),
                order_by[1]
            )())

        if limit is not None:
            query = query.limit(limit)
        if offset is not None:
            query = query.offset(offset)

        return total, query.all()

    def first(self, select_columns=None, **conditions):
        query = self.select_query(select_columns)
        for key, value in conditions.items():
            if isinstance(value, list):
                query = query.filter(getattr(self.model, key).in_(value))
                continue
            query = query.filter(getattr(self.model, key) == value)

        return query.first()

    def select_query(self, select_columns):
        sql_string = self.session.query(self.model)
        if select_columns is not None:
            sql_string = sql_string.options(load_only(*select_columns))
        return sql_string

    def create(self, flush=True, mapping=None, model=None, **data):
        try:
            if model:
                obj = model()
            else:
                obj = self.model()

            for key in data:
                p = key
                if mapping and key in mapping:
                    p = mapping.get(key)

                if hasattr(obj, key):
                    setattr(obj, key, data[p])
            if 'id' not in data:
                obj.id = str(uuid.uuid4())
            self.session.add(obj)
            if flush:
                self.session.flush()
            return obj
        except exc.IntegrityError as e:
            raise e

    def update(self, obj, flush=True, only=None, **data):
        if obj:
            for k in data:
                if hasattr(obj, k) and (only is None or k in only):
                    setattr(obj, k, data.get(k))
        if flush:
            self.session.flush()
        return obj

    def delete(self, obj, flush=True):
        try:
            self.session.delete(obj)
            if flush:
                self.session.flush()
            return True
        except exc.IntegrityError as e:
            raise e
