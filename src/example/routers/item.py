import logging

from example import crud
from example.schemas.item import ItemSchema, ItemCreateSchema
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .utils.db import get_db

router = APIRouter()

logger = logging.getLogger('example')


@router.post("/", response_model=ItemSchema, name="item:create")
def item_create(
        *,
        db: Session = Depends(get_db),
        item_in: ItemCreateSchema,
):
    item = crud.item.create(
        db_session=db,
        obj_in=item_in,
    )
    return item


@router.get("/{slug}", response_model=ItemSchema, name="item:get")
def item_get(
        *,
        db: Session = Depends(get_db),
        slug: str,
):
    raise NotImplementedError


@router.put("/{slug}", response_model=ItemSchema, name="item:update")
def item_update(
        *,
        db: Session = Depends(get_db),
        slug: str,
):
    raise NotImplementedError


@router.delete("/{slug}", name="item:archive")
def item_archive(
        *,
        db: Session = Depends(get_db),
        slug: str,
):
    raise NotImplementedError
