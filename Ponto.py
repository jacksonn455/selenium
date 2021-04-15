# -*- encoding: utf-8 -*-

# Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import os

# Intra-imports
from driver import driver

username = ''
password = ''

class Ponto:
    def __init__(self, driver):
        self.driver = driver
        self.start()

    def __str__(self):
        return self.driver

    def start(self):
        self.paginaInicial()
        self.dashBoard()
        self.horaManhaInicial()
        self.minutoManhaInicial()
        self.horaManhaFinal()
        pass

    def paginaInicial(self):
        # Acessar painel de login
        print('PAGINA INICIAL')
        self.driver.get('https://www.dimepkairos.com.br/Dimep/Account/LogOn?ReturnUrl=%2F')
        print('     Inserindo usuario e senha')
        # Insere user
        self.driver.waitForSelector(
            '#LogOnModel_UserName').send_keys(username)
        # Insere senha
        self.driver.waitForSelector(
            '#LogOnModel_Password').send_keys(password)
        # Clica no botao de logon
        print('     Clicando no botao para logar')
        self.driver.waitForSelector('#btnFormLogin').click()
      
    pass

    def dashBoard(self):
        print('     Fechando Poup-up')
        #Fecha popup
        actions = ActionChains(self.driver)
        page = self.driver.find_element_by_tag_name('html')
        self.driver.waitForSelector('#conpass-tag > div > div.sc-jTzLTM.fJrlJd.conpass-step.conpass-notification.conpass-show > div.sc-bdVaJa.fnqArd.conpass-close-button').click()
        time.sleep(1)
        print('     Clicando no perfil')
        self.driver.waitForSelector('#UserName').click()
        time.sleep(1)
        print('     Clicando em pessoa')
        self.driver.waitForSelector('#UserMenu > div:nth-child(1) > span').click()
        time.sleep(1)
        print('     Clicando em pedidos')
        self.driver.waitForSelector('#UserProfilePedidosJustificativas > span').click()
    pass

    def horaManhaInicial(self):
        print('     Entrada do horario da manha')
        actions = ActionChains(self.driver)
        page = self.driver.find_element_by_tag_name('html')
        self.driver.waitForSelector('#ApontID6 > div:nth-child(12)').click()
        self.driver.waitForSelector('#ui-datepicker-div > div.ui-timepicker-div > dl > dd.ui_tpicker_hour > div > a').click()
        self.driver.actions.move_to_element_with_offset(page, 1024, 603)
        self.driver.actions.click_and_hold()
        self.driver.actions.move_to_element_with_offset(page, 1088, 598)
        self.driver.actions.release().perform()
        time.sleep(1)
    pass

    def minutoManhaInicial(self):
        actions = ActionChains(self.driver)
        page = self.driver.find_element_by_tag_name('html')
        print('     Entrada do minuto da manha')
        self.driver.actions.send_keys(Keys.ESCAPE).perform()
        self.driver.waitForSelector('#ui-datepicker-div > div.ui-timepicker-div > dl > dd.ui_tpicker_minute > div > a').click()
        time.sleep(1)
        self.driver.actions.move_to_element_with_offset(page, 1024, 625)
        self.driver.actions.click_and_hold()
        self.driver.actions.move_to_element_with_offset(page, 1105, 625)
        self.driver.actions.release().perform()
        self.driver.actions.move_to_element_with_offset(page, 875, 795).click()
        time.sleep(1)
        self.driver.waitForSelector('#ui-datepicker-div > div.ui-datepicker-buttonpane.ui-widget-content > button.ui-datepicker-close.ui-state-default.ui-priority-primary.ui-corner-all').click()
        time.sleep(1)
        self.driver.actions.send_keys(Keys.ESCAPE).perform()
    pass

    def horaManhaFinal(self):
        actions = ActionChains(self.driver)
        page = self.driver.find_element_by_tag_name('html')
        print('     saida do horario da manha')
        self.driver.actions.move_to_element_with_offset(page, 875, 795).click()
        time.sleep(1)
        self.driver.actions.move_to_element_with_offset(page, 1086, 546).click()
        time.sleep(1)
        self.driver.actions.move_to_element_with_offset(page, 1026, 648)
        self.driver.actions.click_and_hold()
        self.driver.actions.move_to_element_with_offset(page, 1115, 645)
        self.driver.actions.release().perform()
        time.sleep(1)
        self.driver.waitForSelector('#ui-datepicker-div > div.ui-datepicker-buttonpane.ui-widget-content > button.ui-datepicker-close.ui-state-default.ui-priority-primary.ui-corner-all').click()
        time.sleep(1)
        self.driver.actions.send_keys(Keys.ESCAPE).perform()
        time.sleep(1)
    pass

    def horaTardeInicial(self):
        print('     Entrada do horario da manha')
        actions = ActionChains(self.driver)
        page = self.driver.find_element_by_tag_name('html')
        time.sleep(1)
        self.driver.actions.send_keys(Keys.ESCAPE).perform()
        self.driver.waitForSelector('#ApontID6 > div:nth-child(16)').click()
        time.sleep(1)
        self.driver.actions.move_to_element_with_offset(page, 1089, 690)
        self.driver.actions.click_and_hold()
        self.driver.actions.move_to_element_with_offset(page, 1184, 691)
        self.driver.actions.release().perform()
        self.driver.actions.move_to_element_with_offset(page, 875, 795).click()
        time.sleep(1)
        self.driver.waitForSelector('#ui-datepicker-div > div.ui-datepicker-buttonpane.ui-widget-content > button.ui-datepicker-close.ui-state-default.ui-priority-primary.ui-corner-all').click()
        time.sleep(1)
    pass