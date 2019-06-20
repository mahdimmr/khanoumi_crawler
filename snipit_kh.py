import requests
from pprint import pprint
from bs4 import BeautifulSoup

base_url = "https://www.khanoumi.com/"
req = requests.get(base_url)

soup = BeautifulSoup(req.text, 'html.parser')


"""
Get the list of all <a> in main menu with option without the title
"""
for ul in soup.find_all("ul"):
    if ul.attrs.get("id") == "hdr4_mnu":
        for li in ul.find_all("li"):
            for div in li.find_all("div"):
                for li_2 in div.find_all("li"):
                    for a in li_2.find_all("a"):
                        print(a)


"""
Get the list of all <a> in main menu with option with the title
"""
for ul in soup.find_all("ul"):
    if ul.attrs.get("id") == "hdr4_mnu":
        for li in ul.find_all("li"):
            for div in li.find_all("div"):
                for li_2 in div.find_all("li"):
                    print(li_2.find_previous("a"))


"""
Get the specific url that has 
"""
for ul in soup.find_all("ul"):
    if ul.attrs.get("id") == "hdr4_mnu":
        for li in ul.find_all("li"):
            for div in li.find_all("div"):
                for li_2 in div.find_all("li"):
                    if li_2.find_previous("a").text == "محصولات جدید":
                        new_product_ulr = li_2.find_previous("a").get("href")


"""
Get the specific url that has discount and insert into a dict 
"""
menu_urls = []
discount_urls = {}
for ul in soup.find_all("ul"):
    if ul.attrs.get("id") == "hdr4_mnu":
        for li in ul.find_all("li"):
            for div in li.find_all("div"):
                for li_2 in div.find_all("li"):
                    menu_urls.append(li_2.find_previous("a"))
for urls in menu_urls:
    if urls.text == "محصولات جدید":
        discount_urls[urls.text] = urls.get("href")
    if urls.text == "تخفیف های روز":
        discount_urls[urls.text] = urls.get("href")
    if urls.text == "پرطرفدارها":
        discount_urls[urls.text] = urls.get("href")
    if urls.text == "شانس 10:10":
        discount_urls[urls.text] = urls.get("href")
    if urls.text == "بومرنگ":
        discount_urls[urls.text] = urls.get("href")
pprint(discount_urls)


# class Client(QWebPage):
#
#     def __init__(self, url):
#         self.app = QApplication(sys.argv)
#         QWebPage.__init__(self)
#         self.loadFinished.connect(self.on_page_load)
#         self.mainFrame().load(QUrl(url))
#         self.app.exec_()
#
#     def on_page_load(self):
#         self.app.quit()
#
#
# url = 'https://www.khanoumi.com/newproducts#sort_3'
# client_response = Client(url)
# source = client_response.mainFrame().toHtml()
# soup = BeautifulSoup(source, 'html.parser')
# test = soup.find("div", {"id": "bdyno12_product"})
