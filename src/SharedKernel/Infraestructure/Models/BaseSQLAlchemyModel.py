from sqlalchemy import Column, DateTime
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID as PgUUID



class BaseSQLAlchemyModel(DeclarativeBase):
    id:Column[uuid.UUID] = Column(PgUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: Column[datetime] = Column(DateTime, default=datetime.now)
    updated_at: Column[datetime] = Column(DateTime, default=datetime.now, onupdate=datetime.now)