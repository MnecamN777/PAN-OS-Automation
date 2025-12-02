
# ===== creating address object and the firewall with name SOC_address_IP

from imports import *


def creating_address_objects(firewall, ips):
    created_objects = []
    for ip_blocked in ips:  

        address_object_existing = None
        
        try: 
            ip_address(ip_blocked)  # checking if it is a valid IP address, creating address object
            address_object_name = f'SOC_Address_{ip_blocked}'
            address_object = AddressObject(address_object_name, ip_blocked)
       
            address_object_existing = firewall.find(f'SOC_Address_{ip_blocked}', AddressObject)

        except ValueError:
         
            logging.info(f"IP address is invalid at {datetime.now()}, script aborted")
            sys.exit(f"Invalid IP address detected: {ip_blocked}. Script aborted.")
        

    # checking if address object already exists on the firewall
        if address_object_existing is not None: 
        
            logging.info(f"Address object already exists on the firewall {datetime.now()}")
            sys.exit(f"Address object already exists. Script aborted.")
        
        else:
            try:
                firewall.add(address_object)
                address_object.create() # pushing object to the device
                created_objects.append(address_object)
            except Exception as e:
                logging.error(f"Failed to push object to the firewall: {e}")
                sys.exit("Script aborted due to error pushing address object to the firewall.")

    return created_objects