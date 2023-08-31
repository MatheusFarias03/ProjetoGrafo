from bs4 import BeautifulSoup
import requests
import json

class RappiWebScraper:

    def __init__(self):
        self.url_rappi = "https://www.rappi.com.br"
        self.url_supermarkets = self.url_rappi + "/lojas/tipo/supermercados"
        self.url_restaurants = self.url_rappi + "/restaurantes"
        self.html_content = None
        self.wholesalers_links = []
        self.wholesalers_names = []
        self.restaurants_links = []
        self.restaurants_names = []

    def get_wholesalers_links(self):
        try:
            # Send a GET request to the page.
            self.html_content = requests.get(self.url_supermarkets)

            # Use BeautifulSoup to parse the HTML content.
            soup = BeautifulSoup(self.html_content.text, 'html.parser')

            divs_tag = soup.find_all('div')
            header_2_tag = soup.find_all('h2')

            # Find the header tag that contains 'Atacados'.
            for tag in header_2_tag:
                if 'Atacados' in tag.string:
                    atacado_header = tag

            # Find all <a> tags with the specified class.
            target_class = "sc-dedb9a4b-0 cGxdzt"
            for div in divs_tag:
                if atacado_header in div:
                    a_tags_with_class = div.find_all('a', class_=target_class)

            # Collect the "href"s from each <a> tag
            for a_tag in a_tags_with_class:
                href_value = self.url_rappi + a_tag.get("href")
                self.wholesalers_links.append(href_value)

            print('Wholesalers links have been successfully retrieved.')

        except Exception as e:
            print(f'Error: {e}.')


    def get_wholesalers_names(self):
        if len(self.wholesalers_links) != 0:
            try:
                # For each site, send a GET request and scrap it.
                for link in self.wholesalers_links:
                    self.html_content = requests.get(link)
                    soup = BeautifulSoup(self.html_content.text, 'html.parser')

                    # Find the name of the wholesaler.
                    wholesaler_name = soup.find("h1", {"data-qa":"store-name"})
                    wholesaler_name = wholesaler_name.get_text()
                    self.wholesalers_names.append(wholesaler_name)

                    print(f'\nWebsite: {link} \nWholesaler Name: {wholesaler_name}')

            except Exception as e:
                print(f'Error: {e}.')


rappi_scraper = RappiWebScraper()
print(rappi_scraper)
rappi_scraper.get_wholesalers_links()
rappi_scraper.get_wholesalers_names()
