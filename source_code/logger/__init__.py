import logging , os # create the log file in our projects
from datetime import datetime 
dir_name = "insurance_log"
# os.makedirs(dir_name,exist_ok=True)
time_stamp =datetime.now().strftime("%d-%m-%y-%H-%M-%S")
file_name=time_stamp+".log"
log_file_path = os.path.join(dir_name,file_name)
# print(log_file_path)


logging.basicConfig(filename=log_file_path,level=logging.DEBUG,filemode='w',format='%(asctime)s-%(levelname)s,%(message)s')