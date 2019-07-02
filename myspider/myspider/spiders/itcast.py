# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.cn']
    start_urls = ['https://www.amazon.cn/s?k=shu&i=software&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&ref=nb_sb_noss_2']

    def parse(self, response):
        fname=response.xpath('//div[@class="sg-col-inner"]//span[@class="a-size-medium a-color-base a-text-normal"]/text()').extract()
        fprice=response.xpath('//div[@class="sg-col-inner"]//span[@class="a-offscreen"]/text()').extract()
        print (fname,fprice)
        item=[",".join(item) for item in zip(fname,fprice)]
        for item in zip(fname,fprice):
            yield {
                "商品：":item[0],"价格：":item[1]
            }
