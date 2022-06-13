from scrapy.spiders import Spider
from scrapy.item import Field
from scrapy.item import Item
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader


class Pelicula(Item):
    aid = Field()
    titulo = Field()
    rating = Field()
    director = Field()
    descripcion = Field()


class IMDbCrawler(Spider):
    name = "imdb"
    start_urls = [
        "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"]

    def limpiarTexto(self, texto):
        nuevoTexto = texto.replace("\n", " ").replace("\r", " ").replace("\t", " ").strip()
        return nuevoTexto

    def parse(self, response):
        sel = Selector(response)
        peliculas = sel.xpath('//div[@class="lister-list"]/div')

        for i, elem in enumerate(peliculas):
            item = ItemLoader(Pelicula(), elem)
            item.add_value("aid", i)
            item.add_xpath("titulo", './/h3/a/text()')
            item.add_xpath("rating", './/strong/text()')
            item.add_xpath("director", './/p[contains(.,"Director")]/a[1]/text()')
            item.add_xpath("descripcion", './/p[@class="text-muted"]/text()', MapCompose(self.limpiarTexto))

            yield item.load_item()
