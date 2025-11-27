from pydantic import BaseModel

class MarksBase(BaseModel):
    name: str
    marks: int

class MarksResponse(MarksBase):
    student_id: int
    model_config = {"from_attributes": True}

class CoachBase(BaseModel):
    name: str
    section: str
    subject: str


class CoachResponse(CoachBase):
    coach_id: int
    model_config = {"from_attributes": True}
