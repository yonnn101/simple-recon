import requests
print("DIR SCAN")
# Set the target URL and the wordlist file path
read = open("created_files/full_url.txt","r")
target_url = read.read()
wordlist_file = input("Enter a wordlist: ")

# Read the wordlist file
with open(wordlist_file, "r") as file:
    wordlist = file.read().splitlines()

# Perform directory scanning
total_directories = len(wordlist)
scanned_directories = 0

for directory in wordlist:
    # Construct the URL to check
    url = target_url + directory

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the response status code is not 404
    if response.status_code != 404:
        print(f"Directory found: {url}")

    # Update progress
    scanned_directories += 1
    progress = (scanned_directories / total_directories) * 100
    print(f"Progress: {progress:.2f}% ({scanned_directories}/{total_directories})")