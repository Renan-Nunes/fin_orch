from sqlalchemy import String, Integer, DateTime, Column
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from .base_config import BaseConfig


class User(BaseConfig):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    phone_nm = Column(String(20), nullable=True)
    items = relationship("Item", back_populates="user")
