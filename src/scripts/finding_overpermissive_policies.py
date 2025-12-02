
# ===== Script for finding overpermissive policies

import panos
import os
import logging
import datetime
from panos.firewall import Firewall
from panos.objects import AddressObject,  AddressGroup, Tag
from panos.policies import Rulebase, SecurityRule, NatRule, RulebaseHitCount
from dotenv import load_dotenv
from datetime import datetime
import json
from pathlib import Path



project_root = Path(__file__).resolve().parent.parent.parent
load_dotenv(project_root / ".env") 

log_file = project_root / "logs" / "firewall_logs.log"
logging.basicConfig(filename=f'{log_file}', level=logging.INFO)


logging.info(f"Script for finding overpermissive rules is running at {datetime.now()}")


load_dotenv() 



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
   
    firewall = Firewall(firewall_host, username, password)

   

    rulebase = firewall.add(Rulebase())
    security_policies = SecurityRule.refreshall(rulebase)

    
    print(f"Firewall host --- {firewall_host}")
    for policy in security_policies:
    # if "any" in policy.source and "None" in policy.log_setting:
        if (policy.log_setting is None and "any" in policy.source and "any" in policy.service):
           print(policy)