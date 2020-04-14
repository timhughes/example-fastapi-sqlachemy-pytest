from copy import copy

from example import crud
from example.models.item import ItemModel
from example.schemas.item import ItemCreateSchema, ItemUpdateSchema


def test_item_get(db_session, ):
    obj_in = ItemCreateSchema(name="test_item", description="something cool")
    item: ItemModel = crud.item.create(
        db_session, obj_in=obj_in,
    )
    item2: ItemModel = crud.item.get(db_session, item_id=item.id)
    assert item == item2


def test_item_get_by_name(db_session, ):
    obj_in = ItemCreateSchema(name="test_item", description="something cool")
    item: ItemModel = crud.item.create(
        db_session, obj_in=obj_in,
    )
    item2: ItemModel = crud.item.get_by_name(db_session, name="test_item")
    assert item == item2

def test_item_list(db_session, ):
    for i in range(1, 20):
        item = ItemCreateSchema(name=f"item{i}",
                                description=f"something cool {i}")
        crud.item.create(db_session, obj_in=item)
    item_list = crud.item.list(db_session, skip=5, limit=8)
    for i, item in enumerate(item_list, start=6):
        assert item.name == f"item{i}"
    assert len(item_list) == 8

def test_item_create(db_session, ):
    obj_in = ItemCreateSchema(name="test_item", description="something cool")
    item: ItemModel = crud.item.create(
        db_session, obj_in=obj_in,
    )
    assert item.name == "test_item"


def test_item_update(db_session, ):
    obj_setup = ItemCreateSchema(name="test_item", description="something cool")
    item: ItemModel = crud.item.create(
        db_session, obj_in=obj_setup,
    )
    obj_in = ItemUpdateSchema(name="test_item_updated")
    item_updated: ItemModel = crud.item.update(
        db_session, db_obj=copy(item), obj_in=obj_in
    )
    assert item_updated.name == "test_item_updated"
    assert item_updated is not item
