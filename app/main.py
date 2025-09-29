from fastapi import FastAPI
from app.routers import test, auth, expenses  # , reports

app = FastAPI()

# Register routers
app.include_router(test, prefix="/test", tags=["Test"])
app.include_router(auth, prefix="/auth", tags=["Auth"])
app.include_router(expenses, prefix="/expenses", tags=["Expenses"])
# app.include_router(reports.router, prefix="/reports", tags=["Reports"])