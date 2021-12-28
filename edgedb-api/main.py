from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import app.crud as crud
import app.models as models
import app.schemas as schemas
from app.database import SessionLocal, engine

# テーブルの作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DBセッションの作成
def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()

def init():
    db = SessionLocal()
    db.query(models.Status).delete()
    db_status = models.Status(status=0)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    
@app.get("/get-status/")
def get_status(db: Session = Depends(get_db)):
   return crud.get_status(db)

@app.post("/update-status/")
def update_status(status: schemas.StatusUpdate, db: Session = Depends(get_db)):
   return crud.update_status(db=db, status=status)

init()