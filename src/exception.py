import sys

def error_message_detail(error,error_deatil:sys):
    __,__,exc_tb=error_deatil.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number[{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    
    return error_message

class CustomExecption(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_deatil=error_detail)

    def __str__(self):
        return self.error_message   