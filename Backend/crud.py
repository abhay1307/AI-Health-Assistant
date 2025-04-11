from sqlalchemy.orm import Session
from Backend import models, schemas

def create_health_data(db: Session, data: schemas.HealthDataCreate):
    new_data = models.HealthData(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

def get_all_health_data(db: Session):
    return db.query(models.HealthData).all()
