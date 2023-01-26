from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    server_id = Column(Integer, ForeignKey('servers.id'), nullable=False)

    author_user = relationship('User', back_populates='memberships')
    author_server = relationship('Server', back_populates='members')