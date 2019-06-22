from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException, WebDriverException
from bs4 import BeautifulSoup
import requests


# somelist[:] = filterfalse(determine, somelist)


class Snake:
    base_url = "https://www.khanoumi.com/"

    # def __init__(self):

    @staticmethod
    def page_content_to_soup(url):
        driver = webdriver.Firefox()
        try:
            driver.get(url)
        except(NoSuchWindowException, WebDriverException):
            driver.quit()
        page_content = driver.execute_script("return document.documentElement.innerHTML")
        soup = BeautifulSoup(page_content, 'html.parser')
        driver.quit()
        driver.quit()
        return soup

    # def get_current_page_state_urls(self):
    #     return .find_elements_by_css_selector(".un.paging")

    def get_urls_main_menu(self, main_page_content):
        menu_urls = []
        discount_urls = {}
        for ul in main_page_content.find_all("ul"):
            if ul.attrs.get("id") == "hdr4_mnu":
                for li in ul.find_all("li"):
                    for div in li.find_all("div"):
                        for li_2 in div.find_all("li"):
                            menu_urls.append(li_2.find_previous("a"))
        for urls in menu_urls:
            if urls.text == "محصولات جدید":
                discount_urls["newproducts"] = urls.get("href")
            if urls.text == "تخفیف های روز":
                discount_urls["discount"] = urls.get("href")
            if urls.text == "پرطرفدارها":
                discount_urls["topfavorites"] = urls.get("href")
            if urls.text == "شانس 10:10":
                discount_urls["specialsaleland"] = urls.get("href")
            if urls.text == "بومرنگ":
                discount_urls["boomerang"] = urls.get("href")
            if urls.text == "مناسب هدیه":
                discount_urls["weekbestsellers"] = urls.get("href")
            if urls.text == "پرفروش های خانومی":
                discount_urls["gift"] = urls.get("href")
        return discount_urls

    @staticmethod
    def main_page_content():
        base_url = "https://www.khanoumi.com/"
        req = requests.get(base_url)
        soup = BeautifulSoup(req.text, 'html.parser')
        return soup

# pages_numbers_section = soup.find("div", {"id": "bdyno12_pages"})
# driver.find_element_by_class_name("mfp-close").click()
#
# current_page = 1
# for n in get_current_page_state_url():
#     if int(n.text) == current_page:
#         driver.refresh()
#         get_current_page_state_url().remove(n)
#         current_page += 1
#     else:
#         n.click()
#
# for n in get_current_page_state_url():
#     print(n.text, type(n.text))

