from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    userId = Column(Integer, primary_key=True)
    point = Column(Integer)