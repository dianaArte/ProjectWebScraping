from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import productos

class list():
        contador = []

class MercadoLibreCrawler(CrawlSpider):
    """Metodo para insertar en la base de datos la lista de productos"""
    name = 'mercadoLibre'

    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
      'CLOSESPIDER_PAGECOUNT': 5 # Numero maximo de paginas en las cuales voy a descargar items. Scrapy se cierra cuando alcanza este numero
    }

    # Utilizamos 2 dominios permitidos, ya que los articulos utilizan un dominio diferente
    allowed_domains = ['listado.mercadolibre.com.ar', 'mercadolibre.com.ar']

    start_urls = ['https://listado.mercadolibre.com.ar/celular-smarphones#D[A:celular%20smarphones]']

    download_delay = 1

    # Tupla de reglas
    rules = (
        Rule( # REGLA #1 => HORIZONTALIDAD POR PAGINACION
            LinkExtractor(
                allow=r'/_Desde_\d+' # Patron en donde se utiliza "\d+", expresion que puede tomar el valor de cualquier combinacion de numeros
            ), follow=False),
        Rule( # REGLA #2 => VERTICALIDAD AL DETALLE DE LOS PRODUCTOS
            LinkExtractor(
                allow=r'/samsung-' 
            ), follow=False, callback='parse_items'), # Al entrar al detalle de los productos, se llama al callback con la respuesta al requerimiento
    )
    
    

    def parse_items(self, response):
        
        cont = list()

        item = {}
        
        item['name'] = response.xpath( '//h1/text()').get()
        item['price'] = response.xpath( '//span[@class="price-tag-fraction"]/text()').get().replace('.','')
        item['full'] = response.xpath( '//svg[@class="ui-pdp-icon ui-pdp-icon--full"]/p/text()').get()
        item['store'] = response.xpath( '//span[@class="ui-pdp-seller__label-sold"]/text()').get()
        item['quantity'] = response.xpath( '//span[@class="ui-pdp-buybox__quantity__available"]/text()').get()
        item['size'] = response.xpath( '//p[@class="ui-pdp-family--REGULAR ui-vpp-highlighted-specs__discrete-bar__title"]/span[@class="ui-pdp-color--BLACK ui-pdp-size--XSMALL ui-pdp-family--SEMIBOLD"]/text()').get().replace(' "','')
        item['memory'] = response.xpath( '//p[@class="ui-pdp-family--REGULAR ui-vpp-highlighted-specs__key-value__labels__key-value"]/span[@class="ui-pdp-color--BLACK ui-pdp-size--XSMALL ui-pdp-family--SEMIBOLD"]/text()').get()

        val = cont.contador.append(item['name'])
        
        item['id'] = int(len(cont.contador))

        #Se envia los datos a insertar
        productos.insertarProductos(item)

        


        
