# AI Interviewer – Intelligent Technical Interview Platform

AI-powered technical interviewer that simulates real interview scenarios and evaluates responses in real time.

---


## Overview

AI Interviewer is an automated technical interview system that simulates real interview scenarios. It generates questions, evaluates answers, and provides structured feedback without requiring a human interviewer. The platform is designed to assess problem-solving ability, technical knowledge, and response quality in a controlled environment.

---

## Features

### Automated Interview Flow

* Dynamic question generation
* Multi-domain support (DSA, Backend, Frontend, Databases)
* Step-by-step interview progression

### Response Evaluation

* Analyzes user answers
* Evaluates correctness and depth
* Identifies knowledge gaps

### Interactive System

* Continuous question-response cycle
* Context-aware follow-up questions
* Simulates real interview conditions

### Feedback Engine

* Highlights strengths and weaknesses
* Provides improvement insights

---

## Tech Stack

* Backend: Python, Flask
* Frontend: HTML, CSS, JavaScript
* AI Integration: LLM-based processing
* Environment Management: python-dotenv

---

## Project Structure

```
project/
│
├── start.py
├── app/
│   ├── controller/
│   │   ├── home_controller.py
│   │   ├── submit_controller.py
│   │   ├── polling_controller.py
│   │   ├── reload_controller.py
│   │   └── coder_controller.py
│
├── templates/
│   └── index.html
│
├── static/
│
└── .env
```

---

## Requirements

* Python 3.8+
* pip

---

## Installation

```
git clone <your-repo-link>
cd <project-folder>
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_key_here
```

---

## Run the Application

```
python start.py
```

Access the app at:

```
http://127.0.0.1:8000
```

---

## API Endpoints

| Endpoint             | Method | Description                    |
| -------------------- | ------ | ------------------------------ |
| `/`                  | GET    | Load main interface            |
| `/flask-api/submit`  | POST   | Start interview / submit input |
| `/flask-api/polling` | POST   | Fetch ongoing results          |
| `/flask-api/reload`  | POST   | Reload previous results        |
| `/flask-api/code`    | POST   | Generate code                  |
| `/flask-api/health`  | GET    | Health check                   |

---

## How It Works

1. User starts an interview session
2. System generates a question based on domain
3. User submits a response
4. Backend evaluates the answer
5. Feedback is generated
6. Next question is triggered
7. Process repeats

---

## Limitations

* Uses polling instead of real-time streaming
* Evaluation quality depends on input prompts
* No persistent session storage

---

## Future Improvements

* WebSocket-based real-time interaction
* Voice-based interview support
* Candidate scoring and ranking system
* Authentication and user profiles

---

## License

This project is for educational and demonstration purposes.
