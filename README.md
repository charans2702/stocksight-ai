# StockSight AI 🚀

StockSight AI is a comprehensive stock analysis platform that combines multi-agent AI systems with real-time market data to provide detailed insights, news analysis, and trading recommendations. The platform features both a FastAPI backend for intelligent stock analysis and a modern React frontend for data visualization.

## 🌟 Features

- **Real-time Stock Analysis**
  - Live price tracking
  - Technical indicators
  - Fundamental analysis
  - Trading volume metrics

- **Multi-Agent AI System**
  - Financial News Specialist
  - Market Data Analyst
  - Investment Analysis Expert

- **Modern React Dashboard**
  - Interactive stock charts
  - Real-time price updates
  - News feed integration
  - Technical analysis visualization
  - Responsive design with dark mode

## 🔧 Tech Stack

### Backend
- FastAPI
- Python 3.8+
- Phi Framework
- Google Gemini AI
- YFinance Tools
- DuckDuckGo API
- Newspaper3k

### Frontend
- React
- Tailwind CSS
- Recharts
- Lucide Icons
- ShadcnUI Components

## 📋 Prerequisites

- Python 3.8 or higher
- Node.js 14.0 or higher
- Google API Key
- Phi API Key
- Internet connection for real-time data

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/charans2702/stocksight-ai.git
cd stocksight-ai
```

2. **Set up backend environment**
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
```

3. **Configure environment variables**
```env
GOOGLE_API_KEY=your_google_api_key
PHI_API_KEY=your_phi_api_key
```

4. **Set up frontend**
```bash
cd frontend
npm install
```

## 🏃‍♂️ Running the Application

1. **Start the backend server**
```bash
# From the root directory
python main.py
```
The API will be available at `http://localhost:8000`

2. **Start the frontend development server**
```bash
# From the frontend directory
npm run dev
```
The web interface will be available at `http://localhost:3000`

## 📚 API Documentation

Once the backend is running, access the API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔰 Project Structure

```
stocksight-ai/
├── app/
│   ├── api/
│   │   └── endpoints/
│   │       └── stock.py
│   ├── models/
│   │   └── schemas.py
│   └── services/
│       ├── agent_service.py
│       └── stock_service.py
├── stock-analysis-ui/
│   
├── config.py
├── main.py
└── requirements.txt
```

## 🛠️ Configuration

The application uses environment variables for configuration. Create a `.env` file in the root directory with the following variables:

```env
GOOGLE_API_KEY=your_google_api_key
PHI_API_KEY=your_phi_api_key
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments

- [Phi Framework](https://github.com/phidata)
- [Google Gemini AI](https://cloud.google.com/vertex-ai)
- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://reactjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)