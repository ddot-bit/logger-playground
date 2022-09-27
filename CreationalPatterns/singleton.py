"""
    Ensure a class only has one instance, and 
    provide a global point of access to it.

    Example:
        - Configuring a logger at one place and using an instance of that
            logger accross your app / codebase
        - Current implementation of the codebase for evaluating feature
            flags
"""
"""
Have a logging class
1. format logging
2. filter each log to not have logger throw errors (like what we have now)
3. provide a method to add atribures
4. need to chache attributes
5. need to configure log record dynamically
6. Need to remove attributes
"""
import logging
# Need to chache attribute names in order to properly format logger
# Need to loop through and format the logger
# need to update the format of the logger
class NoParsingFilter(logging.Filter):
    """
    https://stackoverflow.com/questions/879732/logging-with-filters
    """
    def filter(self, record):
        # Error is thrown by logging module when the attribute is not populated
        # Need to keep what is currently in place but generalize to handle all attributes
        return not record.getMessage().startswith('correlation_id') # can use this to validate all types

cache_attr_name = {}
FILE_FORMAT = (
    "Message: %(message)s"
    "\nCORRELATION ID: %(correlation_id)s"
    "\n"
)

logger = logging.getLogger()
old_factory = logging.getLogRecordFactory()
def record_factory_factory(name, val):
    """
    https://stackoverflow.com/questions/59585861/using-logrecordfactory-in-python-to-add-custom-fields-for-logging
    """
    def record_factory(*args, **kwargs):
        """
        Provided by logging documentation
        https://docs.python.org/3/library/logging.html#logging.LogRecord.getMessage
        """
        record = old_factory(*args, **kwargs)
        setattr(record, name, val)
        return record
    return record_factory

def update_log_attr(attr_name: str, attr_val):
    logging.setLogRecordFactory(record_factory_factory(attr_name, attr_val))
    return

logging.basicConfig(filename="APPLES.log", format=FILE_FORMAT)
# record_factory_factory("whatever")
# update_log_attr("whatever")
# logging.setLogRecordFactory(record_factory_factory("whatever"))
logger.setLevel(logging.INFO)
logger.addFilter(NoParsingFilter())

# for i in range(2):
#     logging.info("test")
#     update_log_attr(str(i))
