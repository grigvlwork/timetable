import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase


class Workload(SqlAlchemyBase):
    __tablename__ = 'workload'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    year_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("years.id", ondelete="CASCADE"))
    teacher_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("teachers.id", ondelete="CASCADE"))
    day_of_week = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    hours = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
