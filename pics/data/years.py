import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase

class Years(SqlAlchemyBase):
    __tablename__ = 'years'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)    
    begin_year = sqlalchemy.Column(sqlalchemy.Integer, nullable=true)
    end_year = sqlalchemy.Column(sqlalchemy.Integer, nullable=true)
