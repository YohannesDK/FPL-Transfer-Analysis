from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper.src.scrapers.PremierLeagueScraper import PremierLeagueScraper



app = FastAPI()
prem_scraper = PremierLeagueScraper()

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
    return prem_scraper.scrape().to_json()

