from typing import Any
from pydantic import BaseModel, Field


class PageSchema(BaseModel):
    pageNumber: int = Field(..., ge=1)
    pageSize: int = Field(..., ge=1)
    total: int = 0
    items: list[Any] = []

    def __init__(self, *, pageNumber: int, pageSize: int, items: list[Any], **data):
        total = len(items)
        offset = (pageNumber - 1) * pageSize
        paged_items = items[offset:offset+pageSize]
        super().__init__(pageNumber=pageNumber, pageSize=pageSize,
                         total=total, items=paged_items, **data)
