from open_webui.models.audit_logs import AuditLog
from open_webui.internal.db import get_db


class AuditService:

    @staticmethod
    def log_event(
        event_type,
        message,
        actor_id=None,
        actor_email=None,
        target_type=None,
        target_id=None,
        metadata=None
    ):

        with get_db() as db:

            log = AuditLog(
                event_type=event_type,
                message=message,
                actor_id=actor_id,
                actor_email=actor_email,
                target_type=target_type,
                target_id=target_id,
                event_metadata=metadata
            )

            db.add(log)
            db.commit()