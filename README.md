# 🤖 AI-Powered Crypto Trading Bot

## 📌 Overview
This project is an **automated trading bot** that analyzes crypto price trends and **executes buy/sell trades using AI models**. It integrates with **Binance API** to fetch real-time market data and execute trades.

## 🚀 Features
- ✅ **Real-Time Market Analysis** – Fetches live crypto prices.
- ✅ **AI-Powered Trading Signals** – Uses **ML models** to predict buy/sell points.
- ✅ **Automated Trading Execution** – Places trades using **Binance API**.
- ✅ **Risk Management** – Implements **stop-loss and take-profit strategies**.
- ✅ **Trade Logging & Dashboard** – Stores **trade history & profit tracking**.
- ✅ **Docker Support** – Deploy using Docker.

## 🏗️ Tech Stack
- **Backend:** Python (FastAPI)  
- **Trading API:** Binance API  
- **Machine Learning:** Scikit-learn, RandomForest, LSTM  
- **Database:** SQLite/PostgreSQL  
- **Deployment:** Docker & Kubernetes  

## 📂 Project Structure
```
├── trading_bot/
│   ├── main.py
│   ├── trading_service.py
│   ├── strategy.py
│   ├── model.py
│   ├── database.py
│   ├── config.py
│   ├── requirements.txt
├── ml_model/
│   ├── train_model.py
│   ├── backtesting.py
│   ├── trading_dataset.csv
├── docker-compose.yml
├── README.md
```

## 🛠️ Setup & Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/AI-Powered-Crypto-Trading-Bot.git
cd AI-Powered-Crypto-Trading-Bot
```

### **2️⃣ Set Up Binance API Keys**
Create a `.env` file and add your **Binance API keys**:
```ini
BINANCE_API_KEY=your_api_key_here
BINANCE_SECRET_KEY=your_secret_key_here
```

### **3️⃣ Run the Trading Bot (FastAPI)**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### **4️⃣ Train the AI Model (Optional)**
```bash
cd ml_model
python train_model.py
```

### **5️⃣ Run Everything Using Docker (Recommended)**
```bash
docker-compose up --build
```

## 📡 API Endpoints (FastAPI)
| Method | Endpoint         | Description              |
|--------|-----------------|--------------------------|
| GET    | `/balance`      | Fetches Binance account balance |
| POST   | `/trade`        | Executes an AI-based trade |

### **Example API Request**
```json
POST /trade
{
  "symbol": "BTCUSDT",
  "trade_type": "BUY",
  "quantity": 0.01
}
```
#### **Example API Response**
```json
{
  "message": "Trade Executed Successfully!",
  "price": 48950.75,
  "quantity": 0.01
}
```

## 📝 Future Enhancements
- 📈 **Live Web Dashboard for Trade Monitoring**  
- 🤖 **AI Model Improvements (LSTM, Reinforcement Learning)**  
- 💰 **Multi-Crypto Support for Trading**  

---


🚀 **Like this project? Star it on GitHub!** ⭐  
