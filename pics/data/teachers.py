import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase


class Teacher(SqlAlchemyBase):
    __tablename__ = 'teachers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    FIO = sqlalchemy.Column(sqlalchemy.String, nullable=true)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=true)
    category = sqlalchemy.Column(sqlalchemy.String, nullable=true)
