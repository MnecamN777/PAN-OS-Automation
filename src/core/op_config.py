
import logging
from datetime import datetime
import xml.etree.ElementTree as ET


def show_running_conf(firewall, conf_file, date_string):
    
    configuration = firewall.op("show config running", xml=True)

    if isinstance(configuration, bytes):
            config_str = configuration.decode("utf-8")

    elif isinstance(configuration, str):
            config_str = configuration

    else:  
            config_str = ET.tostring(configuration, encoding="unicode")

    with open(conf_file, "w", encoding='utf-8') as file:
            file.write(config_str)
            logging.info(f"Configuration exported to data folder --- fw_conf_{date_string}.xml {datetime.now()}")