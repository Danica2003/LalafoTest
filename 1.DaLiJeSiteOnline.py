# Da li je "up and running”, tj. da li sajt funkcioniše normalno.

import Constant
import requests
from selenium import webdriver

driver=webdriver.Chrome()

def isSiteOnLine(siteURL):
    response= requests.get(siteURL)
    if(response.status_code==200):
        return True
    else:
        return False

if(isSiteOnLine(Constant.BASE_URL_LALAFO)==True):
    print('Lalafo je online')
else:
    print('lalafo nije online')

driver.close()

