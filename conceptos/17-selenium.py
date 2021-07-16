from selenium import webdriver
import re

driver=webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities={
                "browserName": "firefox"
        }
    )

try:
    driver.implicitly_wait(10)
    
    driver.get("http://www.itnow.es/")
    print(driver.title)

    # Buscar un elemento dentro de la web.....                      Y hacemos algo en el
    driver.find_element_by_xpath("//input[@id='txtBuscar']")                            .send_keys("servicios")
    driver.find_element_by_xpath("//input[@id='ctl00_BuscadorMenu1_bt_search']")        .click()
    #try:
    #    driver.find_element_by_xpath("//h2[contains(text(),'Error')]") 
    #except: # Se produce si el elemento no existe
    texto_del_h2=driver.find_element_by_xpath("//h2[contains(@class,'ms-search-header')]") .text
    print(texto_del_h2)
    if re.match(".*error",texto_del_h2.lower()):
        print("La busqueda de la web no esta funcionando")
    else:
        print("la busqueda de la web si que funciona")
    
finally:
    driver.quit()
