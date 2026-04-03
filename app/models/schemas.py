from pydantic import BaseModel, Field


class StartInterviewRequest(BaseModel):
    role: str = Field(..., min_length=1, examples=["Backend Engineer"])
    yoe: int = Field(..., ge=0, le=40, examples=[3])


class AnswerRequest(BaseModel):
    session_id: str
    answer: str = Field(..., min_length=1)


class InterviewResponse(BaseModel):
    session_id: str
    question: str
    question_number: int
    done: bool
