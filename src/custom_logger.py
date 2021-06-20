import logging
import os

def get_logger(name):
    """
        get_logger creates the logger object
        :param name: name of the module
    	:type name: str
    	:return: Return the logger object of the given module
    	:rtype: logging.Logger
    """

    #getting the log level from environment varibles. WARNING is the default log_level.
    log_level = os.getenv("LOG_LEVEL","WARNING")

    #create and configure the logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    #create console handler by setting the logelevel
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    #create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    #add the handler to the logger
    logger.addHandler(console_handler)

    return logger

