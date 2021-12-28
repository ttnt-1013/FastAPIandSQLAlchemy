from sqlalchemy import Column, Integer

from app.database import Base

class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Integer)