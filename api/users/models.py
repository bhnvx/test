from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid as _uuid


class User(SQLModel, table=True):
    __tablename__ = 'user'

    id: Optional[_uuid.UUID] = Field(default_factory=_uuid.uuid4, index=True, primary_key=True)
    username: str = Field(..., min_length=4, nullable=False)
    password: str = Field(..., min_length=8, nullable=False)
    created_on: Optional[datetime] = Field(default=datetime.utcnow())
