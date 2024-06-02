import logging
import os
from datetime import datetime

# generating logfile with current timestamp
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# generating directory to store logs
log_path = os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)

# logfile path
LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

# logger object creation
logging.basicConfig(
            level=logging.INFO,
            filename=LOG_FILE_PATH,
            format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
