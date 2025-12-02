import panos
import ipdb
import os
import logging
import datetime
from panos.firewall import Firewall
from panos.objects import AddressObject,  AddressGroup, Tag
from panos.policies import Rulebase, SecurityRule, NatRule, RulebaseHitCount
from dotenv import load_dotenv
from datetime import datetime
from commit_configuration import commit_function
import xml.etree.ElementTree as ET
from pathlib import Path

load_dotenv() 
project_root = Path(__file__).resolve().parent.parent.parent

log_file = project_root / "logs" / "firewall_logs.log"
logging.basicConfig(filename=f'{log_file}', level=logging.INFO)


logging.info(f"Script for showing system info is running {datetime.now()}")


# ===== Loading environmental variables form .env file

firewall_host = os.getenv("firewall_host1")
username = os.getenv("user1")
password = os.getenv("pass1")

# ===== creating firewall object and connecting to it 

firewall = Firewall(firewall_host, username, password)
configuration = firewall.op("show system info", xml=True)

if isinstance(configuration, bytes):
    config_str = configuration.decode("utf-8")

elif isinstance(configuration, str):
    config_str = configuration

else:  
    config_str = ET.tostring(configuration, encoding="unicode")

print(config_str)