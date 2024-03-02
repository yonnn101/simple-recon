import requests
print("SUB DOMAIN ENUMERATION")
def enumerate_subdomains(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url)
        if response.status_code == 200:
            subdomains = set()
            data = response.json()
            for entry in data:
                subdomains.add(entry['name_value'].strip())
            print(f"Subdomains for {domain}:")
            for subdomain in subdomains:
                print(subdomain)
        else:
            print("Failed to fetch data from crt.sh")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    domain = input("Enter the domain to enumerate subdomains: ")
    enumerate_subdomains(domain)
