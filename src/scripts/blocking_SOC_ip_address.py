
# ===== main script for blocking IP address from SOC report

from imports import *

from pathlib import Path

from validating_ip_input import valid_ip
from creating_address_object import creating_address_objects
from adding_object_to_group import adding_object_to_the_group
from commit_configuration import commit_function
from send_email import sending_email

project_root = Path(__file__).resolve().parent.parent.parent
load_dotenv(project_root / ".env") 


ips = sys.argv[1:]  # list of IP addresses from input

for ip in ips:

    valid_ip(ip)

bad_IPs = project_root / "data" / "bad_ips.txt"
with open(f"{bad_IPs}", "a") as f:
    for item in ips:
        f.write(item + "\n")



log_file = project_root / "logs" / "firewall_logs.log"
logging.basicConfig(filename=f'{log_file}', level=logging.INFO)


with open(f"{project_root}/config/fw_credentials.json") as f:
    firewalls = json.load(f)


for fw in firewalls:

    ip_env = fw.get("ip_env")
    username_env = fw.get("username_env")
    pass_env = fw.get("password_env")


    fw["ip"] = os.getenv(ip_env)
    fw["user"] = os.getenv(username_env)
    fw["password"] = os.getenv(pass_env)

    firewall_host = fw["ip"]
    username =  fw["user"]
    password = fw["password"]
   
    firewall = Firewall(firewall_host, username, password)
    
    address_groups = AddressGroup.refreshall(firewall) 

    address_group_name = "Malicious_IP_addresses"  

    address_objects = AddressObject.refreshall(firewall)
 

    created_address_objects = creating_address_objects(firewall, ips)
    
    for address_object in created_address_objects:
       adding_object_to_the_group(firewall, address_group_name, address_object)
 
    commit_function(firewall)

    sending_email()