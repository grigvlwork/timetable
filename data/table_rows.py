import sqlalchemy
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase


class Table_row(SqlAlchemyBase):
    __tablename__ = 'table_rows'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    timetable_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("timetables.id", ondelete="CASCADE"))
    teacher_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("teachers.id", ondelete="CASCADE"))
    data_row = sqlalchemy.Column(sqlalchemy.String, nullable=true)
