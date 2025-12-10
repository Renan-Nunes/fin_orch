from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base_config import BaseConfig


class Institution(BaseConfig):
    __tablename__ = "institution"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    connector_code = Column(String(50), nullable=True)
    type = Column(String(50), nullable=True)  # bank, investment, credit_card

    items = relationship("Item", back_populates="institution")
