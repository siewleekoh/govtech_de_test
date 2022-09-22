import logging
import os
from datetime import datetime


print(os.getcwd())
log_path = os.path.join(os.getcwd(), "..", "logs")

if not os.path.exists(log_path):
    os.makedirs(log_path)


logger = logging.getLogger(__name__)
fh = '{:%Y%m%d%H%M}.log'.format(datetime.now())

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S', filename=log_path + fh, filemode='w')


#
#
#
# import logging
# from datetime import datetime
# import os
#
# # # Gets or creates a logger
# # logger = logging.getLogger(__name__)
# # logger.setLevel(logging.INFO)
#
# # define file handler and set formatter
# fh = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.now()))
# #formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s')
# #fh.setFormatter(formatter)
#
# print(os.getcwd())
# log_path = os.path.join(os.getcwd(), "logs")
#
# if not os.path.exists(log_path):
#     os.makedirs(log_path)
# #log_filename = os.path.join()
# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S', filename='logs/' + fh, filemode='w')
#
#
# from . import main