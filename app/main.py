import asyncio
import time
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Import our other layers
from . import crud, models, schemas, database, logging_config
from .routers import (
    product_router,
    productline_router,
    office_router,
    employee_router,
    order_router,
    orderdetail_router,
    payment_router
)

# Initialize the logger
logger = logging_config.logger

app = FastAPI(title="Concurrency Dashboard API")

# ... registering it ...
app.include_router(product_router.router, prefix="/products", tags=["Products"])
app.include_router(productline_router.router, prefix="/productlines", tags=["ProductLines"])
app.include_router(office_router.router, prefix="/offices", tags=["Offices"])
app.include_router(employee_router.router, prefix="/employees", tags=["Employees"])
app.include_router(order_router.router, prefix="/orders", tags=["Orders"])
app.include_router(orderdetail_router.router, prefix="/orderdetails", tags=["OrderDetails"])
app.include_router(payment_router.router, prefix="/payments", tags=["Payments"])

@app.get("/")
def root():
    return {"message": "ClassicModels API is running!"}

