                   # Quiero la clase Prueba
from Prueba import Prueba
     # Del fichero Prueba.py
from subprocess import run, PIPE
from selenium import webdriver
import re

class PruebaSelenium(Prueba):
        
    def __init__(self, nombre=None, timeout=0, intervalo=0, numero_fallos_permitidos_consecutivos=0 ):
        super().__init__(nombre, timeout, intervalo, numero_fallos_permitidos_consecutivos)
        
    def ejecutar(self, servidor):
        resultado=True
        driver=webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities={
                    "browserName": "firefox"
            }
        )
    
        try:
            driver.implicitly_wait(10)
            
            driver.get(self.url)
            
            
            for operacion in self.operaciones:
               if operacion.get("escribir") is not None:
                    driver.find_element_by_xpath(operacion.get("elemento") ).send_keys(operacion.get("escribir"))
               elif operacion.get("click") is not None:
                    driver.find_element_by_xpath(operacion.get("elemento") ).click()
               elif operacion.get("comprobar_no_texto") is not None:
                    texto_del_elemento=driver.find_element_by_xpath(operacion.get("elemento") ).text
                    if re.match(".*"+operacion.get("comprobar_no_texto") ,texto_del_elemento.lower()):
                        resultado= False
        
        finally:
            driver.quit()
    
        return resultado