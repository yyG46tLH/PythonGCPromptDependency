# This is a core GCC library for logging application outputs.
import logging
import os

def set_gcp_sdk_logging(mygcp):
    # print('...at set_gcp_sks_logging...')
    mygcp.configuration.logger.log_level = mygcp.logger.LogLevel.LError
    mygcp.configuration.logger.log_request_body = True
    mygcp.configuration.logger.log_response_body = True
    mygcp.configuration.logger.log_format = mygcp.logger.LogFormat.TEXT
    mygcp.configuration.logger.log_to_console = False
    mygcp.configuration.logger.log_file_path = os.environ['GENESYS_CLOUD_SDK_LOG']
    return mygcp

# Instantiate a logger object and return it.
def init_logger(log_filename, log_level):
    logging.basicConfig(filename=log_filename, level=log_level,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    new_logger = logging.getLogger('GCC_Logger')
    return new_logger
