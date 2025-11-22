#!/usr/bin/env python3
"""
Browser-based scraper using Playwright for JavaScript-rendered content
This will act like a real browser and should bypass most bot detection
"""

import asyncio
from pathlib import Path
import json
from playwright.async_api import async_playwright

# Pages to scrape
PAGES = [
    'https://bacus.org/john-bacus',
    'https://bacus.org/about-me-1',
    'https://bacus.org/datastructure',
    'https://bacus.org/curriculum-design',
    'https://bacus.org/expansive-help-tip',
    'https://bacus.org/trimble-connect',
    'https://bacus.org/design-foundations',
    'https://bacus.org/3d-warehouse',
    'https://bacus.org/pochade-box',
    'https://bacus.org/skpr',
]

async def scrape_with_browser():
    """Scrape pages using a real browser (Playwright)"""
    output_dir = Path('scraped_content')
    output_dir.mkdir(exist_ok=True)

    results = {}

    async with async_playwright() as p:
        # Launch browser (use chromium)
        browser = await p.chromium.launch(headless=False)  # Set to True for headless mode
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        )

        page = await context.new_page()

        for url in PAGES:
            print(f"Scraping {url}...")
            try:
                # Navigate to page
                await page.goto(url, wait_until='networkidle', timeout=30000)

                # Wait a bit for any dynamic content
                await page.wait_for_timeout(2000)

                # Get the page content
                html_content = await page.content()

                # Save HTML
                page_name = url.split('/')[-1] or 'index'
                html_file = output_dir / f"{page_name}.html"
                html_file.write_text(html_content, encoding='utf-8')

                # Take screenshot
                screenshot_file = output_dir / f"{page_name}.png"
                await page.screenshot(path=str(screenshot_file), full_page=True)

                results[url] = {
                    'status': 'success',
                    'html_file': str(html_file),
                    'screenshot': str(screenshot_file),
                    'size': len(html_content)
                }
                print(f"  ✓ Saved HTML and screenshot")

                # Wait between requests
                await page.wait_for_timeout(2000)

            except Exception as e:
                results[url] = {
                    'status': 'error',
                    'error': str(e)
                }
                print(f"  ✗ Error: {e}")

        await browser.close()

    # Save summary
    summary_file = output_dir / 'summary.json'
    summary_file.write_text(json.dumps(results, indent=2))
    print(f"\nSummary saved to {summary_file}")

    return results

async def main():
    print("Starting browser-based scraper...")
    print("This will open a browser window - you may need to manually solve any CAPTCHAs")
    print()

    results = await scrape_with_browser()

    success_count = sum(1 for r in results.values() if r['status'] == 'success')
    print(f"\nCompleted: {success_count}/{len(PAGES)} pages scraped successfully")

if __name__ == '__main__':
    asyncio.run(main())
