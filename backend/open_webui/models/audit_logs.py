import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime
from open_webui.internal.db import Base, JSONField


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    event_type = Column(String, nullable=False, index=True)

    actor_id = Column(String, nullable=True)
    actor_email = Column(String, nullable=True)

    target_type = Column(String, nullable=True)
    target_id = Column(String, nullable=True)

    message = Column(String, nullable=False)

    event_metadata = Column(JSONField, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, index=True)