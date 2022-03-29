import sqlalchemy
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase


class Replacement(SqlAlchemyBase):
    __tablename__ = 'replacement'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    substitute_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("teachers.id", ondelete="CASCADE"))
    replaced_id = sqlalchemy.Column(sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey("teachers.id", ondelete="CASCADE"))
    date_repl = sqlalchemy.Column(sqlalchemy.Date, nullable=true)
    hours = sqlalchemy.Column(sqlalchemy.Integer, nullable=true)
