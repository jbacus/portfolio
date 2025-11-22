#!/usr/bin/env python3
"""
Simple web scraper for bacus.org
Saves HTML content from specified pages
"""

import requests
from pathlib import Path
import time
import json

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

# Headers to mimic a real browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Cache-Control': 'max-age=0',
}

def scrape_pages():
    """Scrape all pages and save to output directory"""
    output_dir = Path('scraped_content')
    output_dir.mkdir(exist_ok=True)

    results = {}

    for url in PAGES:
        print(f"Scraping {url}...")
        try:
            response = requests.get(url, headers=HEADERS, timeout=30)

            if response.status_code == 200:
                # Save HTML
                page_name = url.split('/')[-1] or 'index'
                html_file = output_dir / f"{page_name}.html"
                html_file.write_text(response.text, encoding='utf-8')

                results[url] = {
                    'status': 'success',
                    'file': str(html_file),
                    'size': len(response.text)
                }
                print(f"  ✓ Saved to {html_file} ({len(response.text)} bytes)")
            else:
                results[url] = {
                    'status': 'failed',
                    'status_code': response.status_code
                }
                print(f"  ✗ Failed with status {response.status_code}")

            # Be polite, wait between requests
            time.sleep(2)

        except Exception as e:
            results[url] = {
                'status': 'error',
                'error': str(e)
            }
            print(f"  ✗ Error: {e}")

    # Save summary
    summary_file = output_dir / 'summary.json'
    summary_file.write_text(json.dumps(results, indent=2))
    print(f"\nSummary saved to {summary_file}")

    return results

if __name__ == '__main__':
    print("Starting scraper...")
    results = scrape_pages()

    success_count = sum(1 for r in results.values() if r['status'] == 'success')
    print(f"\nCompleted: {success_count}/{len(PAGES)} pages scraped successfully")
