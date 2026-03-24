import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, inspect
from open_webui.internal.db import Base, JSONField, engine


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


# ============================
# ✅ AUTO CREATE TABLE (FIX)
# ============================
try:
    inspector = inspect(engine)

    if "audit_logs" not in inspector.get_table_names():
        AuditLog.__table__.create(bind=engine)
        print("✅ audit_logs table created")
except Exception as e:
    print("⚠️ audit_logs init error:", e)