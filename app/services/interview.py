import uuid

from app.config import get_settings
from app.models.schemas import InterviewResponse
from app.services.ai import AIService

SYSTEM_PROMPT = (
    "You are a technical interviewer. The candidate is applying for the role of '{role}' "
    "with {yoe} years of experience. Ask one interview question at a time. "
    "Tailor difficulty to their experience level. Base follow-up questions on their answers. "
    "Be concise — just ask the question, no preamble. "
    "When told it's the final question, also provide a brief performance summary with strengths, "
    "weaknesses, and an overall rating out of 10."
)


class InterviewService:
    def __init__(self, ai_service: AIService):
        self._ai = ai_service
        self._sessions: dict = {}
        self._max_questions = get_settings().MAX_QUESTIONS

    def start(self, role: str, yoe: int) -> InterviewResponse:
        session_id = str(uuid.uuid4())
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT.format(role=role, yoe=yoe)},
            {"role": "user", "content": "Start the interview. Ask your first question."},
        ]
        question = self._ai.get_completion(messages)
        messages.append({"role": "assistant", "content": question})

        self._sessions[session_id] = {"messages": messages, "count": 1}
        return InterviewResponse(
            session_id=session_id, question=question, question_number=1, done=False
        )

    def answer(self, session_id: str, answer: str) -> InterviewResponse:
        session = self._sessions.get(session_id)
        if not session:
            raise ValueError("Session not found or expired.")

        count = session["count"]
        messages = session["messages"]

        is_final = count >= self._max_questions
        if is_final:
            prompt = f"My answer: {answer}\n\nThat was the final question. Please provide your performance summary."
        else:
            prompt = f"My answer: {answer}\n\nAsk the next question."

        messages.append({"role": "user", "content": prompt})
        reply = self._ai.get_completion(messages)
        messages.append({"role": "assistant", "content": reply})

        session["count"] = count + 1

        if is_final:
            del self._sessions[session_id]

        return InterviewResponse(
            session_id=session_id,
            question=reply,
            question_number=count + 1,
            done=is_final,
        )
