import Constant
from selenium import webdriver
import time
import Locators

# pretrazicu suknje na Lalafo
# na dugmetu pretrazi, 
# koje je ujedno i filter dugme dobili smo 
# ukupan broj oglasa koji sadrze atikal suknja 4545 (sto je promenljiva jer ljudi stalno kace nove oglase)
# radimo pretragu u trenutku testiranja


def pretragaLalafo(artikli):
    driver=webdriver.Chrome()
    driver.get(f'{Constant.BASE_URL_LALAFO}{Constant.PRETRAGA_URL_LALAFO}')

    artikliPretragaPolje=driver.find_element_by_css_selector(Locators.sta_trazite_css_s)
    artikliPretragaPolje.send_keys(artikli)
    dugmePretraga=driver.find_element_by_css_selector(Locators.dugme_pretraga_css_s)
    dugmePretraga.click()

artikli={'suknja','pantalone','jakna','televizor'}
pretragaLalafo('suknja')

time.sleep(10)



