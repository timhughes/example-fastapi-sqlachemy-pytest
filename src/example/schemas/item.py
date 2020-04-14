from typing import Optional

from pydantic import BaseModel


# =================================================
# Base classes should only be used to inherit from.
# =================================================

# Shared properties
class ItemBaseSchema(BaseModel):
    name: Optional[str]
    description: Optional[str] = None


# Properties needed in DB only
class ItemBaseInDBSchema(ItemBaseSchema):
    id: int
    class Config:
        orm_mode = True


# ===========================================================
# Tables below here are for use in the rest of the code base.
# ===========================================================

# Additional properties stored in DB
class ItemInDBSchema(ItemBaseInDBSchema):
    pass


# Properties to receive via API on creation
class ItemCreateSchema(ItemBaseSchema):
    pass


# Properties to receive via API on update
class ItemUpdateSchema(ItemBaseSchema):
    # group_id: Optional[int] = None
    pass


# Additional properties to return to client via API
class ItemSchema(ItemBaseSchema):
    class Config:
        orm_mode = True
