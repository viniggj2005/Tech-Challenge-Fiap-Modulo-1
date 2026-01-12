import re
import requests
from typing import List
from bs4 import BeautifulSoup
from app.schemas.book import BookModel
from app.services.data_service import array_to_csv
from app.schemas.scraping import ScrapedLinkAndCategory


BASE_URL = "https://books.toscrape.com"
rating = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}


def scraping_trigger(link: str):
    content = get_web_content(link)
    categories = get_category_and_his_link(content)
    books = get_books(categories)
    array_to_csv(books)
    return content


def get_link_without_page(link):
    return re.split("index.html", link)[0]


def get_web_content(url: str) -> str:
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    return soup.prettify()


def get_category_and_his_link(content):
    result = []
    soup = BeautifulSoup(content, "html.parser")
    for item in soup.find_all(class_=["nav nav-list"]):
        for li in item.ul.find_all("li"):
            result.append(
                {
                    "link": get_link_without_page(li.a["href"]),
                    "category": li.get_text(strip=True),
                }
            )
    return result


def get_books(content=List[ScrapedLinkAndCategory]):
    books_array: List[BookModel] = []
    for scraped in content:
        first_page_content = get_web_content(f"{BASE_URL}/{scraped['link']}index.html")
        books_array += get_book_content(first_page_content, scraped["category"])
        for item in BeautifulSoup(first_page_content, "html.parser").find_all(
            "li", class_="current"
        ):
            pages = re.findall(r"\d+", item.get_text(strip=True))
            if pages:
                for index in range(2, int(pages[-1]) + 1):
                    page_content = get_web_content(
                        f"{BASE_URL}/{scraped['link']}page-{index}.html"
                    )
                    books_array += get_book_content(page_content, scraped["category"])
    books_array = [{**row, "id": index + 1} for index, row in enumerate(books_array)]
    return books_array


def get_book_content(content, category) -> List[BookModel]:
    books = []
    for item in BeautifulSoup(content, "html.parser").find_all(
        "li", class_=["col-xs-6 col-sm-4 col-md-3 col-lg-3"]
    ):
        image = BASE_URL + re.sub(r"^.*(?=/media)", "", item.img["src"])
        title = item.h3.get_text(strip=True)
        price = float(
            item.find(class_="price_color").get_text(strip=True).replace("£", "")
        )
        availability = item.find(class_="instock availability").get_text(strip=True)
        rate = item.find(class_="star-rating")["class"][-1]
        books.append(
            {
                "image": image,
                "title": title,
                "price": price,
                "availability": availability,
                "rate": rating.get(rate.lower()),
                "category": category,
            }
        )
    return books
