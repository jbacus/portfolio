# Web Scraper for bacus.org

Two scraper options to get around bot protection:

## Option 1: Simple Scraper (Fast)

Uses standard HTTP requests. May not work if the site has strong bot protection.

```bash
# Install dependencies
pip install -r requirements.txt

# Run the scraper
python simple_scraper.py
```

## Option 2: Browser-Based Scraper (Recommended)

Uses Playwright to control a real browser. This should bypass most bot detection.

```bash
# Install dependencies
pip install -r requirements.txt

# Install browser binaries
playwright install chromium

# Run the scraper
python browser_scraper.py
```

The browser-based scraper will:
- Open a visible browser window (so you can see what's happening)
- Save full HTML of each page
- Take full-page screenshots
- Allow you to manually solve any CAPTCHAs if needed

## Output

Both scrapers create a `scraped_content/` directory with:
- HTML files for each page
- Screenshots (browser scraper only)
- `summary.json` with scraping results

## Customization

Edit the `PAGES` list in either script to add/remove URLs to scrape.

For headless mode (no visible browser), change `headless=False` to `headless=True` in `browser_scraper.py`.
