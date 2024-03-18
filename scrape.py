import requests
from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text

def scrape_website(url):

    # Handle invalid URLs
    if not url.startswith('http'):
        url = 'http://' + url

    # Send a request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from the body of the web page
    # This will include all text within the body tag
    text = soup.body.get_text(separator=' ', strip=True)

    return text

def scrape_resume(resume):
   return extract_text(resume)
