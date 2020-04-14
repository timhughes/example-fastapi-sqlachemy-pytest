from example.schemas.item import ItemCreateSchema, ItemSchema
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session



def test_group_create(
    app: FastAPI,
    db_session: Session,
    client: TestClient,
):
    group_schema = ItemCreateSchema(
        name="example", description="this is an example group",
    )
    req_data = jsonable_encoder(group_schema)
    response = client.post(
        "/api/item/",
        json=req_data,
    )
    data = response.json()
    print(data)
    assert response.status_code == 200
    assert ItemSchema(**data)
