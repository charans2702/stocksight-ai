import logging
from typing import Optional
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.tools.newspaper_tools import NewspaperTools
from app.models.schemas import UnifiedResponse,FinancialNews,PriceData

logger = logging.getLogger(__name__)

class AgentService:
    def __init__(self):
        try:
            self.multi_ai_agent = self._create_agents()
            logger.info("Successfully initialized multi-agent system")
        except Exception as e:
            logger.error(f"Failed to initialize agents: {str(e)}")
            raise RuntimeError(f"Agent initialization failed: {str(e)}")

    def _create_agents(self) -> Agent:
        try:
            base_model = Gemini(id="gemini-1.5-flash")
            
            news_agent = Agent(
                name="Financial News Specialist",
                role="Track and analyze latest financial news",
                model=base_model,
                tools=[DuckDuckGo(),NewspaperTools()],
                instructions=[
                    "For the given stock symbol:",
                    "1. Search for and collect the 5 most recent relevant news articles",
                    "2. For each article:",
                    "   - Extract the complete, unmodified title",
                    "   - Capture the FULL source URL:",
                    "     * Must begin with http:// or https://",
                    "     * Include complete domain and path",
                    "     * Preserve all query parameters",
                    "     * Do not truncate or modify the URL",
                    "     * Verify URL resolves to actual article page",
                    "   - Write a 2-3 sentence summary of key points",
                    "   - Record publication date in YYYY-MM-DD format",
                    "3. Validate each article entry:",
                    "   - Confirm URL is complete and accessible",
                    "   - Test URL resolves to news article",
                    "   - Verify date is within last 30 days",
                    "4. Return exactly 5 articles as JSON array",
                    "5. Double-check URL fields contain complete links",
                    "6. Output pure JSON without markdown"
                ],
                structured_response=True,
                response_model=FinancialNews,
                markdown=True
            )

            price_agent = Agent(
                name="Market Data Analyst",
                role="Track real-time market data",
                model=base_model,
                tools=[
                    YFinanceTools(
                        stock_price=True,
                        stock_fundamentals=True,
                        company_news=True,
                        analyst_recommendations=True
                    )
                ],
                instructions=[
                    "For the given stock symbol:",
                    "1. Fetch current market data including:",
                    "   - Latest price and currency",
                    "   - Price change (absolute and percentage)",
                    "   - Trading volume",
                    "   - Market capitalization",
                    "   - Exchange information",
                    "2. Format all numerical values appropriately",
                    "3. Include timestamp of data retrieval",
                    "4. Handle different exchanges correctly (NSE/NYSE/NASDAQ)",
                    "5. Return data in strict JSON format",
                    "6. Output only valid JSON, without any markdown formatting"
                ],
                structured_response=True,
                response_model=PriceData,
                markdown=True
            )

            analysis_agent = Agent(
                name="Investment Analyst",
                role="Provide comprehensive stock analysis",
                model=base_model,
                tools=[
                    YFinanceTools(
                        stock_price=True,
                        stock_fundamentals=True,
                        analyst_recommendations=True
                    ),
                    DuckDuckGo()
                ],
                instructions=[
                    "For the given stock symbol:",
                    "1. Perform technical analysis including:",
                    "   - Price trends and patterns",
                    "   - Support and resistance levels",
                    "   - Volume analysis",
                    "   - Key technical indicators",
                    "2. Conduct fundamental analysis covering:",
                    "   - Financial ratios",
                    "   - Growth metrics",
                    "   - Competitive position",
                    "3. Assess risks across market, company, and industry",
                    "4. Provide clear buy/hold/sell recommendation",
                    "5. Include specific price targets",
                    "6. Return analysis in strict JSON format",
                    "7. Output only valid JSON, without any markdown formatting"
                ],
                structured_response=True,
                markdown=True
            )

            multi_agent = Agent(
                teams=[news_agent, price_agent, analysis_agent],
                model=base_model,
                instructions=[
                    "You are a coordinator that combines responses from three specialized agents:",
                    "1. Financial News Agent - provides latest news articles",
                    "2. Price Agent - provides current market data",
                    "3. Analysis Agent - provides technical and fundamental analysis",
                    "For any stock symbol:",
                    "- Collect responses from all three agents",
                    "- Format them into a single JSON response",
                    "- Ensure all data is properly nested under respective sections",
                    "- Verify all URLs in news section are complete and valid",
                    "- Do not use markdown formatting or code blocks",
                    "- Output only valid JSON"
                ],
                structured_response=True,
                response_model=UnifiedResponse,
                markdown=True
            )
            return multi_agent

        except Exception as e:
            logger.error(f"Error creating agents: {str(e)}")
            raise

    async def get_stock_analysis(self, symbol: str) -> UnifiedResponse:
        try:
            logger.info(f"Fetching analysis for symbol: {symbol}")
            response = self.multi_ai_agent.run(symbol)
            
            # Ensure response matches UnifiedResponse schema
            if isinstance(response, dict):
                return UnifiedResponse(**response)
            elif hasattr(response, 'content'):
                # Handle case where response is wrapped in a RunResponse
                if isinstance(response.content, UnifiedResponse):
                    return response.content
                elif isinstance(response.content, dict):
                    return UnifiedResponse(**response.content)
            
            raise ValueError("Invalid response format from agent")
        except Exception as e:
            logger.error(f"Error analyzing stock {symbol}: {str(e)}")
            raise RuntimeError(f"Failed to analyze stock {symbol}: {str(e)}")