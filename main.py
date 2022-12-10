import io
import requests
from bs4 import BeautifulSoup
from datetime import date
url = "https://tass.ru/"
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 Atom/25.0.0.20"
}
def save_html(url):
    s = requests.Session()
    resp = s.get(url=url, headers=headers, timeout=3)

    with io.open("index.html", "w", encoding="utf-8") as f:
        f.write(resp.text)
def get_pars():
    news_dict = []
    with io.open("index.html", encoding="utf-8", ) as f:
        file = f.read()
    soup = BeautifulSoup(file, "lxml")
    all_new = soup.findAll("div", id="content_box")
    for item in all_new:
        s = item.find_all('span')
        h = item.find_all("a", href=True)
        for k, j in zip(h, s):
            u = k.get("href")
            span = j.get_text(strip=True)
            news_dict.append({
                "url": u if "http" in u else "https://tass.ru" + u,
                "conted": span
            })
    save_pars(news_dict)
def save_pars(tet):
    with io.open("save.txt", "a", encoding="utf-8") as f:
        for i in tet:
            print(f"URL: {i['url']}, | contend:{i['conted']}")
            f.write(f"URL: {i['url']}, |  contend:{i['conted']}" + "\n")
    print(date.today())


if __name__ == "__main__":
    save_html(url)
    get_pars()

