
# ===== Script for disabling polices with zero hit count 

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
import json
import subprocess
from export_conf import export
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
load_dotenv(project_root / ".env") 


log_file = project_root / "logs" / "firewall_logs.log"
logging.basicConfig(filename=f'{log_file}', level=logging.INFO)

logging.info(f"Script for disabling policies with 0 hits is running at {datetime.now()}")


backup_file = project_root / "src" / "scripts" / "exporting_configuration.py"
#subprocess.run(["python", ".\src\scripts\exporting_configuration.py"])
subprocess.run(["python", f"{backup_file}"])

# ===== Loading environmental variables form .env file

#firewall_host = os.getenv("firewall_host1")
#username = os.getenv("user1")
#password = os.getenv("pass1")

# ===== creating firewall object and connecting to it 
#firewall = Firewall(firewall_host, username, password)

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

    export(firewall, project_root)
    rulebase = firewall.add(Rulebase())
    security_policies = SecurityRule.refreshall(rulebase)

    rulebase_hit_count = RulebaseHitCount(firewall)
    hit_count = rulebase_hit_count.refresh(style="security", rules=security_policies)

    tags = Tag.refreshall(firewall)
    
    # printing rule name and number of hits
    '''
    for rule_name, hit in hit_count.items():
        ipdb.set_trace()
        print(f"Rule: {rule_name}  Hit count: {hit.hit_count}")
    '''

    # delete policies who are disabled, action = deny and tag TO_DELETE
    for policy in security_policies:
        hit = hit_count.get(policy.name)
        if policy.disabled == True and policy.action == "deny":
            print(f'Rule {policy} is deleted')
            policy.delete()
            

    #commit_function(firewall)
# ===== commiting changes to the firewall

