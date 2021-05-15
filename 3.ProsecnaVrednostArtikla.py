from selenium import webdriver
import Constant
import Locators
import time
# Izračunati prosečnu vrednost svih artikala koji su izlistani na prvoj stranici.
# ukupan broj sukanja je 4545 (sto smo dobili iz predhodne pretrage zadatka 2)
# da bih nasla prosecnu vrednost suknje napravicu opseg cena 

def NadjiSuknje(min, max):
    driver=webdriver.Chrome()
    driver.get(f'{Constant.BASE_URL_LALAFO}{Constant.PRETRAGA_URL_SUKNJE_MIN_MAX}')
    

    minField= driver.find_element_by_css_selector(Locators.opseg_cena_min)
    maxField= driver.find_element_by_css_selector(Locators.opseg_cena_max)
    brSuknji= driver.find_element_by_css_selector(Locators.filter_dugme_br_artikala_css_s)

    minField.send_keys(min)
    maxField.send_keys(max)

    brSuknji.click()

# Ne znam kako da implementiram recnik u ovo pa cu morati pojedinacno opseg vrednosti
# mogu da unosim vrednost koju ocita, ili da je stavim u print, ali svakako je rucno
NadjiSuknje(1,500)
time.sleep(5)
print(int(input('od 1 do 500 dinara ima ukupno oglasa: ')))
NadjiSuknje(501,1000)
time.sleep(5)
print(int(input('od 501 do 1000 dinara ima ukupno oglasa: ')))
NadjiSuknje(1001,5000)
time.sleep(5)
print(int(input('od 1001 do 5000 dinara ima ukupno oglasa: ')))
NadjiSuknje(5001,10000)
time.sleep(5)
print(int(input('od 5001 do 10000 dinara ima ukupno oglasa: ')))
NadjiSuknje(10001,15000)
time.sleep(5)
print(int(input('od 10001 do 15000 dinara ima ukupno oglasa: ')))
NadjiSuknje(15001,20000)
time.sleep(5)
print(int(input('od 15001 do 20000 dinara ima ukupno oglasa:  ')))
#tako sam dobila da je

x=2102
y=1341
z=962
g=17
o=1
w=2
# prelazimo na polje 4.prosecna vrednost za analizu cene