from sqlalchemy import Column, Integer, String, Float
from Backend.database import Base

class HealthData(Base):
    __tablename__ = "health_data"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    heart_rate = Column(Float)
    steps = Column(Integer)
    calories = Column(Float)


