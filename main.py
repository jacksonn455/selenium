# Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import keys
import time
import pickle
import os

# Intra-imports
from driver import driver
from Ponto import Ponto

def start(driver):
    step = Ponto(driver)
    driver = step.getDriver()

start(driver)