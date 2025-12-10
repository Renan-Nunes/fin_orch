from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from .base_config import BaseConfig


class Item(BaseConfig):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    pluggy_item_id = Column(String(100), nullable=False, unique=True)
    institution_id = Column(Integer, ForeignKey("institution.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    status = Column(String(50))

    institution = relationship("Institution", back_populates="items")
    user = relationship("User", back_populates="items")
    account = relationship("Account", back_populates="item")
