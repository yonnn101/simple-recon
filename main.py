# This is the main page
import urllib.request
print("My RECON")
# checking url format and existence
def check_URL():
    url = input("Enter url(http(s)://example.com): ")
    # write the url for other file to access
    text_url=open("created_files/full_url.txt","w")
    text_url.write(url)
    try:
        try:
            response = urllib.request.urlopen(url)
            status_code = response.getcode()
            status_codes = [
                200, 301, 302, 304, 400, 401, 403, 404, 500, 503
            ]
            if status_code in status_codes:
                print("URL exists.")
        except urllib.error.HTTPError as e:
            print("URL exists")

    except :
        print("Give appropriate URL.")
        check_URL()
check_URL()
def option(choose):

    if choose == 1:
        import port_scan
    elif choose == 2:
        import subdomain
    elif choose == 3:
        import web_crawler
    elif choose == 4:
        import web_links
    elif choose == 5:
        import dir_scan
    elif choose == 6:
        import dns_enumeration
    elif choose ==99:
        exit()
    else:
        print("invalid input")
print("""   1.port scan
    2.subdomain
    3.web crawler
    4.web links
    5.dir scan
    6.DNS enumeration
    99. EXIT
    """)
choice = int(input("ENTER a number: "))

while choice !=99:
    option(choice)
