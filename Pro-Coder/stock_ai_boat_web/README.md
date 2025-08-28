# Stock-AI-Boat (Web)
Full-stack web hackathon project: React frontend (Vite + Tailwind) + FastAPI backend.

## Quick start (dev)
1. Start backend:
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate   # Windows: .\.venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload --port 8000
   ```
2. Start frontend (requires Node.js + npm/yarn):
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
3. Open `http://localhost:5173` (Vite default) to view the app. The frontend will call the backend at `http://localhost:8000/api` by default.

## Docker
A docker-compose file is included to run both services together.

## Notes
- ML inference uses demo heuristics in `backend/app/models/ml.py`. Replace with your trained models for better accuracy.
- Update SECRET_KEY in `backend/.env` before pushing to public repo.
