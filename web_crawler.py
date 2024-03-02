import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
print("WEB CRAWLER")
# Set the target URL to crawl
read = open("created_files/full_url.txt", "r")
target_url = read.read()
# Set the maximum number of pages to crawl
try:
    max_pages = int(input("Enter maximum number of pages to crawl(Default = 5): "))
except:
    max_pages = 5

# Set the set of crawled URLs
crawled_urls = set()

def crawl(url):
    # Check if the maximum number of pages has been reached
    if len(crawled_urls) == max_pages:
        return

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the base URL
    base_url = urlparse(url).netloc

    # Find all the links on the page
    links = soup.find_all('a')

    # Process each link
    for link in links:
        href = link.get('href')

        # If the link has an href attribute
        if href:
            # Normalize the URL by joining it with the base URL
            absolute_url = urljoin(url, href)

            # Check if the URL belongs to the same domain
            if urlparse(absolute_url).netloc == base_url:
                # Check if the URL has not been crawled before
                if absolute_url not in crawled_urls:
                    # Add the URL to the set of crawled URLs
                    crawled_urls.add(absolute_url)

                    # Print the absolute URL
                    print(absolute_url)

                    # Recursively crawl the absolute URL
                    crawl(absolute_url)

# Start crawling from the target URL
crawl(target_url)