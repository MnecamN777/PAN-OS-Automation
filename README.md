# Palo Alto Firewall Automation

This project provides a set of Python automation scripts for managing Palo Alto Networks firewalls.  
It includes scripts for configuration management, security checks, policy cleanup, SSL certificate monitoring, and orchestration across multiple firewalls.  

---

Project Structure

firewall-automation/
│
├── src/

│   ├── core/

│   │   └── __init__.py
        | op_config.py
        
│   │
│   ├── scripts/ 

│   │   ├── blocking_soc_ip_address.py

│   │   ├── certifcation_expiry_check.py

│   │   ├── creating_address_object.py

│   │   ├── adding_object_to_group.py

│   │   ├── disable_0_hit_rules.py

│   │   ├── delete_disabled_rules.py

│   │   ├── export_conf.py

│   │   ├── finding_overpermissive_rules.py

│   │   ├── exporting_configuration.py

│   │   ├── commit_configuration.py

|   |   ├── send_email.py

│   │   ├── showing_system_info.py

│   │   └── __init__.py
│   
│                      
│
├── config/

│   ├── fw_credentials.json

│   ├── fw_credemtials.example.json  
│   
│
├── data/

│   ├── bad_ips.txt   

│   └── backups/                    
│
├── logs/                           
│   └── firewall_logs.log
│
│
├── requirements.txt

├── .env                

├── .gitignore

├── README.md


---

Features

1. **Monitor SSL Certificate Expiration**  
   - Query certificates 
   - Alert if any certificate expires within 30 days  

2. **Policy Management**  
   - Identify overly permissive rules
   - Disable zero-hit rules and add tag TO-DELETE
   - Delete disabled policies

3. **Address Objects & Groups**  
   - Create address objects   
   - Add them to address groups  
   - Validate IP addresse

4. **Firewall Configuration Management**  
   - Automated backup of configuration   
   - Commit configuration

5. **Orchestration Across Multiple Firewalls**  
   - Run scripts at SOC-scale  
   - Centralized workflow management  
   - Block Malicious IP address from SOC report
   - Send mail to SOC after blocking IP address

6. **Logging**  
   - Centralized logging for all operations  

---

Installation

1. Clone the repository:

git clone https://github.com/MnecamN777/PAN-OS-Automation

2. In .env file put your credentials for the firewalls:
firewall_host1= 
user1= 
pass1=

3. To run scripts on mutliple firewalls add data in fw_credentials.json for every new firwall in .env file
 {
    "vendor": "paloalto",
    "ip_env": "firewall_host1",
    "username_env": "user1",
    "password_env": "pass1",
    "policy_package": "SOC"
  }

 4. Run scripts python src/scripts/_script_name 




Developed a Python-based Palo Alto firewall automation suite using the PAN-OS SDK, enabling certificate monitoring, policy optimization, address-object orchestration, multi-firewall configuration backups, and automated SOC workflows (malicious IP blocking, alerting). Improved operational efficiency, accuracy, and consistency across security teams.

