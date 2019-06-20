import scrapy


class BlogSpider(scrapy.Spider):
    name = 'khanoumi'

    def start_requests(self):
        urls = [
            'https://www.khanoumi.com/newproducts#sort_3'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-1]

        filename = f'khanoumi_{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f"Saved file {filename}")



    # for title in response.css('.post-header>h2'):
    #     yield {'title': title.css('a ::text').get()}
    #
    # for next_page in response.css('a.next-posts-link'):
