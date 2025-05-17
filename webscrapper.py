from playwright.sync_api import sync_playwright
import sys


def scrap_web(url: str|None, search: str) -> None:
    url = "https://unsplash.com/s/photos/"
    
    try:
        with sync_playwright() as pr:
            browser = pr.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(f"{url}{search}")
            page.wait_for_selector("figure")
            content = page.content()
            browser.close()

        with open("temp.html", "w", encoding="utf-8") as f:
            f.write(content)

        print("Scraping successful!")

    except Exception as e:
        print("Scraping failed:", e)



if __name__ == "__main__":
    search_term = sys.argv[1] if len(sys.argv) > 1 else "flower"
    scrap_web(url = None, search = search_term)
    print(f"Scraped and saved as 'temp.html'")