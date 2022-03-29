import sqlalchemy
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase


class Profession(SqlAlchemyBase):
    __tablename__ = 'profession'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    full_name = sqlalchemy.Column(sqlalchemy.String, nullable=true)
    short_name = sqlalchemy.Column(sqlalchemy.String, nullable=true)
