import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase


class Sick_list(SqlAlchemyBase):
    __tablename__ = 'sick_list'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    timetable_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("timetables.id", ondelete="CASCADE"))
    teacher_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("teachers.id", ondelete="CASCADE"))
    timetable = orm.relation('timetables')
    teacher = orm.relation('teachers')
    date_begin = sqlalchemy.Column(sqlalchemy.Date, nullable=true)
    date_end = sqlalchemy.Column(sqlalchemy.Date, nullable=true)