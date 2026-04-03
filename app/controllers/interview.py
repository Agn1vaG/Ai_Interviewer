from fastapi import APIRouter, HTTPException

from app.models.schemas import AnswerRequest, InterviewResponse, StartInterviewRequest
from app.services.ai import AIService
from app.services.interview import InterviewService

router = APIRouter(prefix="/api/interview", tags=["interview"])

_ai_service = AIService()
_interview_service = InterviewService(_ai_service)


@router.post("/start", response_model=InterviewResponse)
async def start_interview(req: StartInterviewRequest):
    return _interview_service.start(role=req.role, yoe=req.yoe)


@router.post("/answer", response_model=InterviewResponse)
async def submit_answer(req: AnswerRequest):
    try:
        return _interview_service.answer(session_id=req.session_id, answer=req.answer)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
