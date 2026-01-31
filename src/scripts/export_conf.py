
# ===== Script for exporting running configuration from firewall and storing it locally

import panos
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
from datetime import datetime
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.op_config import show_running_conf

def export(firewall, project_root):


    log_file = project_root / "logs" / "firewall_logs.log"
    logging.basicConfig(filename=f'{log_file}', level=logging.INFO)

    current_date = datetime.now()
    date_string = current_date.strftime("%d-%m-%Y-%H-%M-%S")

    logging.info(f"Script for exporting configuration is running {datetime.now()}")
    conf_file = project_root / "data" / "backups" / f"fw_conf__{date_string}.xml"

    show_running_conf(firewall, conf_file, date_string)


