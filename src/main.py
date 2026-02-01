from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import strava

app = FastAPI(title="Running AI Coach API")

# Security: Allow your Vercel frontend to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-app.vercel.app", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(strava.router)

@app.get("/health")
def health_check():
    return {"status": "online", "engine": "running"}