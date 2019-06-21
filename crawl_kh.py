from test import Snake

# from pprint import pprint
# main_page_content = Snake().main_page_content()
# menu_urls = Snake().get_urls_main_menu(main_page_content)

all_content = {
    "product_page_newproducts_1": Snake().page_content_to_soup("https://www.khanoumi.com/newproducts#sort_3")}
pages = all_content["product_page_newproducts_1"].find("div", {"id": "bdyno12_pages"})
number_page = pages.find_all("a").__len__()

for num in range(2, number_page + 1):
    print(num)
    all_content[f"product_page_newproducts_{num}"] = Snake().page_content_to_soup(
                Snake.base_url + "newproducts" + f"#paging_{num}/")
