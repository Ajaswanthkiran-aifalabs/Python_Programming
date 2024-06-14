

# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv()


import logging
import os 

import re
def check(phno):

    exp1=os.getenv("exp1")
    

    if re.search(exp1[0],phno)==None:
        print()
        logging.warning("\nThe provided phone number is not in correct formate retry!")
        return False


    return True



    

    