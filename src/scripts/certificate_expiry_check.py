# ===== finding all certificates on the firewall that expired within the 30 days
# ===== printing name and the date when certificate expires 

import panos
import ipdb
import os
import sys
import logging
import datetime
import requests
from ipaddress import ip_address, IPv4Address, IPv6Address
from panos.firewall import Firewall
from panos.objects import AddressObject,  AddressGroup
from dotenv import load_dotenv
from datetime import datetime
import xml.etree.ElementTree as ET
import re
import json
from pathlib import Path
from datetime import timedelta




project_root = Path(__file__).resolve().parent.parent.parent
load_dotenv(project_root / ".env") 



log_file = project_root / "logs" / "firewall_logs.log"
logging.basicConfig(filename=f'{log_file}', level=logging.INFO)

logging.info(f"Script for checking certifications expiration is running {datetime.now()}")

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
    #info = firewall.op('show system info', xml=True)
    #info = firewall.op('show system info')
    info = firewall.op('show sslmgr-store config-certificate-info', xml=True)
    text = info.decode('utf-8')
    
    db_exp_date = []
    cert_names = []
    
for line in text.splitlines():
    line = line.strip()  # remove leading/trailing spaces
    if line.startswith("db-exp-date:"):
        date_expiry = (line.split(":", 1)[1].strip()).split("(", 1)[1].strip(")")
        db_exp_date.append(date_expiry) # extract value after colon
    if line.startswith("db-name:"):
        db_name = line.split(":",1)[1].strip()
        cert_names.append(db_name)

cert_names_exp_dates = []
cert_names_exp_dates = {key: value for key, value in zip(cert_names, db_exp_date)}


for name, expiry in cert_names_exp_dates.items():
    expiry_date = datetime.strptime(expiry, "%b %d %H:%M:%S %Y %Z")
    now = datetime.utcnow() 
    days_left = (expiry_date - now).days
    if days_left < 0:
        print(f"Certificate {name} Expired !!! ")
        logging.info(f" Certificate {name} Expired !!! at {expiry_date}")
    elif expiry_date - now <= timedelta(days=30):
        print(f"Certificate {name} Expiry is within 30 days! On {expiry_date}")
        logging.info(f" Certificate {name} Expiry is within 30 days! On {expiry_date} at {datetime}")

