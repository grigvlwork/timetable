import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Work_weekend(SqlAlchemyBase):
    __tablename__ = 'work_weekends'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    date_work = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    day_of_week = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    