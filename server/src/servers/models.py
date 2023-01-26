from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from database import Base


class Server(Base):
    __tablename__ = 'servers'

    id = Column(Integer, primary_key=True, nullable=False)
    #owner_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, nullable=False)
    
    #owner = relationship('User', back_populates='servers')

    members = relationship('Member', back_populates='author_server')
    