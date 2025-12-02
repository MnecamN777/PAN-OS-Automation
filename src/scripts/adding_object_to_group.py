
# ===== adding address object to the address group

from imports import *

def adding_object_to_the_group(firewall, address_group_name, address_object):
        try:
            address_group = firewall.find(address_group_name, AddressGroup)
            address_group.static_value.append(address_object.name)
            address_group.apply()

            
            logging.info(f"Created address object {address_object.name} and added to group {address_group_name} at {datetime.now()}")

            print(f'Address object {address_object.name} is created on the firewall')

        except Exception as e:
            logging.error(f"Failed to add {address_object.name} to {address_group_name}: {e}")
            sys.exit("Script aborted due to error adding object to group.")
