import scrapy
#'https://www.amazon.com/dp/B07FZ8S74R?ref=ods_ucc_echo_B07FZ8S74R_rc_nd_ucc&th=1'
#to run this code, cd into the root folder and then provide the following commands to the terminal: scrapy crawl text
# scrapy crawl text -o myFileNameHere.json
class TextSpider(scrapy.Spider):
    name = "text"


    def start_requests(self):
        # tell it which website(s) to visit
        urls = ['https://www.amazon.com/gp/product/0813526140?pf_rd_r=RQSVMXY45Q0RN3P31Z04&pf_rd_p=edaba0ee-c2fe-4124-9f5d-b31d6b1bfbee',\
                'https://www.amazon.com/Darkness-Biographical-Introduction-Joseph-Conrad-ebook/dp/B000FC1C50/ref=sr_1_1?dchild=1&keywords=hear+of+darkness&qid=1598187842&sr=8-1', \
                'https://www.amazon.com/Rudyard-Kipling-Complete-Works-ebook/dp/B079YWS8NL/ref=cm_cr_arp_d_pl_foot_top?ie=UTF8']

        # urls = ['https://www.amazon.com/Rudyard-Kipling-Complete-Works-ebook/dp/B079YWS8NL/ref=cm_cr_arp_d_pl_foot_top?ie=UTF8']

        # visit each url
        for url in urls:
            # at each url, run the ‘parse’ function
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # for book in response.css('article.product_pod'):
        #     # get the title from the nested <a> link object inside the <h3> object
        #     yield {
        #         # 'rating': book.css('p::text').get(),
        #         'title': book.css('h3 a::text').get(),
        #         'price': book.css('div.product_price p.price_color::text').get()
        #     }

        for review in response.css('span.a-size-base.review-text'):
            # get the title from the nested <a> link object inside the <h3> object
            yield {
                # 'rating': book.css('p::text').get(),
                'title': review.css('div.review-text-content span::text').get(),
                # 'price': book.css('div.product_price p.price_color::text').get()
            }

        #set a filename to write the response to
        filename = 'amazon_review_heart.html'
        with open(filename, "wb") as f:
            f.write(response.body)
        # self.log('Saved file % s' % filename)
