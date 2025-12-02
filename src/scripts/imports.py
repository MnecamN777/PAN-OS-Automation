
# ==== all import modules

import panos
import ipdb
import os
import sys
import logging
import datetime
from ipaddress import ip_address, IPv4Address, IPv6Address
from panos.firewall import Firewall
from panos.errors import PanDeviceError
from panos.objects import AddressObject,  AddressGroup
from dotenv import load_dotenv
from datetime import datetime
import re
import json
from pathlib import Path