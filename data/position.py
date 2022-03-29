import sqlalchemy
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase


class Position(SqlAlchemyBase):
    __tablename__ = 'position'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    full_name = sqlalchemy.Column(sqlalchemy.String, nullable=true)
    short_name = sqlalchemy.Column(sqlalchemy.String, nullable=true)
