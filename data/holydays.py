import sqlalchemy
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase


class Holydays(SqlAlchemyBase):
    __tablename__ = 'holydays'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    holyday = sqlalchemy.Column(sqlalchemy.Date, nullable=true)
