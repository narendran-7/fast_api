from requests import get
from bs4 import BeautifulSoup as soup

class FindRate:
    def __init__(self):

        self.gold_url   = "https://www.goodreturns.in/gold-rates/"
        self.silver_url = "https://www.goodreturns.in/silver-rates/"
        self.platinum_url = "https://www.goodreturns.in/platinum-price.html"

    def getSource(self,url):
        req = get(url)
        soup_obj = soup(req.content, "lxml")
        
        sp = soup_obj.find_all("tr", {"class":"odd_row"})[0]
        return sp.findNext('td').findNext('td').contents[1]

    def gold(self):
        return float(self.getSource(self.gold_url).replace(',','.'))

    def silver(self):
        return float(self.getSource(self.silver_url))

    def platinum(self):
        return float(self.getSource(self.platinum_url).replace(',','.'))

if __name__ == "__main__":
    getRate = FindRate()
    print(getRate.gold())
    print(getRate.silver())
    print(getRate.platinum())