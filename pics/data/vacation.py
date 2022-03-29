import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase


class Vacation(SqlAlchemyBase):
    __tablename__ = 'vacation'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    timetable_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("timetables.id", ondelete="CASCADE"))
    date_begin = sqlalchemy.Column(sqlalchemy.Date, nullable=true)
    date_end = sqlalchemy.Column(sqlalchemy.Date, nullable=true)
    vacation_type = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("vacation_type.id", ondelete="CASCADE"))
    timetable = orm.relation('timetables')
    vacation_type_orm = orm.relation('vacation_type')

