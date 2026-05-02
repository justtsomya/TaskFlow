from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "member"
    admin_code: Optional[str] = None  # Required only when role == "admin"

class LoginSchema(BaseModel):
    username: str
    password: str

class ProjectCreate(BaseModel):
    name: str

class TaskCreate(BaseModel):
    title: str
    due_date: datetime
    assigned_to: int
    project_id: int

class TaskStatusUpdate(BaseModel):
    status: str  # "pending" or "completed"

class ChangePassword(BaseModel):
    username: str
    current_password: str
    new_password: str
