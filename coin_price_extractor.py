import bs4
import requests


class CoinPriceExtractor:
    def __init__(self, pages):
        self.url = "https://coinmarketcap.com/?page={page_number}"
        self.pages = pages

    def extract(self, page):
        html_data = requests.get(self.url.format(page_number=page)).content
        s = bs4.BeautifulSoup(html_data, "html.parser")

        result = {}
        for currency in s.find_all("tbody")[0].find_all("tr"):
            currency_price = currency.find_all("td")[3].find("span").get_text().replace(",", "")
            currency_name = currency.find_all("a", {'class': 'cmc-link'})[0]['href'].split('/')[2]
            result[currency_name] = currency_price.split("$")[1]
        return result
    
    def extract_all_pages(self):
        result = {}
        for page in self.pages:
            result = result | self.extract(page)
        return result
        

