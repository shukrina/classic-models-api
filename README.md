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
Hardcoding passwords or API keys is a major security risk because once code is committed to version control (like Git), those secrets are visible to anyone with access and are nearly impossible to erase from history.
•Using .env files keeps sensitive data out of your repository.
•Additionally, it allows you to change settings for different environments (like moving from a local test database to a production one) without ever touching the actual source code.

### Factor VIII: Concurrency
In this task, I implemented Factor VIII by moving from sequential processing to concurrent processing using asyncio. Sequential processing acts like a single cashier; it forces each database query to wait for the previous one to finish, creating a bottleneck. By using asyncio.gather, I treatedthe API like a bank with multiple cashiers, allowing the system to handle all 8 table counts simultaneously. This significantly reduces the total response time for the dashboard.
Furthermore, by combining this with Factor II (Dependencies) and Factor IV (Backing Services), the application remains scalable. If the database grows or we switch from PostgreSQL to another service, our modular CRUD functions and concurrent architecture ensure that the API remains high-performing without needing a total rewrite. This setup demonstrates how modern cloud-native applications handle high loads by efficiently utilizing system resources rather than staying idle while waiting for external database responses.

### Factor X: Dev/Prod Parity
Docker creates a consistent "container" that includes the exact same operating system, libraries, and dependencies regardless of where it runs. By using the same Docker image in development and production, you eliminate the "it works on my machine" syndrome.It ensures that if the code passes tests on a developer's laptop, it will behave identically in the production environment.
