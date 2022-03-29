import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Vacation_type(SqlAlchemyBase):
    __tablename__ = 'vacation_type'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    symbol = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    