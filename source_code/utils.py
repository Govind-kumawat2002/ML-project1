from source_code.logger import logging
from source_code.exception import InsuranceException
from source_code.dbconfig import connect_to_mogodb,connect_to_mysql


def is_mongoconnected(mongo_connections):
    if mongo_connections is not None:
        print("connected ")
    else:
        print("not connected")
