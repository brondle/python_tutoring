import scrapy
import time
#from coverbrowser.items import CoverItem
#to run this program, cd into the directory then in the terminal write: scrapy crawl amazon -o myFileNameHere.json
#the name of the file is the third item in the request to the terminal 'amazon' in other example it is 'text'


class AmazonScraper(scrapy.Spider):
    name = "amazon"

    start_urls = ["https://www.amazon.com/Darkness-Biographical-Introduction-Joseph-Conrad-ebook/product-reviews/B000FC1C50/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"]


    def parse(self, response):
        #check for "next" page button
        nextpageurl = response.xpath(
            '//li[@class="a-last"]/a/@href').get()
        print('next page url: ', nextpageurl)
        for item in self.scrape(response):
            yield item

        if nextpageurl:
            time.sleep(5)
            #adding next page to our stack of pages
            nextpage = response.urljoin(nextpageurl)
#            print("Found url: {}".format(nextpage))
            #recursively call this function on that page
            yield scrapy.Request(nextpage, callback=self.parse)

    def scrape(self, response):
        # CODE FOR SCRAPING "ALL REVIEWS"
        for review in response.css('span.a-size-base.review-text'):
            # get the title from the nested <a> link object inside the <h3> object
            yield {
                'text': review.css('span.review-text-content span::text').get()
            }
        # ORIGINAL CODE FOR MAIN BOOK PAGE
        # for review in response.css('span.a-size-base.review-text'):
        #     #get the title from the nested <a> link object inside the <h3> object
        #        yield {
        #            # 'rating': book.css('p::text').get(),
        #            'title': review.css('div.review-text-content span::text').get(),
        #            # 'price': book.css('div.product_price p.price_color::text').get()
        #            # 'title': review.css('div.review-text-content span::text').get(),
        #
        #        }

            #set a filename to write the response to
        filename = 'amazon_review_heart_original.html'
        with open(filename, "wb") as f:
            f.write(response.body)



