from fastapi import APIRouter, Depends

from app.domain.schemas.stock_list_schema import StockListSchema
from app.domain.models.stock_list import StockList
from app.domain.schemas.stock_list_name_request import StockListNameRequest
from app.domain.schemas.stock_list_symbols_request import StockListSymbolsRequest

from fastapi.responses import JSONResponse
from app.usecase.stock_list_usecase import StockListUseCase

router = APIRouter(tags=["Stock Lists"], prefix="/stock-lists")


@router.post("/", response_model=StockListSchema)
def create_stock_list(stock_list: StockListSchema, usecase: StockListUseCase = Depends(StockListUseCase)):
    return usecase.create_stock_list(StockList(**stock_list.model_dump()))


@router.put("/{id}", response_model=StockListSchema)
def update_name(id: int, request: StockListNameRequest, usecase: StockListUseCase = Depends(StockListUseCase)):
    return usecase.update_stock_list(id, request.name)


@router.post("/{id}/stocks")
def add_symbols_to_stock_list(id: int, request: StockListSymbolsRequest, usecase: StockListUseCase = Depends(StockListUseCase)):
    usecase.add_symbols_to_list(id, request.symbols)
    return JSONResponse(content={"message": "Symbols added to the list successfully"})


@router.delete("/{id}/stocks")
def remove_symbols_from_stock_list(id: int, request: StockListSymbolsRequest, usecase: StockListUseCase = Depends(StockListUseCase)):
    usecase.remove_symbols_from_list(id, request.symbols)
    return JSONResponse(content={"message": "Symbols removed from the list successfully"})

@router.delete("/{id}")
def delete_stock_list(id: int, usecase: StockListUseCase = Depends(StockListUseCase)):
    usecase.delete_list(id)
    return JSONResponse(content={"message": "Stock list deleted successfully"})