# ClassicModels Enterprise REST API

A high-performance, scalable backend system built with **FastAPI** and **PostgreSQL**. This project demonstrates enterprise-level software engineering practices, including a 4-layer clean architecture, containerization, and asynchronous concurrency.

## 🚀 Overview
This API provides full CRUD (Create, Read, Update, Delete) capabilities for the classic `ClassicModels` relational database, which includes 8 interconnected tables (Customers, Orders, Products, Employees, etc.). 

The project is built following the **Twelve-Factor App** methodology to ensure portability, security, and performance.

## 🛠 Tech Stack
*   **Framework:** FastAPI (Python)
*   **Database:** PostgreSQL
*   **ORM:** SQLAlchemy
*   **Validation:** Pydantic
*   **Environment:** Docker & Docker Compose
*   **Concurrency:** Asyncio

## 🏗 Architecture
The project follows a **4-Layer Clean Architecture** to ensure separation of concerns and maintainability:
1.  **Database Layer (`database.py` & `models.py`):** Manages the engine connection and SQLAlchemy ORM models.
2.  **Schema Layer (`/schemas`):** Uses Pydantic models for strict data validation and request/response serialization.
3.  **Logic Layer (`/crud`):** Contains reusable business logic and database queries.
4.  **API Layer (`/routers`):** Handles HTTP requests, routing, and response status codes.

## ⚡ Key Features
*   **Automated Initialization:** Database and tables are automatically created and seeded upon Docker startup using `seed.sql`.
*   **High-Performance Aggregation:** An `/overall_counts` endpoint leverages **Factor VIII (Concurrency)** via `asyncio.gather()` to query 8 tables simultaneously, minimizing latency.
*   **Strict Validation:** Pydantic validators ensure data integrity (e.g., validating email formats and ensuring `requiredDate` is after `orderDate`).
*   **Comprehensive Logging:** Centralized logging tracks every request, database operation, and performance metric.

## 🚦 Getting Started

### Prerequisites
*   Docker & Docker Compose
*   Python 3.10+ (for local testing)

### Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/shukrina/classic-models-api.git
   cd classic-models-api
