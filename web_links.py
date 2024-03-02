import requests
from bs4 import BeautifulSoup
print("WEB LINKS")
def extract_links(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the links on the page
    links = soup.find_all('a')

    # Extract and print the href attribute of each link
    for link in links:
        href = link.get('href')
        print(href)

# Specify the URL of the website to extract links from
read = open("created_files/full_url.txt", "r")
website_url = read.read()
# Call the function to extract links from the website
extract_links(website_url)