import sys # any exception that we need to control sys library will automatically have it, sys helps access detailed exception information like filename & line number.
#`sys` → gives access to the **traceback info** (like filename and line number) when an error occurs.
from src.logger import logging
# `logging` → imports the logger you’ve defined, so you can log error messages if needed.

# whenever u sue try catch u just raise a custom exception then this will be activated
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    
# customexception class Automatically shows you the file name, line number, and error message whenever something fails
# Can be raised inside any try-except block
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys): # error detail should be of type sys
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self): #__str__ method automatically called to convert the exception into a string
        return self.error_message #This means that if you print the exception or log it, it will automatically show your custom error message instead of a boring default one.

'''
for testing the logging of error :-
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("divison by zero error")
        raise CustomException(e,sys)
'''
