import requests
from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text

def scrape_website(url):

    if not url.startswith('http'):
        url = 'http://' + url

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    text = soup.body.get_text(separator=' ', strip=True)

    return text

def scrape_resume(resume):
   return extract_text(resume)
