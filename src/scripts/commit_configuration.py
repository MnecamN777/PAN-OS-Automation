
# ===== commiting changes to the firewall


from imports import *

def commit_function(firewall):
    try:
        firewall.commit()
        logging.info(f"Configuration commited at {datetime.now()}")
    except Exception as e:
        logging.error(f"Commit failed as {e}")
        sys.exit("Script aborted due to failed commit.")