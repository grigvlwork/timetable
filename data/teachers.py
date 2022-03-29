import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.sql.expression import true

from .db_session import SqlAlchemyBase


class Teacher(SqlAlchemyBase):
    __tablename__ = 'teachers'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    FIO = sqlalchemy.Column(sqlalchemy.String, nullable=true)
    position_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("position.id", ondelete="CASCADE"))
    category_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("category.id", ondelete="CASCADE"))
    profession_id = sqlalchemy.Column(sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey("category.id", ondelete="CASCADE"))
