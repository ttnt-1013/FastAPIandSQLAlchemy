from pydantic import BaseModel

class StatusBase(BaseModel):
   id: int
   status: int

class StatusUpdate(StatusBase):
   status: int