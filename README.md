# FastAPI Scraper

This project is a web scraping tool using FastAPI to scrape product data from [website](https://dentalstall.com/shop/).

## Setup

1.Will Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    uvicorn app.main:app --reload
    ```


## Usage

- Start the FastAPI server and use the `/scrape/` endpoint to initiate scraping.
