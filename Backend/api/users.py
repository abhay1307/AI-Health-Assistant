from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Backend.database import get_db
from Backend import schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.HealthDataResponse)
def create_data(data: schemas.HealthDataCreate, db: Session = Depends(get_db)):
    return crud.create_health_data(db, data)

@router.get("/", response_model=list[schemas.HealthDataResponse])
def get_data(db: Session = Depends(get_db)):
    return crud.get_all_health_data(db)
