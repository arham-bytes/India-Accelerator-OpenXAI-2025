from sqlmodel import SQLModel, Field
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str
    hashed_password: str
class UserCreate(SQLModel):
    email: str
    password: str
