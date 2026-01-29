
# ===== Script for exporting running configuration from firewall and storing it locally

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
import json
import sys
from pathlib import Path
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.op_config import show_running_conf


project_root = Path(__file__).resolve().parent.parent.parent
load_dotenv(project_root / ".env") 

log_file = project_root / "logs" / "firewall_logs.log"
logging.basicConfig(filename=f'{log_file}', level=logging.INFO)


logging.info(f"Script for exporting configuration is running {datetime.now()}")





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
    username = fw["user"]
    password = fw["password"]

    current_date = datetime.now()
    date_string = current_date.strftime("%d-%m-%Y-%H-%M-%S") 
    conf_file = project_root / "data" / "backups" / f"fw_conf_{firewall_host}_{date_string}.xml"

    firewall = Firewall(firewall_host, username, password)


    show_running_conf(firewall, conf_file, date_string)
    #configuration = firewall.op("show config running", xml=True)

    #if isinstance(configuration, bytes):
    #    config_str = configuration.decode("utf-8")

    #elif isinstance(configuration, str):
    #    config_str = configuration

    #else:  
    #    config_str = ET.tostring(configuration, encoding="unicode")

    #with open(conf_file, "w", encoding='utf-8') as file:
    #    file.write(config_str)
    #    logging.info(f"Configuration exported to data folder --- fw_conf_{firewall_host}_{date_string}.xml {datetime.now()}")


