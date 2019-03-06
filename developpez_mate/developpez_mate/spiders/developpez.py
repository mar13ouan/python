
import scrapy

class DevelopppezSpryder(scrapy.spider):
    name = 'forum-python-developpez'

    start_urls = ['https://www.developpez.net/forums/f938/dotnet/general-dotnet/debuter/']

    def parse(self, response):
        for fil_discussion in response.css('#threads .inner'):
            yield(
                'titre': fil_discussion.css('.threadtitle a::text').extract_first()
            ) 
                
            