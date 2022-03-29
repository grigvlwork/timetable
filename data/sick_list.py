import sqlalchemy
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase


class Sick_list(SqlAlchemyBase):
    __tablename__ = 'sick_list'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    teacher_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("teachers.id", ondelete="CASCADE"))
    date_begin = sqlalchemy.Column(sqlalchemy.Date, nullable=true)
    date_end = sqlalchemy.Column(sqlalchemy.Date, nullable=true)