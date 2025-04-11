from fastapi import FastAPI
from Backend import models
from Backend.database import engine
from Backend.api import users

# Create tables on startup
#models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Health Assistant")

# Include routes
app.include_router(users.router, prefix="/user", tags=["User"])

@app.get("/")
def root():
    return {"message": "Welcome to the AI Health Assistant"}
