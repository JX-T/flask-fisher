# -*- coding: utf-8 -*-
# __author__ = 'Miracle'


# from app.libs.enums import PendingStatus
from sqlalchemy import Column, String, Integer, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship

from app.libs.enums import PendingStatus
from app.models.base import Base, db


class Drift(Base):
    """
        一次具体的交易信息
    """
    __tablename__ = 'drift'

    # def __init__(self):
    #     self.pending = PendingStatus.waiting
    #     super(Drift, self).__init__()

    id = Column(Integer, primary_key=True)

    # 邮寄信息
    recipient_name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)

    # 数据信息
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    # 请求者信息
    requester_id = Column(Integer)
    requester_nickname = Column(String(20))
    # requester_id = Column(Integer, ForeignKey('user.id'))
    # requester = relationship('User')

    # 赠送这信息
    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))
    # gift_id = Column(Integer, ForeignKey('gift.id'))
    # gift = relationship('Gift')

    # pending = Column('pending', SmallInteger, default=1)
    _pending = Column('pending', SmallInteger, default=1)

    @property
    def pending(self):
        return PendingStatus(self._pending)

    @pending.setter
    def pending(self, status):
        self._pending = status.value



