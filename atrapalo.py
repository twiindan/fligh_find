# coding: utf-8
__author__ = 'artanis'

from selenium import webdriver
from configuration import BASE_URL, ORIGIN, DESTINATION

if __name__ == "__main__":

    import calculate_dates

    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    verificationErrors = []
    accept_next_alert = True
    dates_dict = calculate_dates.calculate_ranges()
    for dates in dates_dict:

        driver.get(BASE_URL + "/")
        driver.find_element_by_id("origen").clear()
        driver.find_element_by_id("origen").send_keys(ORIGIN)
        driver.find_element_by_id("destino").clear()
        driver.find_element_by_id("destino").send_keys(DESTINATION)
        driver.find_element_by_id("fecha_salida").clear()
        driver.find_element_by_id("fecha_salida").send_keys(dates['fecha_origen'])
        driver.find_element_by_id("fecha_regreso").click()
        driver.find_element_by_id("fecha_regreso").clear()
        driver.find_element_by_id("fecha_regreso").send_keys(dates['fecha_destino'])
        driver.find_element_by_id("vue").click()
        precio = driver.find_element_by_xpath("//form[@id='form0']/div/div[2]/div/a/span").text
        dates[precio] = precio
        print dates

