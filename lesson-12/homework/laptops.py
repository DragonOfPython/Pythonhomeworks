import requests
from bs4 import BeautifulSoup
import json

# Function to scrape laptop data from the Demoblaze website
def scrape_laptops(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    laptops = []
    laptop_items = soup.find_all('div', class_='col-lg-4')
    
    for item in laptop_items:
        name = item.find('a', class_='hrefch').text
        price = item.find('h5').text.split('Price: ')[-1]
        description = item.find('p').text
        
        laptop = {
            'name': name,
            'price': price,
            'description': description
        }
        
        laptops.append(laptop)
    
    return laptops

# URL of the Demoblaze Laptops section
url = 'https://demoblaze.com/index.html#/'

# Scraping laptop data and storing it in JSON format
laptops_data = scrape_laptops(url)

# Saving the extracted information in a structured JSON format
with open('laptops_data.json', 'w') as f:
    json.dump(laptops_data, f, indent=4)

print("Laptop data scraped and saved in 'laptops_data.json'")