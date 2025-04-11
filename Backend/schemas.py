from pydantic import BaseModel

class HealthDataCreate(BaseModel):
    user_name: str
    heart_rate: float
    steps: int
    calories: float

class HealthDataResponse(HealthDataCreate):
    id: int

    class Config:
        orm_mode = True
