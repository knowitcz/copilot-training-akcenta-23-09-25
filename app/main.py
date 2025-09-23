from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.db import SQLModel, engine
from app.api.account_routes import router as account_router
from app.api.bank_routes import router as bank_router
from app.startup import create_default_accounts

SQLModel.metadata.create_all(bind=engine)

app = FastAPI()

# Serve index.html from the static directory
@app.get("/")
def serve_static_files():
    return FileResponse("resources/static/index.html")

app.include_router(account_router, prefix="/api/v1", tags=["account"])
app.include_router(bank_router, prefix="/api/v1", tags=["bank"])

create_default_accounts()