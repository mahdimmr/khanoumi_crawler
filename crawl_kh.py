from snake import Snake
from pprint import pprint

# paint(number_page)


main_page_content = Snake().main_page_content()
menu_urls = Snake().get_urls_main_menu(main_page_content)
all_content = {}

for url in menu_urls.keys():
    print("urls", menu_urls.get(url))
    print("url_key", url.title())
    u = menu_urls.get(url)
    if u.startswith("http"):
        u = menu_urls.get(url)
    else:
        u = f"https://www.khanoumi.com{menu_urls.get(url)}"

    all_content[f"{url.title()}_first_page"] = Snake().page_content_to_soup(u)


    # for num in range(2, number_page + 1):
    #     print(num)
    #     all_content[f"product_page_newproducts_{num}"] = Snake().page_content_to_soup(
    #         Snake.base_url + "newproducts" + f"#paging_{num}/")
    # ges = all_content["product_page_newproducts_1"].find("div", {"id": "bdyno12_pages"})
    # number_page = pages.find_all("a")
    # pr
