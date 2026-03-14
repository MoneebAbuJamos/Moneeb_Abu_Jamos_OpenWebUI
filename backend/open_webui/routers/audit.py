from fastapi import APIRouter, Depends
from open_webui.internal.db import get_db
from open_webui.models.audit_logs import AuditLog
from open_webui.utils.auth import get_admin_user

router = APIRouter()

@router.get("/logs")
async def get_audit_logs(user=Depends(get_admin_user)):

    with get_db() as db:

        logs = (
            db.query(AuditLog)
            .order_by(AuditLog.created_at.desc())
            .limit(100)
            .all()
        )

        result = []

        for log in logs:
            result.append({
                "id": log.id,
                "event_type": log.event_type,
                "actor_email": log.actor_email,
                "target_type": log.target_type,
                "target_id": log.target_id,
                "message": log.message,
                "created_at": log.created_at,
            })

        return result