from bs4 import BeautifulSoup
import requests
import json
from Graph import *

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


    def get_wholesalers_vertices(self, id_num:int):
        
        wholesalers_vertices = []
        
        self.get_wholesalers_links()
        
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
                    
                    # Create a vertex for the wholesaler.
                    wholesaler_vertex = Vertex(id=id_num, properties={'name': wholesaler_name, 'link': link}, label="Wholesaler")
                    wholesalers_vertices.append(wholesaler_vertex)
                    id_num += 1
                    
                print("Wholesalers vertices have been successfully created.")

            except Exception as e:
                print(f'Error: {e}.')
        
        else:
            print("Wholesalers list empty!")
        
        return wholesalers_vertices
    
    
    def get_wholesalers_fish(self, wholesalers_vertices, id_num:int, graph:Graph):
        
        filtered_elements = []
        
        if len(wholesalers_vertices) != 0:
            try:
                for v in wholesalers_vertices:
                    fish_link = v.properties['link'] + '/acougue-e-peixaria/peixes'
                    self.html_content = requests.get(fish_link)
                    soup = BeautifulSoup(self.html_content.text, 'html.parser')
                    
                    # Find all the div elements with 'data-qa' attribute set to 'product-item-' to get each item.
                    div_elements = soup.find_all('div')
                    for div in div_elements:
                        data_qa = div.get('data-qa', '')
                        if data_qa.startswith('product-item-'):
                            filtered_elements.append(div)
                    
                    # Loop through the filtered divs and retrieve each property.
                    for div in filtered_elements:
                        product_name = div.find('h3', {'data-qa': 'product-name'}).get_text()
                        product_price = div.find('span', {'data-qa': 'product-price'}).get_text()
                        product_pum = div.find('span', {'data-qa': 'product-pum'}).get_text()
                        product_description = div.find('span', {'data-qa': 'product-description'}).get_text()
                    
                        product = Vertex(id=id_num, properties={'name': product_name, 
                                                                'description': product_description, 
                                                                'price': product_price},
                                         label='Product')
                        
                        graph.add_vertex(product)
                        id_num += 1
                        edge_v_product = Edge(id=id_num, from_vertex=v, to_vertex=product, properties={}, label='OFFERS')
                        id_num += 1
                        graph.add_edge(edge_v_product)
                            
                print("Some fish were caught!")
            
            except Exception as e:
                print(f'Error {e}.')
                
        else:
            print("Wholesalers list empty!")

            
            