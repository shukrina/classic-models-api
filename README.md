# Week 2: ClassicModels REST API

This project is a high-performance REST API built with FastAPI and PostgreSQL, featuring a 4-layer clean architecture and concurrent processing.

## 🚀 Setup Instructions
1. Clone the repo: `git clone <your-url>`
2. Create a `.env` file (refer to the `.env.example` provided).
3. Start the database: `docker-compose up -d`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the API: `uvicorn app.main:app --reload`

## 🛠 Tech Stack
- **FastAPI**: Web Framework
- **SQLAlchemy**: ORM for database interaction
- **PostgreSQL**: Database
- **Docker**: Containerization
- **Pydantic**: Data validation

## 📝 Reflections (Twelve-Factor App)
### Factor III: Config
Storing credentials in `.env` ensures security... (add your 200 words here)

### Factor VIII: Concurrency
We used `asyncio.gather` to retrieve counts from 8 tables simultaneously... (add your 200 words here)

### Factor X: Dev/Prod Parity
Docker ensures that... (add your 200 words here)
