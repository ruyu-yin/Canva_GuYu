import time


def wait_for(condition_function, timeout_seconds = 30, interval_second = 1):
    start_time = time.time()
    while time.time() < start_time + timeout_seconds:
        if condition_function:
            return True
        else:
            time.sleep(interval_second)
    raise Exception('Wait Time out')


def wait_for_string_result(context, string_function, timeout_seconds = 70, interval_second = 10):
    start_time = time.time()
    while time.time() < start_time + timeout_seconds:
        result = string_function
        if result == '':
            if context is not None:
                context.logger.info('Waiting....')
            time.sleep(interval_second)
        else:
            return result
    raise Exception('Time out, waiting non-empty string result')
