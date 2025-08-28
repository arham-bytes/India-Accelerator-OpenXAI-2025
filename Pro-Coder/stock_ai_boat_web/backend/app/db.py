from sqlmodel import create_engine, Session
import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL','sqlite:///./data.db')
engine = create_engine(DATABASE_URL, echo=False, connect_args={'check_same_thread': False} if DATABASE_URL.startswith('sqlite') else {})
def get_session():
    with Session(engine) as session:
        yield session
