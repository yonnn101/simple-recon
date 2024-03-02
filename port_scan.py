import subprocess
import json
print("PORT SCANING")
# Reading the url from the file that created by main,py file
read = open("created_files/full_url.txt", "r")
URL = read.read()
# extract the domain name form the full URL
domain_name = URL.split('/')[2]

def rustscan(url):
    # run rustscan comand and store on file to pass for the nmap scan
    command2 = ["rustscan", domain_name, "-o", "json", ">", "rustscan.json"]
    try:
        subprocess.check_output(command2, shell=True, universal_newlines=True)
        print("open ports")
        with open("created_files/rustscan.json", "r") as file:
            json_data = json.load(file)
        ports = [port["port"] for port in json_data["ports"]]
        for port in ports:
            print(port)
    except subprocess.CalledProcessError as e:
        print("Command execution failed. Error:", e)

def nmap_scan(url):
        command = ["nmap", domain_name, "-sV","-oN","created_files/nmap_scan.txt", "-p"]
        # passing port to nmap scan to speed up nmap

        with open("created_files/rustscan.json", "r") as file:
            json_data = json.load(file)

        # Extract the port numbers
        ports= [port["port"] for port in json_data["ports"]]

            # Print the extracted port numbers
        for port in ports:
            command.append(str(port))

        # run nmap scan with  version scanning argument
        try:
            output = subprocess.check_output(command, shell=True, )
            print("Session completed successfully the output saved in 'created_files/nmap_scan.txt'")
        except subprocess.CalledProcessError as e:
            print("Command execution failed. Error:", e)

print("Domain name: " +'"'+domain_name+'"')

print("""
1. Scan for open ports
2. Scan the port more
3. Exit
""")
user_input = int(input(">>"))
if user_input == 1:
    rustscan(URL)
elif user_input == 2:
    nmap_scan(URL)
elif user_input == 3:
    import main
