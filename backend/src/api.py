from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper.config import *

# DATABASE_URL = config("DATABASE_URL")
# SECRET_KEY = config("SECRET_KEY")


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/api/data")
async def get_data():
    return {"data": [1, 2, 3, 4, 5]}
