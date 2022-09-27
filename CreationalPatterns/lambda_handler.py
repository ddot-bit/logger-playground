from test_decorator import frame_event
from singleton import logger

def lambda_handler(event, context):
    for record in event.values():
        handle_event(record)

@frame_event
def handle_event(r):
    logger.info(f"Inside function: {handle_event.__name__}. Payload: {r}")
    do_business_logic(r)
    return r

def do_business_logic(r):
    logger.info(f"Inside function: {do_business_logic.__name__}. Payload: {r}")
    r += 1
    logger.info(f"Modified record. r = {r}")
    return r

lambda_handler({"a":-1, "b":-2, "c":-3}, {})