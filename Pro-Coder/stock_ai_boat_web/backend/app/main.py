import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
from app.api import router as api_router
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL','sqlite:///./data.db')
engine = create_engine(DATABASE_URL, echo=False, connect_args={'check_same_thread': False} if DATABASE_URL.startswith('sqlite') else {})
app = FastAPI(title='Stock-AI-Boat API')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])
@app.on_event('startup')
def on_startup():
    SQLModel.metadata.create_all(engine)
app.include_router(api_router, prefix='/api')
