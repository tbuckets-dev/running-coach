from fastapi import APIRouter, Query, HTTPException, Request
from src.core.config import settings

router = APIRouter(prefix="/webhooks/strava", tags=["strava"])

@router.get("/")
async def strava_webhook_validation(
    mode: str = Query(None, alias="hub.mode"),
    token: str = Query(None, alias="hub.verify_token"),
    challenge: str = Query(None, alias="hub.challenge")
):
    """
    Handles the initial 'handshake' from Strava to verify your server.
    """
    if mode == "subscribe" and token == settings.STRAVA_VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return {"hub.challenge": challenge}
    
    raise HTTPException(status_code=403, detail="Verification token mismatch")

@router.post("/")
async def handle_strava_event(request: Request):
    """
    This is where Strava POSTS data whenever a user finishes a run.
    """
    event_data = await request.json()
    
    # Example Event: {'object_type': 'activity', 'aspect_type': 'create', 'object_id': 123456}
    if event_data.get("object_type") == "activity":
        activity_id = event_data.get("object_id")
        # TODO: Trigger a Celery worker to fetch the full activity details
        print(f"New activity detected: {activity_id}")
    
    return {"status": "success"}