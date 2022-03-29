import sqlalchemy
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase


class Vacation(SqlAlchemyBase):
    __tablename__ = 'vacation'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    teacher_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("teachers.id", ondelete="CASCADE"))
    date_begin = sqlalchemy.Column(sqlalchemy.Date, nullable=true)
    date_end = sqlalchemy.Column(sqlalchemy.Date, nullable=true)
    vacation_type = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("vacation_type.id", ondelete="CASCADE"))

