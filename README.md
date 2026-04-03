# AI Interview Trainer

An AI-powered mock interview application that generates role-specific technical questions, adapts follow-ups based on your responses, and provides a performance summary at the end.

## Architecture

```
app/
├── main.py                  # FastAPI application entry point
├── config.py                # Centralized settings (env-based)
├── controllers/
│   └── interview.py         # Route handlers (API layer)
├── services/
│   ├── ai.py                # OpenAI integration
│   └── interview.py         # Interview session & business logic
├── models/
│   └── schemas.py           # Pydantic request/response models
└── templates/
    └── index.html           # Frontend UI
```

## Setup

1. **Clone & install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

3. **Run the server**
   ```bash
   uvicorn app.main:app --reload
   ```

4. Open **http://localhost:8000** in your browser.

## API Endpoints

| Method | Endpoint               | Description              |
|--------|------------------------|--------------------------|
| GET    | `/`                    | Serve the frontend UI    |
| POST   | `/api/interview/start` | Start a new interview    |
| POST   | `/api/interview/answer`| Submit answer, get next Q|

## How It Works

1. Enter your target role and years of experience.
2. The AI interviewer asks 10 questions, one at a time.
3. Each follow-up is tailored based on your previous answer.
4. After the final question, you receive a performance summary with strengths, weaknesses, and a rating.
