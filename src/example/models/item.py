from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from example.db.session import DBBase


class ItemModel(DBBase):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
