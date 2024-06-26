import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import wget

def download_file(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_name = os.path.join(folder, url.split('/')[-1]) + ".midi"
    wget.download(url, file_name)
    print(f"Downloaded {file_name}")

def get_all_links_from_div(url, selector):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find(selector)
    if not div:
        raise ValueError(f"No div with id '{selector}' found.")
    links = div.find_all('a', href=True)
    return [urljoin(url, link['href']) for link in links]

def get_midi_links_from_page(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    midi_links = [urljoin(url, link['href']) for link in links if '/download/mid/' in link['href']]
    return midi_links

def scrape(base_url, selector):
    links = get_all_links_from_div(base_url, selector)
    for link in links:
        folder_name = link.split('/')[-1].split('.')[0]
        print(f"Processing {link}...")
        midi_links = get_midi_links_from_page(link)
        for midi_link in midi_links:
            download_file(midi_link, folder_name)

base_url = ''  
selector = 'main'
scrape(base_url, selector)
