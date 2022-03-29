import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase


class Timetable(SqlAlchemyBase):
    __tablename__ = 'timetables'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    year_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("years.id", ondelete="CASCADE"))
    month = sqlalchemy.Column(sqlalchemy.Integer, nullable=true)
    year = orm.relation('years')
