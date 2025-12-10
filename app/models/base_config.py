from sqlalchemy import DateTime, Column
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

Base = declarative_base()


class BaseConfig(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    excluded_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
