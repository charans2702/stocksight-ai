from fastapi import APIRouter, HTTPException, status
from typing import Optional
from app.models.schemas import UnifiedResponse
from app.services.stock_service import StockService

router = APIRouter()
stock_service = StockService()

@router.get(
    "/stock/{symbol}",
    response_model=UnifiedResponse,
    responses={
        404: {"description": "Stock symbol not found"},
        400: {"description": "Invalid stock symbol"},
        500: {"description": "Internal server error"},
    }
)
async def get_stock_analysis(symbol: str):
    if not symbol or len(symbol) > 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid stock symbol length"
        )
    
    try:
        return await stock_service.get_stock_data(symbol.upper())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))