import dns.resolver
print("DNS ENUMERATION")
def dns_enum(domain):
    try:
        answers = dns.resolver.resolve(domain, 'ANY')

        a_records = [answer.address for answer in answers if answer.rdtype == dns.rdatatype.A]
        print(f"A Records for {domain}: {a_records}")

        mx_records = [answer.exchange.to_text() for answer in answers if answer.rdtype == dns.rdatatype.MX]
        print(f"MX Records for {domain}: {mx_records}")

        ns_records = [answer.to_text() for answer in answers if answer.rdtype == dns.rdatatype.NS]
        print(f"NS Records for {domain}: {ns_records}")

        txt_records = [answer.to_text() for answer in answers if answer.rdtype == dns.rdatatype.TXT]
        print(f"TXT Records for {domain}: {txt_records}")

    except dns.resolver.NoAnswer:
        print(f"No DNS records found for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain '{domain}' does not exist")
    except dns.resolver.NoNameservers:
        print("No nameservers found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    domain = "google.com"
    dns_enum(domain)
