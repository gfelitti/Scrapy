# -*- coding: utf-8 -*-
import scrapy


class ChaquenteSpider(scrapy.Spider):
    name = "chaquente"
    allowed_domains = ["http://chaquente.com"]
    start_urls = (
        'http://www.http://chaquente.com/',
    )

    def parse(self, response):
        pass
