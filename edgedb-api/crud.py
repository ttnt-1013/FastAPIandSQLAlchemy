from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas


def initialize_status(db: Session):
    db.query(models.Status).delete()
    db_status = models.Status(status=0)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)

def get_status(db: Session):
    return db.query(models.Status).all()[0]

def update_status(db: Session, status: schemas.StatusUpdate):
    db_status = db.query(models.Status).all()[0]
    db_status.status = status.status
    db.commit()
    db.refresh(db_status)
    return db.query(models.Status).all()[0]