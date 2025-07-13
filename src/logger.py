import logging
import os # to work with file paths (cross-platform)
from datetime import datetime
# Automatically writes logs to .log files

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #Generates a filename like: 07_13_2025_12_11_30.log,So every time you run your project, a new log file is created with the exact time
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #Combines your current working directory + logs/ + log filename
os.makedirs(logs_path,exist_ok=True) #creates the folder if it doesn’t exist

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

#This configures how logs will be written into the file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", #Defines what each log line looks like
    level=logging.INFO, #Only logs INFO and above (INFO, WARNING, ERROR, CRITICAL)
)

#to check:-
'''
if __name__=="__main__":
    logging.info("logging has started") = logs will be created with  [ 2025-07-13 16:10:26,290 ] 21 root - INFO - logging has started

'''
