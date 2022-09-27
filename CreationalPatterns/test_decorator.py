import functools
from singleton import logger, update_log_attr
import uuid

def frame_event(fn):
    @functools.wraps(fn)
    def wrapper(record):
        # ensure correlationID
        correlation_id = lambda: str(uuid.uuid4())

        # logger.info("Inside Wrapper function")
        
        # configure correlationID
        update_log_attr("correlation_id", correlation_id())

        fn(record)

        update_log_attr("correlation_id", "")
        logger.info("Exit from wrapper function")
        return
    return wrapper