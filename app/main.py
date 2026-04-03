from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.controllers.interview import router as interview_router

app = FastAPI(title="AI Interview Trainer", version="1.0.0")

app.include_router(interview_router)


@app.get("/")
async def serve_ui():
    return FileResponse("app/templates/index.html")
