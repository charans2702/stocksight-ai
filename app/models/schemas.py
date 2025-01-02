from typing import List
from pydantic import BaseModel

class FinancialNews(BaseModel):
    headline: str
    source: str
    url: str
    date: str

class PriceData(BaseModel):
    symbol: str
    last_price: float
    high: float
    low: float
    volume: int
    timestamp: str

class AllFinancialNews(BaseModel):
    financial_news:List[FinancialNews]


class TechnicalAnalysis(BaseModel):
    moving_average_50: float
    moving_average_200: float
    rsi: int
    Description: str
    recommendations: str

class FundamentalAnalysis(BaseModel):
    pe_ratio: float
    eps: float
    revenue_growth: float
    debt_to_equity: float
    Description: str
    recommendations: str

class Analysis(BaseModel):
    technical: TechnicalAnalysis
    fundamental: FundamentalAnalysis

class StockData(BaseModel):
    financial_news: List[FinancialNews]
    price_data: PriceData
    analysis: Analysis

class UnifiedResponse(BaseModel):
    stock_data: StockData