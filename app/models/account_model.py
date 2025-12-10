from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, ForeignKey, String, DECIMAL, DateTime
from typing import Optional
from datetime import datetime
from .base_config import BaseConfig


class Account(BaseConfig):
    __tablename__ = "account"

    id: int = Column(Integer, primary_key=True, index=True)
    pluggy_account_id: str = Column(String(100), nullable=False, unique=True)
    item_id: int = Column(Integer, ForeignKey("item.id"))
    name: Optional[str] = Column(String(100))
    type: Optional[str] = Column(String(50))  # checking, savings, credit_card
    number: Optional[str] = Column(String(50))
    branch: Optional[str] = Column(String(50))
    balance: Optional[DECIMAL] = Column(DECIMAL(15, 2))
    currency: Optional[str] = Column(String(10))

    item = relationship("Item", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")