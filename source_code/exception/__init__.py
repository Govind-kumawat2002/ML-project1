import sys
class InsuranceException(Exception):
    def __init__(self,error_message:Exception,error_detail:sys ):
        super().__init__(error_message)
        self.error_message = InsuranceException.error_message_detail(error_message,error_detail=error_detail)
    @staticmethod
    def error_message_detail(error:Exception,error_detail:sys)->str:
        error_class,error_message,exe_tb = error_detail.exc_info()
        line_number=exe_tb.tb_frame.f_lineno
        file_name =exe_tb.tb_frame.f_code.co_filename
        error_message=f"filename {file_name},and line number {line_number},and error class {error_class}"
        return error_message
    def __str__(self):
        return InsuranceException.__name__.__str__()




