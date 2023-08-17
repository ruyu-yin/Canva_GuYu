# coding:utf-8
import types
import inspect

from Log.log import Logger

_failed_expectations = []   # verification exceptions
_is_first_call = dict()     # verification exceptions
_file_logger = None         # file logger
_console_logger = None      # console logger


class VerifyType:
    FAIL_AND_STOP = 0
    FAIL_AND_CONTINUE = 1
    SKIP_FAIL = 2
    logger =Logger().logger

    def get_failed_expectations(self):
        global _failed_expectations
        return _failed_expectations


    def set_file_logger(self,logger):
        global _file_logger
        _file_logger = self.logger


    def set_console_logger(logger):
        global _console_logger
        _console_logger = logger


    def verify(expr, verify_type=VerifyType.FAIL_AND_STOP, msg=None):
        """
        keeps track of failed expectations
        :param expr: expect expression
        :param verify_type: throw the exception or not
        :param msg: customized error message
        """
        global _failed_expectations, _is_first_call
        # get stack caller, first caller clear the exception list
        caller = inspect.stack()[1][3]
        if _is_first_call.get(caller, True):
            _failed_expectations = []
            _is_first_call[caller] = False

        """
        Python lambda does not support statement inside lambda, so
        `lambda: assert 1 == 1` won't work as it's not valid lambda expression
        """
        if isinstance(expr, types.FunctionType):
            try:
                expr()
            except Exception as e:
                _log_and_handle_failure(verify_type, e)
        elif not expr:
            _log_and_handle_failure(verify_type, msg)


    def assert_expectations():
        """
        raise an assert if there are any failed expectations
        :return:
        """
        if _failed_expectations:
            raise AssertionError(_report_failures())


    def _log_and_handle_failure(verify_type, msg=None):
        """
        log the failure in memory
        :param verify_type: verify type
        :param msg: error message
        """
        (file_path, line, func_name, context_list) = inspect.stack()[2][1:5]
        context = context_list[0]
        exception_info = 'Failed at "' + '%s:%s' % (file_path, line) + '", in %s()%s\n%s' % (func_name, ('\n\t' + 'ErrorMessage:' + '\t%s' % msg), context)

        # log exception
        if _file_logger:
            _file_logger.warning(exception_info)
        if _console_logger:
            _console_logger.warning(exception_info)

        # FAIL_AND_STOP
        if verify_type == VerifyType.FAIL_AND_STOP:
            raise AssertionError(exception_info)
        # FAIL_AND_STOP
        elif verify_type == VerifyType.FAIL_AND_CONTINUE:
            _failed_expectations.append(exception_info)
        # SKIP_FAIL
        else:
            pass


    def _report_failures():
        """
        log all verification expectations and return as list
        :return: verification expectations as list
        """
        report = []
        global _failed_expectations
        if _failed_expectations:
            (file_path, line, func_name) = inspect.stack()[2][1:4]
            report = [
                '\n\nverify_expectations() called at', '"%s:%s"' % (file_path, line) + ' in %s()\n' % func_name, 'Failed Expectations : %s\n' % len(_failed_expectations)]
            for i, failure in enumerate(_failed_expectations, start=1):
                report.append('%d: %s' % (i, failure))
            _failed_expectations = []
        return '\n'.join(report)
