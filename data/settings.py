import sqlalchemy

from .db_session import SqlAlchemyBase


class Settings(SqlAlchemyBase):
    __tablename__ = 'settings'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    parameter = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    value = sqlalchemy.Column(sqlalchemy.String, nullable=True)