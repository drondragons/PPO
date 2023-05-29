from requests import Session
from bs4 import BeautifulSoup
from functions import Functions


DEFAULT_URL = 'https://example.org/'
DEFAULT_CULTURE_URL = 'https://www.culture.ru'

DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
DEFAULT_HEADERS = {'User-Agent': DEFAULT_USER_AGENT}


class Scrapper:
    DEFAULT_PARSER = 'html.parser'

    def __init__(self, url=DEFAULT_URL, headers=DEFAULT_HEADERS):
        self.baseurl = url
        self.session = Session()
        self.session.headers.update(headers)
        

class ScrapperCultureRU(Scrapper):
    def __init__(self, url=DEFAULT_CULTURE_URL, headers=DEFAULT_HEADERS):
        super().__init__(url, headers)       


    def get_pages_amount(self, subdir):
        response = self.session.get(self.baseurl + subdir)

        pages = 1
        soup = BeautifulSoup(response.text, self.DEFAULT_PARSER)
        pagination = soup.find('nav', class_='pagination')
        if pagination:
            pages = int(pagination.find_all('a')[-1].text)

        return pages


    def get_page_entities_urls(self, entities):
        return [DEFAULT_CULTURE_URL + entity.find('a', class_='card-cover')['href'] for entity in entities]
        

    def get_entities_urls(self, subdir):
        items_urls = list()
        
        url = self.baseurl + subdir
        pages = self.get_pages_amount(subdir.format(page=1)) + 1
        for page in range(1, pages):
            response = self.session.get(url.format(page=page))
            
            soup = BeautifulSoup(response.text, self.DEFAULT_PARSER)
            soup = soup.find_all('div', class_='entity-cards_item col')
            items_urls.extend(self.get_page_entities_urls(soup))
            items_urls = list(set(items_urls))
            
        return items_urls


    def get_entity_header(self, soup):
        header = soup.find('h1', class_='about-entity_title entity-title').text
        return Functions.replace_html_symbols(header)
    
    
    def get_paragraphs(self, soup):
        annotation = str()
        for paragraph in soup:
            annotation += paragraph.text + '\\n'
        return Functions.replace_html_symbols(annotation)
    

    def get_entity_annotation(self, soup):
        content_body = soup.find('div', class_='styled-content_body')
        return self.get_paragraphs(content_body.find_all('p'))


    def get_entity_attribute(self, soup, entity_attribute):
        value = list()
        attributes = soup.find_all('div', class_='attributes_block')
        for attribute in attributes:
            label = attribute.find('div', class_='attributes_label').text
            if label == entity_attribute:
                value = attribute.find_all(class_='attributes_value')
                value = [Functions.replace_html_symbols(el.text) for el in value]
                break
            
        return value
