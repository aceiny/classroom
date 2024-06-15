
import datetime
from pydantic import BaseModel , EmailStr
from enum import Enum

class CourseWorkType(Enum):
    Assignment = "Assignment"
    Quiz = "Quiz"
    Exam = "Exam"
    Project = "Project"
    Other = "Other"

class CreateCoursworkDto(BaseModel):
    title: str
    description: str
    due_date: datetime.datetime
    type: CourseWorkType