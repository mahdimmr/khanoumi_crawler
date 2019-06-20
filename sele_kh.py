from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Firefox()
driver.get("https://www.khanoumi.com/newproducts#sort_3")
page_content = driver.execute_script("return document.documentElement.innerHTML")
driver.quit()

soup = BeautifulSoup(page_content, 'html.parser')

print(soup.find("div", {"id": "bdyno12_product"}))

# print(page_content)

