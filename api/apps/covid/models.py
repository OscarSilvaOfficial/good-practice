from api.bases.repository.base import BaseModel
from api.sqlalchemy import db

class Covid(BaseModel):
    date = db.Column(db.Date, nullable=True)