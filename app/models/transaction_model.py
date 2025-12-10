from sqlalchemy import Column, DECIMAL, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from typing import Optional
from .base_config import BaseConfig

class Transaction(BaseConfig):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)
    pluggy_transaction_id = Column(String(100), nullable=False, unique=True)
    account_id = Column(Integer, ForeignKey("account.id"))
    description = Column(String, nullable=True)
    category = Column(String(100), nullable=True)
    type = Column(String(10), nullable=True)  # credit / debit
    amount = Column(DECIMAL(15, 2), nullable=True)
    date = Column(Date, nullable=True)

    account = relationship("Account", back_populates="transactions")
