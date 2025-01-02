import json
import logging
from app.models.schemas import UnifiedResponse
from app.services.agent_service import AgentService

logger = logging.getLogger(__name__)

class StockService:
    def __init__(self):
        try:
            self.agent_service = AgentService()
            logger.info("Successfully initialized StockService")
        except Exception as e:
            logger.error(f"Failed to initialize StockService: {str(e)}")
            raise

    async def get_stock_data(self, symbol: str) -> UnifiedResponse:
        try:
            logger.info(f"Getting stock data for symbol: {symbol}")
            response = await self.agent_service.get_stock_analysis(symbol)
            
            # Ensure we're returning a UnifiedResponse
            if not isinstance(response, UnifiedResponse):
                if isinstance(response, dict):
                    response = UnifiedResponse(**response)
                else:
                    raise ValueError("Invalid response format")
            
            return response
        except Exception as e:
            error_msg = f"Error getting stock data for {symbol}: {str(e)}"
            logger.error(error_msg)
            raise RuntimeError(error_msg)
    @staticmethod
    def clean_json_response(raw_response: str) -> dict:
        try:
            if raw_response.startswith("```") and raw_response.endswith("```"):
                raw_response = raw_response.strip("`").strip()
            return json.loads(raw_response)
        except json.JSONDecodeError as e:
            error_msg = f"Invalid JSON: {str(e)}"
            logger.error(error_msg)
            raise ValueError(error_msg)