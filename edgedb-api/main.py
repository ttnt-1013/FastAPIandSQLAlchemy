from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import app.crud as crud
import app.models as models
import app.schemas as schemas
from app.database import SessionLocal, engine

# テーブルの作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
crud.initialize_status(SessionLocal())

# DBセッションの作成
def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()
 
@app.get("/get-status/")
def get_status(db: Session = Depends(get_db)):
   return crud.get_status(db)

@app.post("/update-status/")
def update_status(status: schemas.StatusUpdate, db: Session = Depends(get_db)):
   return crud.update_status(db=db, status=status)