from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from ..models.item import ItemModel
from ..schemas.item import ItemCreateSchema, ItemSchema, ItemUpdateSchema


def get(db_session: Session, *, item_id: int) -> ItemModel:
    return db_session.query(ItemModel).filter(ItemModel.id == item_id).first()


def get_by_name(db_session: Session, *, name: str) -> Optional[ItemModel]:
    return db_session.query(ItemModel).filter(ItemModel.name == name).first()


def list(db_session: Session, *, skip=0, limit=100) -> List[ItemSchema]:
    return db_session.query(ItemModel).offset(skip).limit(limit).all()


def create(db_session: Session, *, obj_in: ItemCreateSchema, ) -> ItemModel:
    db_obj = ItemModel(**obj_in.dict())
    db_session.add(db_obj)
    db_session.commit()
    db_session.refresh(db_obj)
    return db_obj


def update(
        db_session: Session, *, db_obj: ItemModel, obj_in: ItemUpdateSchema
) -> ItemModel:
    obj_data = jsonable_encoder(db_obj)
    update_data = obj_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db_session.add(db_obj)
    db_session.commit()
    db_session.refresh(db_obj)
    return db_obj
