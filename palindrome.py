import scrapy


class Palindromes(scrapy.Spider):
    name = "palindromes"
    start_urls = [
        'https://en.wiktionary.org/wiki/Appendix:English_palindromes'
    ]

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        for word in response.selector.xpath('//li/i/a/text()').extract():
            yield {
                'word': word
            }
