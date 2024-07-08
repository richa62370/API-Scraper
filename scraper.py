import httpx
from typing import Optional, List
from models.product import Product
import json
import asyncio

class Scraper:
    def __init__(self, page_limit: Optional[int] = None, proxy: Optional[str] = None):
        self.page_limit = page_limit
        self.proxy = proxy
        self.base_url = "https://dentalstall.com/shop/"
        self.headers = {"User-Agent": "Mozilla/5.0"}

    async def fetch_page(self, client, url: str):
        response = await client.get(url, headers=self.headers, proxies=self.proxy)
        response.raise_for_status()
        return response.text

    async def scrape(self) -> List[Product]:
        products = []
        async with httpx.AsyncClient() as client:
            page = 1
            while True:
                if self.page_limit and page > self.page_limit:
                    break
                url = f"{self.base_url}?page={page}"
                page_content = await self.fetch_page(client, url)
                # Parse the page content and extract product details
                # For now, let's just simulate with dummy data
                products.append(Product(product_title="Dummy", product_price=100.0, path_to_image="/path/to/image"))
                page += 1
        self.save_to_json(products)
        return products

    def save_to_json(self, products: List[Product]):
        data = [product.dict() for product in products]
        with open("products.json", "w") as f:
            json.dump(data, f, indent=4)

# Add more methods for retry mechanism, caching, etc.
