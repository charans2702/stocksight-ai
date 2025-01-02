import { useState } from 'react';
import { Search, TrendingUp, DollarSign, Newspaper, BarChart2, ArrowUp, ArrowDown } from 'lucide-react';
import { Alert, AlertTitle } from '@/components/ui/alert';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const StockAnalysis = () => {
  const [symbol, setSymbol] = useState('');
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchStockData = async () => {
    if (!symbol) {
      setError('Please enter a stock symbol');
      return;
    }
    
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch(`http://localhost:8000/api/v1/stock/${symbol}`);
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to fetch stock data');
      }
      const result = await response.json();
      setData(result.stock_data);
    } catch (err) {
      setError(err.message || 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetchStockData();
  };

  const getPriceColor = (value) => {
    return value >= 0 ? 'text-emerald-600' : 'text-rose-600';
  };

  return (
    <div className="h-screen bg-gradient-to-br from-slate-900 to-slate-800 p-4">
      <div className="h-full max-w-7xl mx-auto grid grid-rows-[auto,1fr] gap-4">
        {/* Search Bar */}
        <div className="w-full">
          <form onSubmit={handleSubmit} className="flex gap-4 items-center bg-slate-700/50 p-4 rounded-xl backdrop-blur-sm border border-slate-600">
            <Search className="text-slate-400" />
            <input
              type="text"
              value={symbol}
              onChange={(e) => setSymbol(e.target.value.toUpperCase())}
              placeholder="Enter stock symbol (e.g., TSLA)"
              className="flex-1 bg-transparent border-none outline-none text-lg text-white placeholder-slate-400"
            />
            <button
              type="submit"
              disabled={loading}
              className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50 transition-colors"
            >
              {loading ? 'Loading...' : 'Analyze'}
            </button>
          </form>
        </div>

        {error && (
          <Alert variant="destructive" className="absolute top-20 left-1/2 transform -translate-x-1/2">
            <AlertTitle>{error}</AlertTitle>
          </Alert>
        )}

        {data && (
          <div className="grid grid-cols-12 gap-4 h-full">
            {/* Left Column */}
            <div className="col-span-8 grid grid-rows-[auto,1fr] gap-4">
              {/* Price Cards */}
              <div className="grid grid-cols-4 gap-4">
                <Card className="bg-slate-700/50 border-slate-600 backdrop-blur-sm">
                  <CardContent className="p-4">
                    <div className="text-slate-400 text-sm">Last Price</div>
                    <div className="text-2xl font-bold text-white flex items-center gap-2">
                      ${data.price_data.last_price}
                      <ArrowUp className="text-emerald-500 h-4 w-4" />
                    </div>
                  </CardContent>
                </Card>
                <Card className="bg-slate-700/50 border-slate-600 backdrop-blur-sm">
                  <CardContent className="p-4">
                    <div className="text-slate-400 text-sm">High</div>
                    <div className="text-2xl font-bold text-white">${data.price_data.high}</div>
                  </CardContent>
                </Card>
                <Card className="bg-slate-700/50 border-slate-600 backdrop-blur-sm">
                  <CardContent className="p-4">
                    <div className="text-slate-400 text-sm">Low</div>
                    <div className="text-2xl font-bold text-white">${data.price_data.low}</div>
                  </CardContent>
                </Card>
                <Card className="bg-slate-700/50 border-slate-600 backdrop-blur-sm">
                  <CardContent className="p-4">
                    <div className="text-slate-400 text-sm">Volume</div>
                    <div className="text-2xl font-bold text-white">{data.price_data.volume.toLocaleString()}</div>
                  </CardContent>
                </Card>
              </div>

              {/* Technical & Fundamental Analysis */}
              <div className="grid grid-cols-2 gap-4">
                <Card className="bg-slate-700/50 border-slate-600 backdrop-blur-sm">
                  <CardHeader className="pb-2">
                    <CardTitle className="flex items-center gap-2 text-white">
                      <BarChart2 className="text-blue-400" />
                      Technical Analysis
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="grid grid-cols-2 gap-4">
                      <div className="bg-slate-600/50 p-3 rounded-lg">
                        <div className="text-sm text-slate-400">50 MA</div>
                        <div className="text-lg font-semibold text-white">${data.analysis.technical.moving_average_50}</div>
                      </div>
                      <div className="bg-slate-600/50 p-3 rounded-lg">
                        <div className="text-sm text-slate-400">200 MA</div>
                        <div className="text-lg font-semibold text-white">${data.analysis.technical.moving_average_200}</div>
                      </div>
                    </div>
                    <div className="mt-4 text-sm text-slate-300">{data.analysis.technical.Description}</div>
                  </CardContent>
                </Card>

                <Card className="bg-slate-700/50 border-slate-600 backdrop-blur-sm">
                  <CardHeader className="pb-2">
                    <CardTitle className="flex items-center gap-2 text-white">
                      <TrendingUp className="text-blue-400" />
                      Fundamental Analysis
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="grid grid-cols-2 gap-4">
                      <div className="bg-slate-600/50 p-3 rounded-lg">
                        <div className="text-sm text-slate-400">P/E Ratio</div>
                        <div className="text-lg font-semibold text-white">{data.analysis.fundamental.pe_ratio}</div>
                      </div>
                      <div className="bg-slate-600/50 p-3 rounded-lg">
                        <div className="text-sm text-slate-400">EPS</div>
                        <div className="text-lg font-semibold text-white">${data.analysis.fundamental.eps}</div>
                      </div>
                    </div>
                    <div className="mt-4 text-sm text-slate-300">{data.analysis.fundamental.Description}</div>
                  </CardContent>
                </Card>
              </div>
            </div>

            {/* Right Column - News Feed */}
            <div className="col-span-4">
              <Card className="bg-slate-700/50 border-slate-600 backdrop-blur-sm h-full">
                <CardHeader>
                  <CardTitle className="flex items-center gap-2 text-white">
                    <Newspaper className="text-blue-400" />
                    Latest News
                  </CardTitle>
                </CardHeader>
                <CardContent className="h-[calc(100%-5rem)] overflow-auto custom-scrollbar">
                  <div className="space-y-3">
                    {data.financial_news.map((news, index) => (
                      <a
                        key={index}
                        href={news.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="block p-3 bg-slate-600/50 rounded-lg hover:bg-slate-500/50 transition-colors"
                      >
                        <div className="font-medium text-white">{news.headline}</div>
                        <div className="text-sm text-slate-400 mt-1">
                          {news.source} • {news.date}
                        </div>
                      </a>
                    ))}
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        )}
      </div>

      <style jsx global>{`
        .custom-scrollbar::-webkit-scrollbar {
          width: 8px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: rgba(148, 163, 184, 0.1);
          border-radius: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: rgba(148, 163, 184, 0.5);
          border-radius: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: rgba(148, 163, 184, 0.7);
        }
      `}</style>
    </div>
  );
};

export default StockAnalysis;