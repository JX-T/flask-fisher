# -*- coding: utf-8 -*-
# __author__ = 'Miracle'


from sqlalchemy import Column, Integer, String
from app.models.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(20), nullable=True, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass


