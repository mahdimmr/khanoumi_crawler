from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get("https://www.khanoumi.com/newproducts#sort_3")
page_content = {"0": driver.execute_script("return document.documentElement.innerHTML")}
print(page_content.__len__())

soup = BeautifulSoup(page_content["0"], 'html.parser')
pages_numbers_section = soup.find("div", {"id": "bdyno12_pages"})
all_a_in_pages_numbers_section = pages_numbers_section.find_all("a").__len__()


for num_of_page in range(2, all_a_in_pages_numbers_section+1):
    driver.get(f"https://www.khanoumi.com/newproducts#paging_{num_of_page}")
    page_content[str(num_of_page)] = driver.execute_script("return document.documentElement.innerHTML")
    print(page_content.__len__())


for page_key in page_content.keys():
    soup = BeautifulSoup(page_content[page_key], 'html.parser')
    product_section = soup.find("div", {"id": "bdyno12_product"})
    product_section.find_all("div", {"class": "item"})


driver.quit()


result_product = {}
result_data = []
for page_key in page_content.keys():
    soup = BeautifulSoup(page_content[page_key], 'html.parser')
    product_section = soup.find("div", {"id": "bdyno12_product"})
    products_items = product_section.find_all("div", {"class": "item"})
    item_link = ""
    item_picture = ""
    item_title = ""