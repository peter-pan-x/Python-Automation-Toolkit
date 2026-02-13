"""
Web Scraper Utility

A powerful, reusable web scraper using requests and BeautifulSoup.
Supports proxies, retries, and clean data extraction.

Author: Peter
"""

import requests
from bs4 import BeautifulSoup
import logging
import time
import random

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class WebScraper:
    def __init__(self, headers=None, proxies=None):
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.proxies = proxies

    def fetch(self, url, retries=3):
        """Fetch content from a URL with retry logic."""
        attempt = 0
        while attempt < retries:
            try:
                response = requests.get(url, headers=self.headers, proxies=self.proxies, timeout=10)
                response.raise_for_status()
                logging.info(f"Successfully fetched {url}")
                return response.text
            except requests.RequestException as e:
                attempt += 1
                logging.warning(f"Attempt {attempt} failed for {url}: {e}")
                time.sleep(random.uniform(1, 3))
        
        logging.error(f"Failed to fetch {url} after {retries} attempts.")
        return None

    def parse_html(self, html):
        """Parse HTML content with BeautifulSoup."""
        if not html:
            return None
        return BeautifulSoup(html, "html.parser")

    def extract_links(self, soup):
        """Extract all links from a parsed page."""
        if not soup:
            return []
        return [a.get("href") for a in soup.find_all("a", href=True)]

# Example Usage
if __name__ == "__main__":
    scraper = WebScraper()
    url = "https://example.com"
    content = scraper.fetch(url)
    if content:
        soup = scraper.parse_html(content)
        links = scraper.extract_links(soup)
        print(f"Found {len(links)} links on {url}")
