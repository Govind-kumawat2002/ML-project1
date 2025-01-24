from source_code.logger import logging
from source_code.exception import InsuranceException
import sys

# # leval mode 
# logging.info("hello this is Govind ")
# logging.debug("hello this is Govind ")
# logging.warning("hello this is Govind ")
# logging.error("hello this is Govind ")
# logging.critical("hello this is Govind ")

try:
    10/0
except Exception as e :

    obj=InsuranceException(error_message=e,error_detail=sys)
    logging.warning(obj.error_message)
    # print(obj.error_message)