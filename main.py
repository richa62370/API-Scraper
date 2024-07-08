from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from scraping.scraper import Scraper
from config import TOKEN

app = FastAPI()

# Authentication dependency
def get_token_header(token: str):
    if token != TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

class ScrapeSettings(BaseModel):
    page_limit: Optional[int] = None
    proxy: Optional[str] = None

@app.post("/scrape/", dependencies=[Depends(get_token_header)])
async def scrape(settings: ScrapeSettings):
    scraper = Scraper(settings.page_limit, settings.proxy)
    result = await scraper.scrape()
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
