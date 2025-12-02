

# ==== Validating the IP address is correct format 


from imports import *

ipv4_pattern = re.compile(
    r'^('
    r'(25[0-5]|'     # 250-255
    r'2[0-4][0-9]|'  # 200-249
    r'[0-1]?[0-9]{1,2})'  # 0-199
    r'\.){3}'        # dot three times
    r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})$'  # last octet
)

def valid_ip(ip):
    if not ipv4_pattern.match(ip):
        print("You entered invalid IP address")
        logging.info(f"IP address is invalid at {datetime.now()}")
        sys.exit(f"Script aborted.")