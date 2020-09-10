import scrapy
#from coverbrowser.items import CoverItem


class AmazonScraper(scrapy.Spider):
    name = "amazon"

    start_urls = ["https://www.amazon.com/Darkness-Biographical-Introduction-Joseph-Conrad-ebook/product-reviews/B000FC1C50/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"]

    def parse(self, response):
        nextpageurl = response.xpath(
            '//li[@class="a-last"]/a/@href').get()
        print('next page url: ', nextpageurl)
        for item in self.scrape(response):
            yield item

        if nextpageurl:
            nextpage = response.urljoin(nextpageurl)
#            print("Found url: {}".format(nextpage))
            yield scrapy.Request(nextpage, callback=self.parse)

    def scrape(self, response):
         for review in response.css('span.a-size-base.review-text'):
            # get the title from the nested <a> link object inside the <h3> object
            yield {
                'text': review.css('span.review-text-content span::text').get()
            }


        #set a filename to write the response to
#        filename = 'amazon_review_heart.html'
#        with open(filename, "wb") as f:
#            f.write(response.body)
